import pandas as pd

# Load the database into a DataFrame
df = pd.read_csv('/datasets/eteplygina/filtered_positive_data.csv')

# # Convert relevant columns to datetime objects
# df['shock_time'] = pd.to_datetime(df['shock_time'])
# df['time'] = pd.to_datetime(df['time'])

# # Define the time window (e.g., 4 hours before sepsis_time to 4 hours after shock_time)
# window_start = df['shock_time'] - pd.Timedelta(hours=4)
# window_end = df['shock_time'] + pd.Timedelta(hours=4)

# Add a new column for labels and initialize with 0
df['label'] = 1

# # Assign labels based on the time window
# for i, row in df.iterrows():
#     if row['time'] >= window_start[i] and row['time'] <= window_end[i]:
#         df.at[i, 'label'] = 1

# Save the updated DataFrame to a new database file
df.to_csv('/datasets/eteplygina/labeled_positive_database.csv', index=False)


# Load the negative database into a DataFrame
negative_df = pd.read_csv('/datasets/eteplygina/filtered_negative_data.csv')

# Add a new column to represent the labels and assign 0 to all rows
negative_df['label'] = 0

# Save the DataFrame with labels to a new file
negative_df.to_csv('/datasets/eteplygina/labeled_negative_database.csv', index=False)
