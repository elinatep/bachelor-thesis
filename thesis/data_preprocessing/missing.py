import pandas as pd

# Load the dataset
datan = pd.read_csv('/datasets/eteplygina/neg_30.csv')
datap = pd.read_csv('/datasets/eteplygina/pos_30.csv')

# Sort the dataset by patient ID and timestamp
datap.sort_values(by=['id', 'time_rounded'], inplace=True)
datan.sort_values(by=['id', 'time_rounded'], inplace=True)


# Backward-fill any remaining missing values
datap.bfill(inplace=True)
datan.bfill(inplace=True)

# Interpolate any remaining missing values linearly
datap.interpolate(method='linear', inplace=True)
datan.interpolate(method='linear', inplace=True)

# Check if there are any remaining missing values
missing_values_countp = datap.isnull().sum().sum()
missing_values_countn = datan.isnull().sum().sum()
print("Total missing values after handling:", missing_values_countp)
print("Total missing values after handling:", missing_values_countn)

# Save the preprocessed dataset
datan.to_csv('/datasets/eteplygina/labeled_negative_database.csv', index=False)
datap.to_csv('/datasets/eteplygina/labeled_positive_database.csv', index=False)