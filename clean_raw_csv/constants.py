import dotenv
import os

from .helpers import process_question_six

dotenv.load_dotenv()

CSV_FILENAME = os.getenv('CSV_FILENAME', 'raw_survey_data.csv')
TIDY_DATA_EXPORT_FILENAME = os.getenv('TIDY_DATA_EXPORT_FILENAME',  '2018 Tidy Data.xlsx')
# observations for python files that do not have
NOT_PYTHON_STR = 'No, I don’t use Python for my current projects'

DROP_NA = 1
REPLACE_NA = 2
CUSTOM_PROCESSING_FUNC = 3
BOTH_PYTHON_AND_NON_PYTHON_USERS = 4

QUESTIONS_CHARACTERISTICS = [
    {
        'string': 'What other language(s) do you use?',
        'number': 2,
        'start_index': 2,
        'end_index': 26,
        'processing_technique': DROP_NA

    },
    {
        'string': 'For what purposes do you mainly use Python?',
        'number': 3,
        'start_index': 26,
        'end_index': 27,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What do you use Python for?',
        'number': 4,
        'start_index': 27,
        'end_index': 43,
        'processing_technique': DROP_NA
    },
    {
        'string': 'To what extent are you involved in the following activities?',
        'number': 5,
        'start_index': 43,
        'end_index': 59,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What do you use Python for the most?',
        'number': 6,
        'process_func': process_question_six,
        'processing_technique': CUSTOM_PROCESSING_FUNC
    },
    {
        'string': 'Do you consider yourself as a Data-Scientist?',
        'number': 7,
        'start_index': 60,
        'end_index': 61,
        'replace_str': 'I do neither data science nor machine learning',
        'processing_technique': REPLACE_NA
    },
    {
        'string': 'Which version of Python do you use the most?',
        'number': 8,
        'start_index': 61,
        'end_index': 62,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which version of Python 2 do you use the most?',
        'number': 9,
        'start_index': 62,
        'end_index': 63,
        'processing_technique': DROP_NA
    },

    {
        'string': 'Which version of Python 3 do you use the most?',
        'number': 10,
        'start_index': 63,
        'end_index': 64,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What do you typically use to upgrade your Python version?',
        'number': 11,
        'start_index': 64,
        'end_index': 78,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Do you use any of the following tools to isolate Python environments, if any?',
        'number': 12,
        'start_index': 78,
        'end_index': 84,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What web frameworks / libraries do you use in addition to Python?',
        'number': 13,
        'start_index': 84,
        'end_index': 96,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What data science framework(s) do you use in addition to Python?',
        'number': 14,
        'start_index': 96,
        'end_index': 109,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which of the following frameworks / libraries do you use in addition to Python?',
        'number': 15,
        'start_index': 109,
        'end_index': 124,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which of the following cloud platforms do you use?',
        'number': 16,
        'start_index': 124 ,
        'end_index': 136,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How do you run code in the cloud (in the production environment)?',
        'number': 17,
        'start_index': 136 ,
        'end_index': 142,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How do you develop for the cloud?',
        'number': 18,
        'start_index': 142,
        'end_index': 150,
        'processing_technique': DROP_NA
    },
    {
        'string':'What operating system(s) are your development environment?',
        'number': 19,
        'start_index': 150,
        'end_index': 155,
        'processing_technique': DROP_NA
    },
    {
        'string':'Which Python unit-testing framework(s) do you use, if any?',
        'number': 20,
        'start_index': 155,
        'end_index': 164,
        'processing_technique': DROP_NA
    },
    {
        'string':'What ORM(s) do you use together with Python, if any?',
        'number': 21,
        'start_index': 164,
        'end_index': 173,
        'processing_technique': DROP_NA
    },
    {
        'string':'Which database(s) do you regularly use, if any?',
        'number': 22,
        'start_index': 173,
        'end_index': 189,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which of the following Big Data tool(s) do you use, if any?',
        'number': 23,
        'start_index': 189,
        'end_index': 201,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which Continuous Integration (CI) system(s) do you regularly use?',
        'number': 24,
        'start_index': 201,
        'end_index': 211,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which configuration management tools do you use, if any?',
        'number': 25,
        'start_index': 211,
        'end_index': 218,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What is the main editor you use for your current Python development?',
        'number': 26,
        'start_index':  218,
        'end_index': 219,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which database(s) do you regularly use, if any?',
        'number': 27,
        'start_index': 219,
        'end_index': 245,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Do you regularly work on multiple projects at the same time?',
        'number': 28,
        'start_index': 245,
        'end_index': 246,
        'processing_technique': DROP_NA
    },
    {
        'string': 'When developing in Python, how often do you?',
        'number': 29,
        'start_index': 246,
        'end_index': 261,
        'processing_technique': DROP_NA
    },
    {
        'string': ' How did you first learn about your main IDE/editor?',
        'number': 30,
        'start_index': 261,
        'end_index': 262,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How often do you use your main ide/editor',
        'number': 31,
        'start_index': 262,
        'end_index': 263,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Most of the time, do you ...',
        'number': 32,
        'start_index': 263,
        'end_index': 264,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How many people are in your team',
        'number': 33,
        'start_index': 264,
        'end_index': 265,
        'processing_technique': DROP_NA
    },
    {
        'string': 'What is your employment status?',
        'number': 34,
        'start_index': 265,
        'end_index': 266,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How many people work for your company / organization?',
        'number': 35,
        'start_index': 266,
        'end_index': 267,
        'processing_technique': DROP_NA
    },
      {
        'string': 'Which of the following industries best describes your company\'s business?',
        'number': 36,
        'start_index': 267,
        'end_index': 268,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which of the following industries do you develop for?',
        'number': 37,
        'start_index': 268,
        'end_index': 269,
        'processing_technique': DROP_NA
    },
    {
        'string': 'How long have you been working in the IT industry?',
        'number': 38,
        'start_index': 269,
        'end_index': 270,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Which of the following best describes your job role(s)?',
        'number': 39,
        'start_index': 270,
        'end_index': 282,
        'processing_technique': DROP_NA
    },
    {
        'string': 'Could you tell us your age range?',
        'number': 40,
        'start_index': 282,
        'end_index': 283,
        'processing_technique': BOTH_PYTHON_AND_NON_PYTHON_USERS
    },
    {
        'string': 'What country do you live in?',
        'number': 41,
        'start_index': 283,
        'end_index': 284,
        'processing_technique': BOTH_PYTHON_AND_NON_PYTHON_USERS
    },
]
