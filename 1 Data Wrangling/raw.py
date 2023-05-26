# Data Wrangling,
# Perform the following operations using Python on any open source dataset (e.g., data.csv)
# 	1. Import all the required Python Libraries.
#  	2. Locate an open source data from the web (e.g., https://www.kaggle.com). Provide a clear description of the data and its source
# 	3. Load the Dataset into pandas dataframe.
# 	4. Data Preprocessing: check for missing values in the data using pandas isnull(), describe() function to get some initial statistics. Provide variable 		descriptions. Types of variables etc. Check the dimensions of the data frame.
# 	5. Data Formatting and Data Normalization: Summarize the types of variables by checking the data types (i.e., character, numeric, integer, factor, and 		logical) of the variables in the data set. If variables are not in the correct data type, apply proper type conversions.
# 	6. Turn categorical variables into quantitative variables in Python. In addition to the codes and outputs, explain every operation that you do in the 		above steps and explain everything that you do to import/read/scrape the data set. (make me understand every statement)


# 1
import pandas as pd
import numpy as np

# 2, 3
df = pd.read_csv(
    'D:\\Academics\\3rd Year\\Sem 6\\Practicals\\DSBDAL\\1\\IRIS.csv')

# 4
# Check for missing values
print(df.isnull().sum())

# Get initial statistics
print(df.describe())

# Check dimensions of the DataFrame
print(df.shape)

print(df.info())

# 5
print(df.dtypes)
df['sepal_length'] = df['sepal_length'].astype(int)
print(df)

# 6
df_encoded = pd.get_dummies(df, columns=['petal_length'])
print(df_encoded)
