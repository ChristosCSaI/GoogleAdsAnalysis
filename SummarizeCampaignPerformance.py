import pandas as pd

# Load the dataset
file_path = r'C:\Users\user\GoogleAdsPerformance\Updated_AdWords_exercise.xlsx'
ad_data = pd.read_excel(file_path, sheet_name=None)
ad_data_df = ad_data['Sheet1']
ad_data_df['Day'] = pd.to_datetime(ad_data_df['Day'], format='%d-%m-%Y')

# Aggregate data by Campaign
campaign_summary = ad_data_df.groupby('Campaign').agg({
    'Clicks': 'sum',
    'Impressions': 'sum',
    'Cost': 'sum',
    'Conversions': 'sum'
}).reset_index()

# Calculate additional metrics
campaign_summary['CTR'] = (campaign_summary['Clicks'] / campaign_summary['Impressions']) * 100
campaign_summary['Cost per Conversion'] = campaign_summary.apply(
    lambda row: row['Cost'] / row['Conversions'] if row['Conversions'] != 0 else pd.NA, axis=1
)
campaign_summary['Conversion Rate'] = campaign_summary.apply(
    lambda row: (row['Conversions'] / row['Clicks']) * 100 if row['Clicks'] != 0 else pd.NA, axis=1
)

print(campaign_summary)
