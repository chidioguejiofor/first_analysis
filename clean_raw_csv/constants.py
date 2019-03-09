import dotenv
import os

dotenv.load_dotenv()

CSV_FILENAME = os.getenv('CSV_FILENAME', 'raw_survey_data.csv')
TIDY_DATA_EXPORT_FILENAME = os.getenv('TIDY_DATA_EXPORT_FILENAME',  '2018 Tidy Data.xlsx')
# observations for python files that do not have
NOT_PYTHON_STR = 'No, I don’t use Python for my current projects'

DROP_NA = 1
REPLACE_NA = 2
CUSTOM_PROCESSING_FUNC = 3
BOTH_PYTHON_AND_NON_PYTHON_USERS = 4
