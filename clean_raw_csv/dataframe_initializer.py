import pandas as pd
import numpy as np
import json
import click

class DataframeInitializer:

    raw_data_df = None
    python_observations_df = None
    non_python_observations_df = None
    questions = {}

    @classmethod
    def initialise_dataframes(cls):
        from .constants import CSV_FILENAME, NOT_PYTHON_STR
        click.echo('Extracting data from the csv...')
        cls.raw_data_df = pd.read_csv(CSV_FILENAME, dtype=np.object, index_col=0)

        # extracting the observations into two dataframes
        cls.non_python_observations_df = cls.raw_data_df[cls.raw_data_df.iloc[:, 0] == NOT_PYTHON_STR]
        cls.python_observations_df = cls.raw_data_df[cls.raw_data_df.iloc[:, 0] != NOT_PYTHON_STR]

        # parsing the config file export_config.json
        click.echo('Parsing Config file...')
        config_file_settings = cls.parse_config_file()

        click.echo('Extracting questions...')
        cls.questions = cls.process_questions(cls.raw_data_df.columns, config_file_settings)

    @classmethod
    def process_questions(cls, dataframe_columns, config_file_settings=None):
        from .constants import DROP_NA
        final_dict = {}
        question_num = 1
        config_file_settings = config_file_settings if config_file_settings else {}

        default_processing_technique = {'processing_technique': DROP_NA}

        for index, column in enumerate(dataframe_columns):
            question_list = column.split(':')
            question_str = question_list[-1]

            if final_dict.get(question_str):
                final_dict[question_str]['end_index'] = index + 1
            else:
                final_dict[question_str] = {
                    'start_index': index,
                    'end_index': index + 1,
                    'number': question_num,
                    **config_file_settings.get(question_num, default_processing_technique)
                }
                question_num = question_num + 1

        return final_dict


    @classmethod
    def parse_config_file(cls, filename='export_config.json'):
        """Parses JSON config file

        Converts the JSON in the config file to a dict and returns it

        Args:
            filename: The JSON file that contains the configurations

        Returns:
            (dict): a dict containing the question number as key and the settings
            for that questions as values
        """
        final_dict = {}
        try:
            with open(filename) as f:
                data = json.load(f)
        except FileNotFoundError:
            return False

        for config_name, config_settings in data.items():
            if not cls.validate_config_key(config_name, config_settings):
                return False

            _ = [
                final_dict.update(cls._process_single_setting(config_name, setting))
                    for setting in config_settings
            ]

        return final_dict

    @staticmethod
    def _process_single_setting(config_name, setting):
        """Processes each setting in the config option

        Args:
            config_name: The config option name eg. fillna, custom_func, raw_dataset
            setting:

        Returns:
            (dict): a dict that contains the question number as key and processing options as value
        """
        from .constants import REPLACE_NA, CUSTOM_PROCESSING_FUNC, BOTH_PYTHON_AND_NON_PYTHON_USERS

        if isinstance(setting, int):
            return {
                setting: {
                    'processing_technique': BOTH_PYTHON_AND_NON_PYTHON_USERS,
                }
            }
        elif isinstance(setting, dict):
            return {
                setting['number']:  {
                    'processing_technique': REPLACE_NA if config_name == 'fillna' else CUSTOM_PROCESSING_FUNC,
                    'replace_str': setting.get('replace_str'),
                    'process_func': setting.get('process_func')
                }
            }
        return {}

    @classmethod
    def validate_config_key(cls, key, settings):
        return isinstance(settings, list) and \
               all(map(lambda option: cls._validate_config_key_helper(key, option), settings))

    @staticmethod
    def _validate_config_key_helper(key, option):
        config_test = {
            'fillna': isinstance(option, dict) and isinstance(option.get('number'), int) \
                and isinstance(option.get('replace_str'), str),
            'custom_func':isinstance(option, dict) and isinstance(option.get('number'), int) \
                and isinstance(option.get('process_func'), str),
            'raw_dataset': isinstance(option, int)

        }
        return config_test.get(key, False)

