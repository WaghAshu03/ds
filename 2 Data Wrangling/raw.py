# Data Wrangling
# Create an “Academic performance” dataset of students and perform the following operations using Python.
# 1.	Scan all variables for missing values and inconsistencies. If there are missing values and/or inconsistencies, use any of the suitable techniques to deal withthem.
# 2.	Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques to deal withthem.
# 3.	Apply data transformations on at least one of the variables. The purpose of this transformation should be one of the following reasons: to change the scale for better understanding of the variable, to convert a non-linear relation into a linear one, or to decrease the skewness and convert the distribution into a normaldistribution.
# Reason and document your approach properly.

import pandas as pd
import numpy as np

df = pd.read_csv(
    'D:\\Academics\\3rd Year\\Sem 6\\Practicals\\DSBDAL\\2 Data Wrangling\\StudentsPerformance.csv')
df

# 1. Handling Missing Values and Inconsistencies
# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

df['math score'].fillna(df['math score'].mean(), inplace=True)
df


# 2. Dealing with Outliers
# Define the lower and upper quantile thresholds (e.g., 5% and 95%)
lower_threshold = df['reading score'].quantile(0.05)
upper_threshold = df['reading score'].quantile(0.95)

# Identify outliers
outliers = (df['reading score'] < lower_threshold) | (
    df['reading score'] > upper_threshold)

# Replace outliers with nearest valid values within the threshold range
df.loc[outliers, 'reading score'] = df['reading score'].clip(
    lower_threshold, upper_threshold)

# Print the updated dataset
print("Updated Dataset:\n")
df.head()


# 3. Data Transformations
# Apply logarithmic transformation on 'math score' variable for more symmetrical or normal distribution skewness
# np.log() calculates the natural logarithm (base e) of a given value
df['Log math score'] = np.log(df['math score'])
df
