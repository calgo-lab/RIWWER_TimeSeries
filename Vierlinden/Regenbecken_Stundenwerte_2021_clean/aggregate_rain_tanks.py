import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('Füllstand_RRB.csv')

# Concatenate date + time and drop right boundary of time interval
df['Datetime'] = pd.to_datetime(df['Datum'] + " " + df["Zeit"].str[:5])
df.drop(['Datum', 'Zeit', 'Min', 'Max'], axis=1, inplace=True)

# Rename values column to keep track of where it came from
df.rename(columns = {'Wert': 'Füllstand_RRB'}, inplace = True)

# Iterate over the other rain tanks and append their values to the aggregated dataframe
for i, tank in enumerate(['Entleerung_RüB.csv', 'Füllstand_RüB_1.csv', 'Füllstand_RüB_2.csv', 'Füllstand_RüB_3.csv']):
    df_new = pd.read_csv(tank)

    # Append new values from current tank
    df = df.join(df_new['Wert'])
    df.rename(columns={'Wert': tank.split('.')[0]}, inplace = True)

# Set the 'date' column as the DataFrame's index
df.set_index('Datetime', inplace=True)

# Save the aggregated data
df.to_csv('Rain_Tanks.csv')