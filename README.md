# first_analysis
This is a practice project that performs an analysis of the JBeans developer survey 2018


### Overview

The main aim of this project is to perform some analysis on the raw Dataset of the [JetBeans Raw Dataset](https://drive.google.com/drive/folders/1giaGOhJYWIXfZzy-zxmbrUIOB9Y_ROdu)

Note that this analysis has already been done by JetBeans themselves [here]([JBeans Raw Dataset](https://drive.google.com/drive/folders/1giaGOhJYWIXfZzy-zxmbrUIOB9Y_ROdu)).
However, I am doing this to practice the steps of Data Analysis

### Setup Steps
Here are some the steps to setup this project:
- Install Python 3.6.5 from [here](https://www.python.org/downloads/release/python-365/)
- Install pipenv by running `pip install pipenv`
- Clone the repo via: `git clone https://github.com/chidioguejiofor/first_analysis.git`
- Create a virtual environment via: `pipenv shell`
- Install all the app dependencies via: `pipenv install`

### Raw CSV file name

The application gets the raw csv filename through the following steps:
- Checks for an environmental variable `CSV_FILENAME`
- If it is not found it uses `raw_survey.csv`  as the CSV filename

### Cleaning Data

To clean up data execute: `python cli.py tidy-and-export`.

The above would clean up data and export the clean data to `2018 Tidy Data.xlsx`. 

You can specify the filename that it would export the data to via: `python cli.py tidy-and-export --output_filename [put-your-filename-here]`.

