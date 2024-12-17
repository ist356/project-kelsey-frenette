import pandas as pd
from io import StringIO
import os
import matplotlib.pyplot as plt

file_path = "Parking_Violations_-_2023_-_Present.csv"

# Load the dataset and parse dates
data = pd.read_csv(file_path, parse_dates=["Date"], low_memory=False)

# Clean and normalize column names
data.columns = data.columns.str.strip()
data["Location"] = data["Location"].str.strip().str.lower()

# Fix typo in column name
data.rename(columns={"Amounnt": "Amount"}, inplace=True)

# Define the streets to search for
streets_of_interest = ["comstock", "walnut", "marshall", "university"]

# Filter by streets using partial string match
filtered_by_location = data[data["Location"].str.contains("|".join(streets_of_interest), na=False)]

# Filter by date range
start_date = "2024-08-01"
end_date = "2024-12-31"
filtered_by_date = filtered_by_location[
    (filtered_by_location["Date"] >= start_date) & 
    (filtered_by_location["Date"] <= end_date)
]

# Combine both filters
filtered_data = filtered_by_date

# Check if filtered data is empty
if filtered_data.empty:
    print("No matching data found. Verify street names and date range.")
else:
    print("Filtered Data:")
    print(filtered_data)

    # Aggregate data: total tickets and fines by location
    aggregated_data = filtered_data.groupby("Location").agg(
        Total_Tickets=("Violation", "count"),
        Total_Fines=("Amount", "sum")
    ).reset_index()

    # Display aggregated data
    print("\nAggregated Data:")
    print(aggregated_data)

    # Optionally save results
    filtered_data.to_csv("filtered_parking_violations.csv", index=False)
    aggregated_data.to_csv("aggregated_parking_violations.csv", index=False)