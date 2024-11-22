import pandas as pd

# Read the data from the text file into a DataFrame and filter entries
file_path = '/datasets/eteplygina/0labels_septicshock'
df = pd.read_table(file_path, sep=',', 
                   converters={'sepsis_to_shock': lambda x: pd.to_timedelta(x) if x != '-1' else pd.NA,
                               'time_to_shock': lambda x: pd.to_timedelta(x) if x != '-1' else pd.NA})

# Filter entries where sepsis is false and bolus is false
negative_patients = df[(df['sepsis'] == False) & (df['bolus'] == False)]

# Write filtered entries to a new text file
output_file = '/datasets/eteplygina/negative.csv'
negative_patients.to_csv(output_file, sep=',', index=False)

df = df[(df['sepsis'] == True) & 
        (df['bolus'] == True) & 
        (~df['sepsis_to_shock'].isna()) &
        (~df['time_to_shock'].isna()) &
        (df['time_to_shock'] > pd.Timedelta(hours=4)) & 
        (df['time_to_shock'] < pd.Timedelta(days=7))]

# Write filtered entries to exclusion.txt
df.to_csv('/datasets/eteplygina/positive.csv', sep=',', index=False)
