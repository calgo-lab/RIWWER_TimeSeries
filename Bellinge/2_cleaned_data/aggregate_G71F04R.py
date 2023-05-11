import pandas as pd

# Read the dataset into a DataFrame
df_L1_i3 = pd.read_csv('G71F04R_Level1_iFixp3_proc_v6.csv')
df_L1_i4 = pd.read_csv('G71F04R_Level1_iFixp4_proc_v6.csv')#[:9769] # cut off first sensor so that it has as many entries as the second one
df_L2_i3 = pd.read_csv('G71F04R_Level2_iFixp3_proc_v6.csv')
df_L2_i4 = pd.read_csv('G71F04R_Level2_iFixp4_proc_v6.csv')

# Only keep time, sensor value and water level (as target)
for df in [df_L2_i3]: #, df_L1_i4, df_L2_i3, df_L2_i4]:
    df.drop(columns=df.columns[0], axis=1, inplace=True) # the '<anonymous> column
    df.drop(['value_no_errors', 'man_remove', 'ffill', 'stamp', 'outbound', 'frozen', 'outlier', 'depth_s'],
            axis=1, inplace=True)

    # Set the 'date' column as the DataFrame's index
    df.rename(columns={'time': 'Datetime'}, inplace=True)
    df.set_index('Datetime', inplace=True)

    df.to_csv('G71F04R_Level2_iFixp3_proc_v6_short.csv')

# Aggregate Level 1 and Level 2 (10 hours are missing...)


# Save the new data
#df_L2_i3.to_csv('G71F04R_Level2_iFixp3_proc_v6_short.csv')