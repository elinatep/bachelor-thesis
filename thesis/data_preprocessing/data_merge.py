import pandas as pd
import os

# Function to merge patient data with vital signs data from a single CSV
def merge_vital_signs(patient_row, vital_df):
    # Merge patient data with vital signs data based on stay_id
    merged_df = pd.merge(patient_row.to_frame().T, vital_df, on='id', how='outer')
    
    return merged_df

# Define the paths
positive_patients_path = '/datasets/eteplygina/positive.csv'
negative_patients_path = '/datasets/eteplygina/negative.csv'
vital_signs_dir = '/Users/elina/Desktop/mimic_kih7jlb3'

# Read patient data from TXT files
positive_patients_df = pd.read_csv(positive_patients_path)
negative_patients_df = pd.read_csv(negative_patients_path)

# List to store merged dataframes for positive and negative patients
positive_merged_dfs = []
negative_merged_dfs = []

# Iterate through each row in the positive patients data
for index, patient_row in positive_patients_df.iterrows():
    stay_id = patient_row['id']
    csv_filename = f"{stay_id}_vitals.csv"
    csv_path = os.path.join(vital_signs_dir, csv_filename)
    
    # Check if the corresponding CSV file exists
    if os.path.exists(csv_path):
        vital_df = pd.read_csv(csv_path)
        positive_merged_df = merge_vital_signs(patient_row, vital_df)
        positive_merged_dfs.append(positive_merged_df)
    else:
        print(f"No CSV file found for stay_id {stay_id}. Skipping...")

# Iterate through each row in the negative patients data
for index, patient_row in negative_patients_df.iterrows():
    stay_id = patient_row['id']
    csv_filename = f"{stay_id}_vitals.csv"
    csv_path = os.path.join(vital_signs_dir, csv_filename)
    
    # Check if the corresponding CSV file exists
    if os.path.exists(csv_path):
        vital_df = pd.read_csv(csv_path)
        negative_merged_df = merge_vital_signs(patient_row, vital_df)
        negative_merged_dfs.append(negative_merged_df)
    else:
        print(f"No CSV file found for stay_id {stay_id}. Skipping...")

# Concatenate all merged dataframes for positive and negative patients
final_positive_merged_df = pd.concat(positive_merged_dfs, ignore_index=True)
final_negative_merged_df = pd.concat(negative_merged_dfs, ignore_index=True)

# Save merged dataframes to files
final_positive_merged_df.to_csv('/datasets/eteplygina/positive_merged_data.csv', index=False)
final_negative_merged_df.to_csv('/datasets/eteplygina/negative_merged_data.csv', index=False)

# Now you have saved merged dataframes for positive and negative patients to CSV files
