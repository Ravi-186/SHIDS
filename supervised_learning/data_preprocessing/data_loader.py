# data_preprocessing/data_loader.py

import os
import pandas as pd

def load_data():
    """
    Loads data from CSV files in the 'data/raw/' directory.

    Returns:
    - df: DataFrame containing the concatenated data.
    """

    # Correct path to dataset folder
    data_path = '../data/raw'

    # Check if path exists (good practice)
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset folder not found: {data_path}")

    # List all CSV files
    file_list = [f for f in os.listdir(data_path) if f.endswith('.csv')]

    if not file_list:
        raise ValueError("No CSV files found in dataset folder!")

    # Read and combine all CSV files
    dfs = [pd.read_csv(os.path.join(data_path, file)) for file in file_list]

    df = pd.concat(dfs, ignore_index=True)

    return df