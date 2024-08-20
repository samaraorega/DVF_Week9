#Handling missing data
#You can either drop the column,remove the missing values or replace the null values


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('titanic.csv')
df.head()

#Checking for missing data
df.info()  #This gives us various information about the columns

#Checking for duplicates since .info() might not capture anomalies
duplicates = df[df.duplicated()]
print(len(duplicates))
duplicates.head()

#Checking for extraneous values
for col in df.columns:
    print(col, '\n', df[col].value_counts(normalize=True).head(), '\n\n')

#This prints out the sum of null values in all columns of the data set
df.isna().sum()

#This replaces the null values in a particular column
df['column'].fillna('Other', inplace=True)

#Drops/removes a particular column
df['column'].drop()
