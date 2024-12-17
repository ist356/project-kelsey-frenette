import pandas as pd

def test_filter_by_location():
    # Mock dataset
    data = pd.DataFrame({
        "Location": ["100 comstock ave", "200 walnut ave", "300 main st"],
        "Date": pd.to_datetime(["2024-08-01", "2024-08-05", "2024-09-01"]),
        "Violation": ["Parking", "Speeding", "Parking"],
        "Amount": [60, 100, 40]
    })
    
    streets_of_interest = ["comstock", "walnut"]
    
    # Apply filtering
    filtered = data[data["Location"].str.contains("|".join(streets_of_interest), na=False)]
    
    # Assertions
    assert len(filtered) == 2, "Should only include rows with 'comstock' or 'walnut' in 'Location'"
    assert "100 comstock ave" in filtered["Location"].values
    assert "200 walnut ave" in filtered["Location"].values

def test_filter_by_date():
    # Mock dataset
    data = pd.DataFrame({
        "Location": ["100 comstock ave", "200 walnut ave", "300 main st"],
        "Date": pd.to_datetime(["2024-07-31", "2024-08-01", "2024-12-31"]),
        "Violation": ["Parking", "Speeding", "Parking"],
        "Amount": [60, 100, 40]
    }
    )
    start_date = "2024-08-01"
    end_date = "2024-12-31"
    
    # Apply filtering
    filtered = data[
        (data["Date"] >= start_date) & 
        (data["Date"] <= end_date)
    ]
    
    # Assertions
    assert len(filtered) == 2, "Should only include rows within the specified date range"
    assert "2024-07-31" not in filtered["Date"].astype(str).values
    assert "2024-08-01" in filtered["Date"].astype(str).values
    assert "2024-12-31" in filtered["Date"].astype(str).values

def test_aggregate_data():
    # Mock filtered dataset
    filtered_data = pd.DataFrame({
        "Location": ["100 comstock ave", "100 comstock ave", "200 walnut ave"],
        "Violation": ["Parking", "Speeding", "Parking"],
        "Amount": [60, 100, 40]
    })
    
    # Apply aggregation
    aggregated = filtered_data.groupby("Location").agg(
        Total_Tickets=("Violation", "count"),
        Total_Fines=("Amount", "sum")
    ).reset_index()
    
    # Assertions
    assert len(aggregated) == 2, "Should group by unique locations"
    assert aggregated.loc[aggregated["Location"] == "100 comstock ave", "Total_Tickets"].iloc[0] == 2, \
        "Total tickets for '100 comstock ave' should be 2"
    assert aggregated.loc[aggregated["Location"] == "100 comstock ave", "Total_Fines"].iloc[0] == 160, \
        "Total fines for '100 comstock ave' should be 160"