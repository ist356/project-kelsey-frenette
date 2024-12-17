import pandas as pd
from io import StringIO

# Simulated data (replace with real file path when accessible)
data = """Date,Location,Violation,Owed,Amount
2024/08/15 01:30:00,Comstock Ave,ODD/EVEN PARKING NOV-MAR,Collections,60
2024/09/01 11:30:00,Euclid Ave,NO PARKING ANY TIME,Paid in Full,25
2024/10/12 14:00:00,Walnut Ave,ODD/EVEN PARKING NOV-MAR,Collections,60
2024/11/20 09:30:00,Marshall St,ODD/EVEN PARKING NOV-MAR,Paid in Full,60
2024/12/05 17:00:00,University Ave,UNREG/UNAFFIXD/ALL,Collections,25"""

# Load data into a pandas DataFrame
df = pd.read_csv(StringIO(data), parse_dates=["Date"])
print(df)