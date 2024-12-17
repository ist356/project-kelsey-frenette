import os
import pandas as pd

file_path = "/Users/kelseyfrenette/Desktop/project-kelsey-frenette/Parking_Violations_-_2023_-_Present.xlsx"

if os.path.exists(file_path):
    data = pd.read_excel(file_path)
    print(data.head())
else:
    print(f"File not found: {file_path}")