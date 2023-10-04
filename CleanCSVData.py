import pandas as pd
import numpy as np

df = pd.read_csv('E:\\Canada\Conestoga College\\Programming in BigData - PROG8420 - 23S - Sec2\\PythonPrograms\\source\\repos\\train.csv')

print(df.shape)
print(df.dtypes)

df_numeric = df.select_dtypes(include=np.number)
numeric_cols = df_numeric.columns.values
# select only numeric rows
print(numeric_cols)

#No of rows of the data frames
print(len(df))

#No of columns of the data frames
print(len(df.columns))

cols = df.columns
print(cols)
#Print the Name of all the columns
print(df.head())

#Check for null and not NA
df.isnull().any()

#print the column names with the missing values

col = [col for col in df.columns if df[col].isnull().any()]
print(col)

#count of missing values in each col
sum = df.isna().sum()
print(sum)

#percentage of missing values for each of the columns
for col in df.columns:
        pct_missing = np.mean(df[col].isnull())
        if pct_missing >=0.20:
            print('{} - {}%'.format(col, round(pct_missing*100)))

# sum of null values

print(df.isnull().values.sum())

# drop missing na values
df.dropna()

# remove all columns with atleast one null value

columns_with_na_dropped = df.dropna(axis=1)
columns_with_na_dropped

# how many columns did we loose

print("Columns in original dataset: %d \n" % df.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# Replace 0 with NAs

#df.fillna()

# available in particular column

df['product_type'].describe()

#value counts

df['product_type'].value_counts()

#Identify the duplicates and drop it

# we know that column 'id' is unique, but what if we drop it?
df_dedupped = df.drop('id', axis=1).drop_duplicates()

# there were duplicate rows
print(df.shape)
print(df_dedupped.shape)

# drop duplicates based on an subset of variables.

key = ['timestamp', 'full_sq', 'life_sq', 'floor', 'build_year', 'num_room', 'price_doc']
df_dedupped2 = df.drop_duplicates(subset=key)

print(df.shape)
print(df_dedupped2.shape)

#Capitalization
df['sub_area'].head()

#count occurence of each value

df['sub_area'].value_counts(dropna=False)

# make everything lower case.
df['sub_area_lower'] = df['sub_area'].str.lower()
df['sub_area_lower'].value_counts(dropna=False)

# no address column in the housing dataset. So create one to show the code.
df_add_ex = pd.DataFrame(['   test','test','123 MAIN St Apartment 15', '123 Main Street Apt 12   ', '543 FirSt Av', '  876 FIRst Ave.'], columns=['address'])
df_add_ex

df_add_ex['address_std'] = df_add_ex['address'].str.lower()
df_add_ex['address_std'] = df_add_ex['address_std'].str.strip() # remove leading and trailing whitespace.
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('.', '') # remove period.
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('street', 'st') # replace street with st.
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('apartment', 'apt') # replace apartment with apt.
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('av\\b', 'ave',regex=True) # replace avenue with ave.

df_add_ex