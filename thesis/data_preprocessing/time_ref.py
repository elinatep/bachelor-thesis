import pandas as pd

# Load the dataset
dataset_pathn = '/datasets/eteplygina/labeled_negative_database.csv'
datan = pd.read_csv(dataset_pathn)
dataset_pathp = '/datasets/eteplygina/labeled_positive_database.csv'
datap = pd.read_csv(dataset_pathp)

print("Original datan:")
print(datan.head())
print("\nOriginal datap:")
print(datap.head())

# Convert time columns to datetime objects
datan['time_rounded'] = pd.to_datetime(datan['time_rounded'])
datap['shock_time'] = pd.to_datetime(datap['shock_time'])
datap['time_rounded'] = pd.to_datetime(datap['time_rounded'])

print("\nAfter converting time columns:")
print("datan['time_rounded']:\n", datan['time_rounded'].head())
print("\ndatap['shock_time']:\n", datap['shock_time'].head())
print("\ndatap['time_rounded']:\n", datap['time_rounded'].head())



datan['relative_time'] = (datan['time_rounded'] - datan.groupby('id')['time_rounded'].transform('min')).dt.total_seconds() / 3600


datap['relative_time'] = (datap['shock_time'] - datap['time_rounded']).dt.total_seconds() / 3600


print("\nAfter calculating relative time:")
print("datan['relative_time']:\n", datan['relative_time'].head())
print("\ndatap['relative_time']:\n", datap['relative_time'].head())


# Reorder the columns to place 'relative_time' after 'time'
column_ordern = ['id','weight', 'height', 'age', 'gender', 'ethnicity', 'time_rounded', 'relative_time', 'heartrate', 'sbp', 'dbp', 'mbp', 'respiration', 'temperature', 'spo2', 'label']
datan = datan[column_ordern]
column_orderp = ['id','weight', 'height', 'age', 'gender', 'ethnicity', 'shock_time', 'time_rounded', 'relative_time', 'heartrate', 'sbp', 'dbp', 'mbp', 'respiration', 'temperature', 'spo2', 'label']
datap = datap[column_orderp]

print("\nAfter reordering columns:")
print("datan:\n", datan.head())
print("\ndatap:\n", datap.head())

# Save the updated dataset
datan.to_csv('/datasets/eteplygina/labeled_negative_database.csv', index=False)
datap.to_csv('/datasets/eteplygina/labeled_positive_database.csv', index=False)
