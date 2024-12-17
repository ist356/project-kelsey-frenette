import pandas as pd
import streamlit as st

# Function to load and clean the data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=["Date"], low_memory=False)
    data.columns = data.columns.str.strip()
    data["Location"] = data["Location"].str.strip().str.lower()
    data.rename(columns={"Amounnt": "Amount"}, inplace=True)
    return data

# Function to filter data based on street names and date range
def filter_data(data, streets, start_date, end_date):
    # Remove timezone from Date column
    data["Date"] = data["Date"].dt.tz_localize(None)

    # Filter data by streets and date range
    filtered_data = data[
        data["Location"].str.contains("|".join(streets), na=False) &
        (data["Date"] >= pd.Timestamp(start_date)) &
        (data["Date"] <= pd.Timestamp(end_date))
    ]
    return filtered_data

# Function to aggregate the filtered data
def aggregate_data(filtered_data):
    aggregated_data = filtered_data.groupby("Location").agg(
        Total_Tickets=("Violation", "count"),
        Total_Fines=("Amount", "sum")
    ).reset_index()
    return aggregated_data

# Main Streamlit App
def main():
    st.title("Parking Violations Dashboard")
    st.write("Analyze parking violations by location and date range.")

    # File input
    file_path = st.file_uploader("Upload the Parking Violations CSV", type=["csv"])
    
    if file_path is not None:
        # Load data
        data = load_data(file_path)
        st.success("Data loaded successfully!")
        st.write("Sample of the Data:")
        st.dataframe(data.head())

        # Input filters
        streets_of_interest = st.text_input(
            "Enter Streets of Interest (comma-separated)", "comstock, walnut, marshall, university"
        )
        start_date = st.date_input("Start Date", pd.Timestamp("2024-08-01"))
        end_date = st.date_input("End Date", pd.Timestamp("2024-12-31"))

        # Process filters
        streets = [street.strip().lower() for street in streets_of_interest.split(",")]
        filtered_data = filter_data(data, streets, start_date, end_date)

        # Display filtered data
        if not filtered_data.empty:
            st.subheader("Filtered Data")
            st.dataframe(filtered_data)

            # Aggregate data
            aggregated_data = aggregate_data(filtered_data)
            st.subheader("Aggregated Data")
            st.dataframe(aggregated_data)
        else:
            st.warning("No data matches the specified filters. Please try again.")

# Run the Streamlit app
if __name__ == "__main__":
    main()