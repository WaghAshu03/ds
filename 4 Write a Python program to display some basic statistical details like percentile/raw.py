# Write a Python program to display some basic statistical details like percentile, mean, standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris- versicolor’ of iris.csvdataset.Provide the codes with outputs and explain everything that you do in this step.

import pandas as pd

# Load the dataset
df = pd.read_csv(
    'D:\\Academics\\3rd Year\\Sem 6\\Practicals\\DSBDAL\\IRIS.csv')
df

# Filter data for specific species
setosa_data = df[df['species'] == 'Iris-setosa']
versicolor_data = df[df['species'] == 'Iris-versicolor']
virginica_data = df[df['species'] == 'Iris-virginica']

# Calculate statistical details for each species
setosa_stats = setosa_data.describe()
versicolor_stats = versicolor_data.describe()
virginica_stats = virginica_data.describe()

# Print the statistical details
print("Statistical Details for Iris-setosa:\n")
setosa_stats

print("\nStatistical Details for Iris-versicolor:\n")
versicolor_stats

print("\nStatistical Details for Iris-virginica:\n")
virginica_stats
