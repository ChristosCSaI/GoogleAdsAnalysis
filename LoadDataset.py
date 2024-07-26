import pandas as pd

# Load the dataset
file_path = r'C:\Users\user\GoogleAdsPerformance\Updated_AdWords_exercise.xlsx'
ad_data = pd.read_excel(file_path, sheet_name=None)

# Display the sheet names to understand the structure of the file
ad_data.keys()
