import pandas as pd
import numpy as np

# Load the Titanic Machine Learning from Disaster data set to data frame
df = pd.read_csv('E:\\Canada\Conestoga College\\Programming in BigData - PROG8420 - 23S - Sec2\\PythonPrograms\\source\\repos\\Titanic_Machine Learning from Disaster.csv')

# Print the shape and the data types of the data frame
print(df.shape)
print(df.dtypes)

# Return the first n rows from the data frames
pd.set_option('display.max_columns', None)
print(df.head(5))

# Identify the total number of missing values in each column
print(df.isna().sum())

# Determine the % of missing values in Age Column.
pct_missing = np.mean(df['Age'].isnull())
if pct_missing >=0.0:
    print('{} - {}%'.format('Before Replacement Strategy Age', round(pct_missing*100)))

#replace NaN values in 'Age' column with 'unknown'
df.Age = df.Age.fillna(0)

#Check the % of missing values again after replacement
pct_missing = np.mean(df['Age'].isnull())
if pct_missing >=0.0:
    print('{} - {}%'.format('After Replacement Strategy Age', round(pct_missing*100)))

#replace NaN values in 'Cabin' column with 'Unknown'
df.Cabin = df.Cabin.fillna('Unknown')
print(df["Cabin"])

# Determine the % of missing values in Embarked Column.
print('Total No Of Missing Values in Embarked Column - Before Removal : ',df['Embarked'].isna().sum())

# Remove the rows which has missing values in Embarked column
df.dropna(subset=['Embarked'], inplace=True)

# Determine the % of missing values in Embarked Column.
print('Total No Of Missing Values in Embarked Column - After Removal  : ',df['Embarked'].isna().sum())

# Print the shape and the data types of the Sex column
print('Shape of the Sex Column',df['Sex'].shape)
print('Data type of the Sex Column',df['Sex'].dtypes)

# Print the unique values of the Sex column
print('Unique values of the Sex Column',df['Sex'].unique())

# Check if Fare column data type if it is stored as numeric or string
print('Is Fare Column Numeric :', df['Fare'].dtypes)

# Group the "Age" column into bins (e.g., 0-9, 10-19, 20-29, etc.) and create a new column called "AgeGroup" to store the bin labels
# Bin the Age column into 3 equal-sized bins
bins= [1,2,4,13,20,80]
labels = ['Infant','Toddler','Kid','Teen','Adult']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Return the first n rows from the data frames
pd.set_option('display.max_columns', None)
print(df.head(25))
