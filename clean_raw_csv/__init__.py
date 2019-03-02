from .constants import DROP_NA , REPLACE_NA, CUSTOM_PROCESSING_FUNC, BOTH_PYTHON_AND_NON_PYTHON_USERS
from .helpers import reshape_data
from .errors import InvalidProcessTechnique

def process_single_question(question_dict):
    if question_dict['processing_technique'] == DROP_NA:
        return reshape_data(
            question_dict['start_index'],
            question_dict['end_index'],
            question_dict['string']
        )
    elif question_dict['processing_technique'] == REPLACE_NA:
        return reshape_data(question_dict['start_index'],
                     question_dict['end_index'],
                     question_dict['string'],
                     dropna=False, fillna_with_str=question_dict['replace_str'])
    elif question_dict['processing_technique'] == CUSTOM_PROCESSING_FUNC:
        return question_dict['process_func']()

    elif question_dict['processing_technique'] == BOTH_PYTHON_AND_NON_PYTHON_USERS:
        return reshape_data(
            question_dict['start_index'],
            question_dict['end_index'],
            question_dict['string']
        )
    else:
        raise InvalidProcessTechnique

def export_clean_file():
    from .constants import QUESTIONS_CHARACTERISTICS
    list_of_cleaned_dfs= []
    for question_dict in QUESTIONS_CHARACTERISTICS:
        list_of_cleaned_dfs.append(process_single_question(question_dict))
    return list_of_cleaned_dfs