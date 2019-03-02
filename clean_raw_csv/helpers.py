import pandas as pd
import math
from .constants import PYTHON_OBSERVATIONS_DF,  RAW_DATA_DATA_FRAME

def reshape_data(start_index, end_index, question_asked, only_python_observation=True, var_name='question', value_name='answer_chosen', fillna_with_str='',
                 dropna=True):

    """Tidies up a subset dataframe specified by start_index and end_index

   If the python_observation is True it cleans up a subset of the PYTHON_OBSERVATIONS_DF
   constant which contains all the survey information about python users

   When dropna is set to False, the function fills all NaN values with the fillna_with_str string
   else it drops all NaN values

    Args:
        question_asked (str): string representing the question that was asked
        var_name: string representing the column name of the resulting table
        value_name: string representing the name of the column that contains the data
        only_python_observation: The processing is done on only observations where the user is a
        python developer else it is done on all observations
        fillna_with_str: the string that would be used to fill NaN values when dropna is False
        dropna:  if truthy then NaN values would be dropped else Nan values would be replaced by fillna_with_str

    Returns:
        A single column dataframe that contains the title question and the answers that the users
        chose as values
    """

    dataframe = PYTHON_OBSERVATIONS_DF.iloc[:, start_index:end_index]
    if not only_python_observation:
        dataframe = RAW_DATA_DATA_FRAME.iloc[:, start_index:end_index]

    melted_observations = pd.melt(dataframe, var_name=var_name, value_name=value_name)

    if dropna:
        melted_observations = melted_observations.dropna()
    else:
        melted_observations = melted_observations.fillna(fillna_with_str)

    lamda_func = lambda row: question_asked

    melted_observations[var_name] = melted_observations.apply(lamda_func, axis=1)

    pivoted_data = melted_observations.pivot(columns=var_name, values=value_name)
    return pivoted_data


def replace_nans_in_question_six(row):
    """Replaces the nan values in question 6

    Replaces the nan values in the column 'What do you use Python for the most?'
    with the answer to the question 'What do you use Python for?'

    """
    users_most_python_use_case = row[-1]
    if isinstance(users_most_python_use_case, float) and math.isnan(users_most_python_use_case):
        primary_use_case = next(item for item in row.values if isinstance(item, str))
        row[-1] = primary_use_case

    return row


def process_question_six():
    from .constants import PYTHON_OBSERVATIONS_DF
    question_six = {
        'string': 'What do you use Python for the most?',
        'number': 6,
        'start_index': 59,
        'end_index': 60
    }

    question_six_df = PYTHON_OBSERVATIONS_DF.iloc[:, [59]]
    question_four_df = PYTHON_OBSERVATIONS_DF.iloc[:, 27:43]
    question_six_df = pd.merge(question_four_df, question_six, left_index=True, right_index=True)

    question_six_with_no_nans = question_six.apply(replace_nans_in_question_six, axis=1)
    question_six_with_no_nans.iloc[:, -1].value_counts(dropna=False)

    return question_six_with_no_nans.iloc[:, [-1]]

