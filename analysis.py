# Data Science with Python - Sample Final Project

import kagglehub # kaggle api
import pandas as pd
# STEP 0: WRITE RELEVANT FUNCTIONS 

# check_data_clean ensures that:
#   a. No missing values
#   b. No duplicates
#   c. Data typing is consistent
def check_data_clean(df):
    # a. Check for missing values
    missing_values = df.isnull().sum()
    missing_values_found = False
    for column in df.columns: 
        missing_count = df[column].isnull().sum()
        
        if missing_count > 0:
            missing_values_found = True
            print(f"Missing values in {column}:", {missing_count})
    if not missing_values_found:
        print("No missing values found! :)")

    # b. Cehck for duplicates
    duplicates = df.duplicated().sum()
    if duplicates == 0:
        print("No duplicates found! :)")
    else: 
        print(f"Number of duplicate rows: {duplicates}")
    
    # c. Check data types
    print("Data Types:", df.dtypes)

# count_percent takes in a column containing binary values of the DataFrame and calculates percent true
def count_percent(df, column):
    # Make sure column only contains binary or Boolean values
    '''
    if not set(df[column].unique()).issubset({True, False, 0, 1}):
        raise ValueError(f"The column '{column}' should only contain binary or Boolean values.")
    '''
    # Calculate percent true
    percent_true = (df[column].sum()/len(df))*100
    return percent_true

def convert_yes_no(df, column):
    df[column] = df[column].str.lower().map({'yes': 1, 'no': 0})
    return df
# STEP 1: IMPORT DATA

# If using kagglehub, run pip install kagglehub in terminal

path = kagglehub.dataset_download("jillanisofttech/brain-stroke-dataset")

# print("Path to dataset files:", path) # Check correct path

# Load DataFrame
stroke_df = pd.read_csv(f"{path}/brain_stroke.csv")

# Check DataFrame loaded correctly by printing first five rows
# print(stroke_df.head())


# STEP 2: CLEAN DATA
# check_data_clean(stroke_df)
# Convert ever_married column to 0/1 instead of yes/no
stroke_df = convert_yes_no(stroke_df, 'ever_married')

# STEP 3: DATA MANIPULATION 

# STEP 4: EDA

# print(stroke_df.describe())

percent_never_smoked = (df['smoking_status'].lower().eq('never smoked').mean())*100

print("Percent of respondents with hypertension: ", count_percent(stroke_df, 'hypertension'))
print("Percent of respondents with heart disease: ", count_percent(stroke_df, 'heart_disease'))
print("Percent of respondents that have been married: ", count_percent(stroke_df, 'ever_married'))
print("Percent of respondents that have never smoked: ", percent_never_smoked)
# print("Percent of respondents who smoke", count_percent(stroke_df, 'smoking_status'))