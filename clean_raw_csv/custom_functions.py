import pandas as pd

from .dataframe_initializer import DataframeInitializer
from .helpers import replace_nans_in_question_six


def process_question_six():
    """Processes question six

    The processing of Question 6 does not follow the normal conventions. This function
    is used to process question six ( 'What do you use Python for the most?').

    All NaN values in this question are filled with the answer in question 4 when
    only one option was chosen


    Returns:
        (pandas.Dataframe): A dataframe containing tidy question 6 replies data
    """

    question_six_df = DataframeInitializer.python_observations_df.iloc[:, [58]]
    question_four_df = DataframeInitializer.python_observations_df.iloc[:, 26:42]
    question_six_df = pd.merge(question_four_df, question_six_df, left_index=True, right_index=True)

    question_six_with_no_nans = question_six_df.apply(replace_nans_in_question_six, axis=1)

    return question_six_with_no_nans.iloc[:, [-1]]
