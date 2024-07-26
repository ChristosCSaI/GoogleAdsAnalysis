import pandas as pd

# Load the dataset
file_path = r'C:\Users\user\GoogleAdsPerformance\Updated_AdWords_exercise.xlsx'
ad_data = pd.read_excel(file_path, sheet_name=None)
ad_data_df = ad_data['Sheet1']
ad_data_df['Day'] = pd.to_datetime(ad_data_df['Day'], format='%d-%m-%Y')

# Aggregate data by AdGroup
adgroup_summary = ad_data_df.groupby('AdGroup').agg({
    'Clicks': 'sum',
    'Impressions': 'sum',
    'Cost': 'sum',
    'Conversions': 'sum'
}).reset_index()

# Calculate additional metrics
adgroup_summary['CTR'] = (adgroup_summary['Clicks'] / adgroup_summary['Impressions']) * 100
adgroup_summary['Cost per Conversion'] = adgroup_summary.apply(
    lambda row: row['Cost'] / row['Conversions'] if row['Conversions'] != 0 else pd.NA, axis=1
)
adgroup_summary['Conversion Rate'] = adgroup_summary.apply(
    lambda row: (row['Conversions'] / row['Clicks']) * 100 if row['Clicks'] != 0 else pd.NA, axis=1
)

print(adgroup_summary)
