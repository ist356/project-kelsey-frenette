# About My Project

Student Name:  Kelsey Frenette
Student Email:  kfrenett@syr.edu

### What it does
For my project I decided to take all of parking violations in Syracuse, NY in 2024 and have it be extracted, transformed and analyzed. 
this is a breakdown of each area:
1.File Loading:
	•The project loads a dataset of parking violations from a specified file (e.g., cache/Parking Violations 2024.csv).
	•Ensures the dataset includes properly parsed dates and normalized column names.
2.Filtering Data:
	•Filters the parking violation data to include only entries:
	•From specific streets (Comstock, Walnut, Marshall, University).
	•Within a defined date range (e.g., August 2024 to December 2024).
	•Uses partial string matching to locate these streets within full addresses.
3.Aggregating Data:
	•Groups the filtered data by location.
	•Calculates:
	    •The total number of parking tickets issued (Total_Tickets).
	    •The total fines collected (Total_Fines).
4.Streamlit Dashboard:
	•Provides an interactive interface using Streamlit:
	    •Allows users to upload a dataset.
	    •Lets users specify streets and date ranges for filtering.
	    •Displays filtered and aggregated data in a clean, user-friendly format.
5.Visualizing Data:
	•Generates bar charts using Seaborn:
        •Displays the top 10 locations with the highest ticket counts.
	    •Displays the top 10 locations with the highest fines collected.
6.Testing:
	•Includes tests to verify:
	    •Filtering logic for both street names and date ranges.
	    •Correct aggregation of tickets and fines.
### How you run my project

- First run the pandaslib.py to get the dataset (Parking Violations 2024)
- Execute code.py to load, filter, aggregate, and save the results as CSV files
- Run the Streamlit.py in streamlit for interactive analysis. (you will have to save the parking violations csv to your computer)
- Run the visualize.py code to see the data in bar plot graphs
- tests can be run in the testing tab from the test_script.py

### Other things you need to know
I'm honestly unsure if the CSV (Parking Violations 2024) will copy over when u run in because I'm not sure if I did it correctly.