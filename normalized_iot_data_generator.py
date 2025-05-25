import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os

# Define the base directory
base_dir = 'C:/Users/presc/Downloads/dataset'

# Construct file paths
file_path = os.path.join(base_dir, 'Beach_Weather_Stations_-_Automated_Sensors.csv')
device_data_file_path = os.path.join(base_dir, 'device_data_packets1.csv')

# Load the datasets
beach_weather_df = pd.read_csv(file_path)
device_data_packets_df = pd.read_csv(device_data_file_path)

# Select the relevant columns from the beach weather data
selected_columns = ['Air Temperature', 'Wind Speed']  # Adjust this based on your requirements
beach_weather_selected_df = beach_weather_df[selected_columns]

# Normalize the selected columns to match the range of the 'Data' column in device_data_packets1.csv
device_data_values = device_data_packets_df['Data'].values.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(device_data_values.min(), device_data_values.max()))

# Normalize the beach weather data
normalized_beach_weather_df = pd.DataFrame(
    scaler.fit_transform(beach_weather_selected_df),
    columns=selected_columns
)

# Function to create the dataset in the desired format with Device labels similar to 'A' or 'T'
def create_specific_dataset(df, num_nodes, label):
    # Randomly sample the specified number of nodes
    sampled_df = df.sample(n=num_nodes, random_state=42)
    
    # Convert to the format 'Data, Device'
    formatted_data = []
    for index, row in sampled_df.iterrows():
        for col in selected_columns:
            formatted_data.append({'Data': row[col], 'Device': label})
    
    return formatted_data

# Create datasets for 25, 50, 75, and 100 nodes with appropriate labels
# Here, we'll alternate between 'A' and 'T' for simplicity
dataset_25_nodes_specific = create_specific_dataset(normalized_beach_weather_df, 25, 'A')
dataset_50_nodes_specific = create_specific_dataset(normalized_beach_weather_df, 50, 'A')
dataset_75_nodes_specific = create_specific_dataset(normalized_beach_weather_df, 75, 'T')
dataset_100_nodes_specific = create_specific_dataset(normalized_beach_weather_df, 100, 'A')

# Convert to DataFrame for easier saving to CSV
dataset_25_nodes_specific_df = pd.DataFrame(dataset_25_nodes_specific)
dataset_50_nodes_specific_df = pd.DataFrame(dataset_50_nodes_specific)
dataset_75_nodes_specific_df = pd.DataFrame(dataset_75_nodes_specific)
dataset_100_nodes_specific_df = pd.DataFrame(dataset_100_nodes_specific)

# Save the datasets to CSV files
dataset_25_nodes_specific_df.to_csv(os.path.join(base_dir, 'device_data_packets_25_nodes_specific.csv'), index=False)
dataset_50_nodes_specific_df.to_csv(os.path.join(base_dir, 'device_data_packets_50_nodes_specific.csv'), index=False)
dataset_75_nodes_specific_df.to_csv(os.path.join(base_dir, 'device_data_packets_75_nodes_specific.csv'), index=False)
dataset_100_nodes_specific_df.to_csv(os.path.join(base_dir, 'device_data_packets_100_nodes_specific.csv'), index=False)

# Display the first few rows of the new datasets to confirm
dataset_25_nodes_specific_df.head(), dataset_50_nodes_specific_df.head(), dataset_75_nodes_specific_df.head(), dataset_100_nodes_specific_df.head()
