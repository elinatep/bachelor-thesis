import pandas as pd

# Read the data from the CSV files
pos_data = pd.read_csv('/datasets/eteplygina/labeled_positive_database.csv')
neg_data = pd.read_csv('/datasets/eteplygina/labeled_negative_database.csv')

# Convert 'time_rounded' column to datetime format
pos_data['time_rounded'] = pd.to_datetime(pos_data['time_rounded'])
neg_data['time_rounded'] = pd.to_datetime(neg_data['time_rounded'])

# Ensure data is sorted by 'id' and 'time_rounded'
pos_data = pos_data.sort_values(by=['id', 'time_rounded'])
neg_data = neg_data.sort_values(by=['id', 'time_rounded'])

# Ensure 'id' column remains as integer
pos_data['id'] = pos_data['id'].astype(int)
neg_data['id'] = neg_data['id'].astype(int)

def resample_patient_data(df, recalculate_relative_time=False):
    all_patients = []
    for patient_id in df['id'].unique():
        patient_data = df[df['id'] == patient_id].copy()
        start_time = patient_data['time_rounded'].min()
        end_time = patient_data['time_rounded'].max()
        complete_time_index = pd.date_range(start=start_time, end=end_time, freq='30T')
        complete_time_df = pd.DataFrame({'time_rounded': complete_time_index})
        patient_complete = pd.merge(complete_time_df, patient_data, on='time_rounded', how='left')
        patient_complete.ffill(inplace=True)
        
        if recalculate_relative_time:
            patient_complete['relative_time'] = (patient_complete['time_rounded'] - patient_complete['time_rounded'].min()).dt.total_seconds() / 3600.0  # relative time in hours
        
        all_patients.append(patient_complete)
    return pd.concat(all_patients, ignore_index=True)

# Resample positive patients' data without recalculating relative_time
resampled_pos_data = resample_patient_data(pos_data, recalculate_relative_time=False)

# Resample negative patients' data and recalculate relative_time
resampled_neg_data = resample_patient_data(neg_data, recalculate_relative_time=True)

# Reorder columns
vitals_columns = ['heartrate', 'sbp', 'dbp', 'mbp', 'respiration', 'temperature', 'spo2']
columns_order = ['id', 'weight', 'height', 'age', 'time_rounded', 'relative_time', 'ethnicity', 'gender', 'shock_time', 'label'] + vitals_columns
columns_ordern = ['id', 'weight', 'height', 'age', 'time_rounded', 'relative_time', 'ethnicity', 'gender', 'label'] + vitals_columns

resampled_pos_data = resampled_pos_data[columns_order]
resampled_neg_data = resampled_neg_data[columns_ordern]

# Set 'id' and 'label' columns to integer type
resampled_pos_data['id'] = resampled_pos_data['id'].astype(int)
resampled_pos_data['label'] = resampled_pos_data['label'].astype(int)
resampled_neg_data['id'] = resampled_neg_data['id'].astype(int)
resampled_neg_data['label'] = resampled_neg_data['label'].astype(int)

# Save the resampled dataset to a new CSV file
resampled_pos_data.to_csv('/datasets/eteplygina/pos_301.csv', index=False)
resampled_neg_data.to_csv('/datasets/eteplygina/neg_301.csv', index=False)

# Display the resampled dataset
print(resampled_pos_data)
print(resampled_neg_data)
