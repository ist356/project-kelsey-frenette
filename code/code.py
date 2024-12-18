import pandas as pd
from io import StringIO
import os
import matplotlib.pyplot as plt


file_path = "cache/Parking Violations 2024.csv"

data = pd.read_csv(file_path, parse_dates=["Date"], low_memory=False) #load the datatset

data.rename(columns={"Amounnt": "Amount"}, inplace=True) # Rename typo in column name
data = data.drop(columns=["X", "Y", "z", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"], errors="ignore") # Drop unnecessary columns

streets_of_interest = ["comstock", "walnut", "marshall", "university"] # Define the streets to search for

data["Location"] = data["Location"].str.strip().str.lower() # Remove leading/trailing whitespaces and convert to lowercase

# Filter data 
start_date = "2024-08-01"
end_date = "2024-12-31"

filtered_data = data[
    (data["Location"].str.contains("|".join(streets_of_interest), na=False)) &
    (data["Date"] >= start_date) & 
    (data["Date"] <= end_date)
]

# Print Filtered Data
print("\nFiltered Data:")
print(filtered_data)

# Aggregate data: total tickets and total fines per location
aggregated_data = filtered_data.groupby("Location").agg(
    Total_Tickets=("Violation", "count"),
    Total_Fines=("Amount", "sum")
).reset_index()

# Print Aggregated Data
print("\nAggregated Data:")
print(aggregated_data)

