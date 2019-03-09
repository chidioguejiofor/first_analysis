import pandas as pd
from .constants import (
    DROP_NA, REPLACE_NA,
    CUSTOM_PROCESSING_FUNC, BOTH_PYTHON_AND_NON_PYTHON_USERS,
    TIDY_DATA_EXPORT_FILENAME
)
from .helpers import reshape_data
from .errors import InvalidProcessTechnique
from .dataframe_initializer import DataframeInitializer
import click
import importlib

def process_single_question(question_dict,question_str):
    if question_dict['number'] == 4:
        print(question_dict)

    if question_dict['processing_technique'] == DROP_NA:
        return reshape_data(
            question_dict['start_index'],
            question_dict['end_index'],
            question_str
        )
    elif question_dict['processing_technique'] == REPLACE_NA:
        return reshape_data(question_dict['start_index'],
                     question_dict['end_index'],
                     question_str,
                     dropna=False, fillna_with_str=question_dict['replace_str'])
    elif question_dict['processing_technique'] == CUSTOM_PROCESSING_FUNC:
        print(question_dict)
        module_path, function_name = question_dict['process_func'].rsplit('.', 1)
        func_args = question_dict.get('args', [])
        module = importlib.import_module(module_path)
        function_reference = getattr(module, function_name)
        return function_reference(*func_args)

    elif question_dict['processing_technique'] == BOTH_PYTHON_AND_NON_PYTHON_USERS:
        return reshape_data(
            question_dict['start_index'],
            question_dict['end_index'],
            question_str
        )
    else:
        raise InvalidProcessTechnique


def export_clean_file(output_filename=TIDY_DATA_EXPORT_FILENAME):
    if not output_filename.endswith('xlsx'):
        output_filename = '{}.xlsx'.format(output_filename)

    excel_writer = pd.ExcelWriter(output_filename,  engine='xlsxwriter')

    for question_str, question_dict in DataframeInitializer.questions.items():
        question_number = question_dict['number']
        click.echo('Processing question {}...'.format(question_number))
        final_dataframe = process_single_question(question_dict, question_str)
        final_dataframe.to_excel(excel_writer, sheet_name='Question {}'.format(question_number))

    click.echo('Saving the data to an excel sheet `{}`'.format(output_filename))
    excel_writer.save()
    click.echo('Saved successfully')