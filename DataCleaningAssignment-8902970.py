import pandas as pd
import numpy as np

#Data Exploration

#a.Load the dataset into your preferred data analysis tool
df = pd.read_csv('E:\\Canada\Conestoga College\\Programming in BigData - PROG8420 - 23S - Sec2\\PythonPrograms\\source\\repos\\Movies.csv')

#b.Checking the dimensions, previewing a few rows, and identifying the data types of each column
# Prints number of rows and columns in dataframe
print(df.shape)
# Prints the datatypes of all the columns in dataframe
print(df.dtypes)
# Prints first n rows of the DataFrame
print(df.head(15))
# Prints last n rows of the DataFrame
print(df.tail(15))
# Index, Datatype and Memory information
print(df.info())

#Handling Missing Values
#a. Identify and print the columns with missing values
col = [col for col in df.columns if df[col].isnull().any()]
print(col)
#b. Evaluate and print the extent of missing values in each column and 
# decide on an appropriate strategy for handling them
# Printing the columns for which the missing percentage is greater than or equal to 20%
for col in df.columns:
        pct_missing = np.mean(df[col].isnull())
        if pct_missing >=0.20:
            print('{} - {}%'.format(col, round(pct_missing*100)))
#c. Implement the chosen strategy and explain your reasoning behind it
# Dropping only those columns which is more than 20% therefore only RunTime & Gross
df_null_clear = df.drop(['RunTime','Gross'], axis=1)
df_null_clear
# Drops all rows that contain null values
df_null_clear = df_null_clear.dropna()
#d. Validate the changes made and ensure that no missing values remain
for col in df_null_clear.columns:
        pct_missing = np.mean(df_null_clear[col].isnull())
        print('{} - {}%'.format(col, round(pct_missing*100)))

#Removing Duplicates

#a. Check for duplicate rows in the dataset
# count number of duplicate rows
num_duplicate_rows = df_null_clear.duplicated().sum()
print("Number of duplicate rows: ", num_duplicate_rows)
#b. If duplicates exist, remove them, and justify your approach.
# remove duplicate rows
df_no_duplicates = df_null_clear.drop_duplicates()
# Print the no of rows and columns just before the remove duplicates and after
print(df_null_clear.shape)
print(df_no_duplicates.shape)
#c. Verify that duplicate rows have been successfully removed
# count number of duplicate rows
num_duplicate_rows = df_no_duplicates.duplicated().sum()
print("Number of duplicate rows After Cleaning: ", num_duplicate_rows)

#Dealing with Inconsistent Data

#a. Identify columns that contain inconsistent or erroneous data
count_special_chars1 = df_no_duplicates['GENRE'].str.count(r'\n')
print("Number of Special Characters: ", count_special_chars1)
#b. Implement necessary corrections to resolve inconsistencies (e.g., standardizing formats, correcting typos)
df_no_duplicates['GENRE'] = df_no_duplicates['GENRE'].str.replace('\n', '',regex=True)
#c. Document the changes made and explain how they improve the data quality.
count_special_chars1 = df_no_duplicates['GENRE'].str.count(r'\n')
print("Number of Special Characters After Cleaning: ", count_special_chars1)

#Handling Outliers
#Identify columns that may contain outliers
print("Checking If there is any Outliers in Rating Column :",np.where(df_no_duplicates['RATING']>10))

#Final Data Validation
#Perform any additional checks or validations that you think are necessary to ensure the overall quality of the dataset
print(df_no_duplicates.describe())
