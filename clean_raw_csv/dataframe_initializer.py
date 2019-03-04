import pandas as pd
import numpy as np


class DataframeInitializer:

    raw_data_df = None
    python_observations_df = None
    non_python_observations_df = None

    @classmethod
    def initialise_dataframes(cls):
        from .constants import CSV_FILENAME, NOT_PYTHON_STR
        cls.raw_data_df = pd.read_csv(CSV_FILENAME, dtype=np.object)

        # extracting the observations into two dataframes
        cls.non_python_observations_df = cls.raw_data_df[cls.raw_data_df.iloc[:, 1] == NOT_PYTHON_STR]
        cls.python_observations_df = cls.raw_data_df[cls.raw_data_df.iloc[:, 1] != NOT_PYTHON_STR]

