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

### Configuring cleaning

You can control the way the data would be cleaned by modifying the `export_config.json` file. The following is how you should structure the file:

```
{
  "fillna":[
    {..}
  ],
  "custom_func":[
    {..}
  ],
  "raw_dataset":[..]
}
```


- The `fillna` option takes a list of dictionaries and tells the app questions whose `NaN` values should be
filled with a particular value. The dictionary keys are:
    - number: an int that tells the app the question number
    - replace_str: tells the app the string that should be used to in place of `NaN` values.
    For example,
    ```
    {
        "fillna":[
            { 
                "number":10,
                "replace_str": "This string would be used to replace NaN values for Question 10"
            },
            { 
                "number":11,
                "replace_str": "This string would be used to replace NaN values for Question 11"
            },
            ...
        ]
    }

    ```

- The `custom_func` option takes a list of dictionaries and tells the app to use a custom function to process
a particular question. The dictionary options are :
    - number: an int that tells the app the question number
    - process_func: the function to call once it is done cleaning the data. Note that this function must
      return a `pandas Dataframe` that contains the cleaned question
    For example,
    ```
    {
        ...,
        "custom_func":[
            { 
                "number":10,
                "process_func": "base_module.function_module.question_10_func"
            },
            { 
                "number":11,
                "process_func": "base_module.function_module.question_11_func",
                "args":[ "argument1", "argument2"]
            },
            ...
        ]
    }

    ```
    The app would:
     - call  function `question_10_func` in the module `base_module.function_module` when processing
    `Question 10`.
     - call function called `question_11_func` in the module `base_module.function_module`, with arguments
     `argument1` and `argument2`, when processing `Question 11` .
     
    NB: As you can see the `args` option is optional

