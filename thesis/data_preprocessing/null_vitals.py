import pandas as pd

# Read merged data from CSV files
positive_merged_data = pd.read_csv('/datasets/eteplygina/positive_merged_data.csv')
negative_merged_data = pd.read_csv('/datasets/eteplygina/negative_merged_data.csv')



# Drop the 'Unnamed' column from positive_merged_data.csv

positive_merged_data = positive_merged_data.loc[:, ~positive_merged_data.columns.str.contains('^Unnamed')]


# Drop the 'Unnamed' column from negative_merged_data.csv

negative_merged_data = negative_merged_data.loc[:, ~negative_merged_data.columns.str.contains('^Unnamed')]



# Check if at least one vital sign column is completely null for each positive patient ID
positive_empty_vitals = positive_merged_data.groupby('id').apply(lambda x: x.iloc[:, 15:].isnull().all(axis=0).any())

# Check if at least one vital sign column is completely null for each negative patient ID
negative_empty_vitals = negative_merged_data.groupby('id').apply(lambda x: x.iloc[:, 15:].isnull().all(axis=0).any())

# Filter positive patients with complete vital signs
filtered_positive_data = positive_merged_data[~positive_merged_data['id'].isin(positive_empty_vitals[positive_empty_vitals].index)]

# Filter negative patients with complete vital signs
filtered_negative_data = negative_merged_data[~negative_merged_data['id'].isin(negative_empty_vitals[negative_empty_vitals].index)]

# Save filtered data to new CSV files
filtered_positive_data.to_csv('/datasets/eteplygina/filtered_positive_data.csv', index=False)
filtered_negative_data.to_csv('/datasets/eteplygina/filtered_negative_data.csv', index=False)

