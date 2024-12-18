import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = { # Simulated data (from provided text)
    "Location": [
        "100 comstock ave", "100 comstock pl", "100 marshall st", "100 walnut ave", "100 walnut pl",
        "1000 marshall st", "107 marshall st", "108 marshall st", "180 walnut pl", "200 comstock",
        "200 comstock ave", "200 comstock pl", "200 marshall st", "200 walnut ave", "200 walnut pl"
    ],
    "Total_Tickets": [141, 90, 501, 14, 674, 3, 2, 1, 3, 3, 124, 6, 353, 4, 398],
    "Total_Fines": [5130, 3035, 16395, 325, 18760, 75, 200, 100, 75, 75, 5000, 185, 7855, 75, 11760]
}

aggregated_data = pd.DataFrame(data)

top_locations = aggregated_data.nlargest(10, "Total_Tickets") # Filter for top locations by Total Tickets and Total Fines

colors = sns.color_palette("Set3", len(aggregated_data))  

# Bar chart for Total Tickets
plt.figure(figsize=(12, 6))
sns.barplot(x="Location", y="Total_Tickets", data=top_locations, palette= colors)
plt.title("Top 10 Locations by Total Tickets", fontsize=16)
plt.xlabel("Location", fontsize=12)
plt.ylabel("Total Tickets", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Bar chart for Total Fines
plt.figure(figsize=(12, 6))
sns.barplot(x="Location", y="Total_Fines", data=top_locations, palette=colors)
plt.title("Top 10 Locations by Total Fines", fontsize=16)
plt.xlabel("Location", fontsize=12)
plt.ylabel("Total Fines ($)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()