# FIFA-21 - Data Cleansing - Vidhya Venugopal - 8902970
# Import Packages for data load and clean

import pandas as pd
import numpy as np
import re
from datetime import datetime

# Load the dataset FIFA 21.csv
fifa21_df = pd.read_csv('E:\\Canada\Conestoga College\\Programming in BigData - PROG8420 - 23S - Sec2\\PythonPrograms\\source\\repos\\FIFA 21.csv')

# Validate if the data has been uploaded properly
# Prints number of rows and columns in dataframe
print(fifa21_df.shape)
# Prints the datatypes of all the columns in dataframe
print(fifa21_df.dtypes)
# Prints first n rows of the DataFrame
print(fifa21_df.head(15))
# Prints last n rows of the DataFrame
print(fifa21_df.tail(15))
# Index, Datatype and Memory information
print(fifa21_df.info())

# Task 1 – FIFA 21 Data 
# Q1. Convert the height and weight columns to numerical forms
# Function to convert height from String to Numerical
def convert_height(height):
    if "'" in height:
        height = height.replace('"', '')
        feet, inches = map(int, height.split("'"))
        return ((feet * 12 + inches) * 2.54)
    else:
        return int(height.replace('cm', ''))

# Function to convert weight from String to Numerical
def convert_weight(weight):
    if "lbs" in weight:
        return int(weight.replace('lbs', '')) * 0.453592
    else:
        return int(weight.replace('kg', ''))

# Apply conversion functions to the height and weight columns
fifa21_df['Height'] = fifa21_df['Height'].apply(convert_height)
fifa21_df['Weight'] = fifa21_df['Weight'].apply(convert_weight)

# Q2.Remove the unnecessary newline characters from all columns that have them

fifa21_df = fifa21_df.replace({r'\r|\n': ''}, regex=True)

# Q3.'Value', 'Wage' and "Release Clause' are string columns. Convert them to numbers. For eg, "M" in value column is Million, so multiply the row values by 1,000,000, etc
# Function to convert string representations to numerical values
def convert_to_numeric(value):
    if value[-1] == 'M':
        return float(value[1:-1]) * 1000000  # Convert 'M' to millions
    elif value[-1] == 'K':
        return float(value[1:-1]) * 1000  # Convert 'K' to thousands
    else:
        return float(value[1:])  # Remove the symbol and convert to float

# Apply conversion function to 'Value', 'Wage', and 'Release Clause' columns
fifa21_df['Value'] = fifa21_df['Value'].apply(convert_to_numeric)
fifa21_df['Wage'] = fifa21_df['Wage'].apply(convert_to_numeric)
fifa21_df['Release Clause'] = fifa21_df['Release Clause'].apply(convert_to_numeric)

# Q4.Some columns have 'star' characters. Strip those columns of these stars and make the columns numerical

# Replace '★' and other non-numeric characters with an empty string
fifa21_df['W/F'] = fifa21_df['W/F'].str.replace('[^0-9]', '', regex=True)
fifa21_df['SM'] = fifa21_df['SM'].str.replace('[^0-9]', '', regex=True)
fifa21_df['IR'] = fifa21_df['IR'].str.replace('[^0-9]', '', regex=True)

# Convert the column to numeric, setting errors='coerce' to handle non-convertible values
fifa21_df['W/F'] = pd.to_numeric(fifa21_df['W/F'], errors='coerce')
fifa21_df['SM'] = pd.to_numeric(fifa21_df['SM'], errors='coerce')
fifa21_df['IR'] = pd.to_numeric(fifa21_df['IR'], errors='coerce')

# Q5.Remove further outliers from data and generate a summary report stating all the changes 

# Function to remove outliers using IQR method for a specific column
def check_outliers_iqr_for_column(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Function to convert 'Hits' column to numeric
def convert_hits(hits):
    if isinstance(hits, str):
        if 'K' in hits:
            return float(hits.replace('K', '')) * 1000  # Convert 'K' to thousands
        elif hits == '?':
            return np.nan  # Handle '?' values as NaN or any other appropriate handling
        else:
            return float(hits)
    else:
        return hits  # If already a number or NaN, return as is

# Apply the conversion function to the 'Hits' column
fifa21_df['Hits'] = fifa21_df['Hits'].apply(convert_hits)

# Check outliers for the 'Hit' column
outlier_column = 'Hits'
before_outlier_count = len(fifa21_df)

outliers = check_outliers_iqr_for_column(fifa21_df, outlier_column)

after_outlier_count = len(fifa21_df)

# Further Data cleaning for better visualization
# Clean the Club column to remove redundant characters
# Remove "\n"
fifa21_df.Club = fifa21_df.Club.str.replace('\n\n\n\n', '')
# Remove "1. " from those
fifa21_df.Club = fifa21_df.Club.apply(
    lambda x: pd.Series(re.sub(pattern=r"^\d+\. ", string=x, repl="")))

#TO ENSURE CONSISTENCY IN NAMING, OVA and LongName IS REMANED
fifa21_df = fifa21_df.rename(columns = {'↓OVA': 'OVA'})
fifa21_df = fifa21_df.rename(columns = {'LongName': 'PlayerFullName'})

#Creating Separate Column Called "YearsOfPlaying"
#Based on the 'Joined' column, check which players have been playing at a club for more than 10 years!
fifa21_df['Joined'] = pd.to_datetime(fifa21_df['Joined'], format='%d-%b-%y')

# Calculate years of playing
current_year = datetime.now().year
fifa21_df['YearsOfPlaying'] = current_year - fifa21_df['Joined'].dt.year

# Split the 'Contract' column based on the delimiter (~) and expand it into two separate columns
fifa21_df[['Contract Start Year', 'Contract End Year']] = fifa21_df['Contract'].str.split(' ~ ', expand=True)

# Drop the original 'Contract' column
fifa21_df.drop(columns=['Contract'], inplace=True)

# Display summary of changes
print("Summary of Changes Made to FIFA 21 Dataset:")

# Display sample of changes for each transformation

# Q1 - Convert Height and Weight columns to numerical forms
print("\nSample of Height and Weight Conversion:")
print(fifa21_df[['Height', 'Weight']].head())

# Q2 - Remove unnecessary newline characters
print("\nSample after Removing Newline Characters:")
print(fifa21_df.head())

# Q3 - Convert 'Value', 'Wage', and 'Release Clause' to numbers
print("\nSample after Converting 'Value', 'Wage', and 'Release Clause' Columns:")
print(fifa21_df[['Value', 'Wage', 'Release Clause']].head())

# Q4 - Strip star characters and convert to numeric
print("\nSample after Stripping Star Characters:")
print(fifa21_df[['W/F', 'SM', 'IR']].head())

# Q5 - Remove outliers from the 'Hits' column
print("\nSample after Removing Outliers from 'Hits' Column:")
print(fifa21_df[['Hits']].head())

# Display summary counts of changes
print("\nSummary Counts:")
print("Rows Before Outlier Check:", before_outlier_count)
print("Rows After Outlier Check:", after_outlier_count)
print("Outliers Rows in Hits Column:", outliers[['LongName', 'Hits']])
print("We cannot remove the outliers as its mandatory for the players but corrected the inconsistency by making the column as numeric and converting into appropriate values.")

# Write the modified DataFrame back to a new CSV file
fifa21_df.to_csv('C:/Users/Vidhya Venugopal/Documents/FIFA 21_Updated.csv', index=False)






