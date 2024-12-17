import os
import pandas as pd

file_path = "/Users/kelseyfrenette/Desktop/project-kelsey-frenette/Parking_Violations_-_2023_-_Present.csv"

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print(data.head())
else:
    print(f"File not found: {file_path}")