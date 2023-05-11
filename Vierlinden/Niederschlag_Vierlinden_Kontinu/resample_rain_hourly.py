import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('vierlinden_niederschlag_kontinuierlich.csv')

# Convert the 'date' column to datetime format
df['Datetime'] = pd.to_datetime(df['Datum'], format = '%d.%m.%Y %H:%M:%S')
df.drop(['Datum'], axis=1, inplace=True)

# Set the 'date' column as the DataFrame's index
df.set_index('Datetime', inplace=True)

# Convert comma separated strings into floats
df['Niederschlag'] = df['Niederschlag'].str.replace(',', '.').astype(float)

# Resample the data by hourly intervals and average out the rain quantity
df_hourly = df.resample('H').mean()

# Save the aggregated data
df_hourly.to_csv('vierlinden_niederschlag_stunden.csv')