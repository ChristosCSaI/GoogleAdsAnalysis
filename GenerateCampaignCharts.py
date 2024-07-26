import pandas as pd
import matplotlib.pyplot as plt

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

# Ensure 'Campaign' is treated as a category
campaign_summary['Campaign'] = campaign_summary['Campaign'].astype('category')

# Generate charts for campaigns
fig, ax = plt.subplots(3, 2, figsize=(14, 14))

ax[0, 0].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['Clicks'], color='b')
ax[0, 0].set_title('Total Clicks by Campaign')
ax[0, 0].set_xlabel('Campaign')
ax[0, 0].set_ylabel('Clicks')
ax[0, 0].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[0, 0].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_clicks.png')

ax[0, 1].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['Impressions'], color='g')
ax[0, 1].set_title('Total Impressions by Campaign')
ax[0, 1].set_xlabel('Campaign')
ax[0, 1].set_ylabel('Impressions')
ax[0, 1].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[0, 1].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_impressions.png')

ax[1, 0].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['Cost'], color='r')
ax[1, 0].set_title('Total Cost by Campaign')
ax[1, 0].set_xlabel('Campaign')
ax[1, 0].set_ylabel('Cost ($)')
ax[1, 0].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[1, 0].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_cost.png')

ax[1, 1].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['Conversions'], color='purple')
ax[1, 1].set_title('Total Conversions by Campaign')
ax[1, 1].set_xlabel('Campaign')
ax[1, 1].set_ylabel('Conversions')
ax[1, 1].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[1, 1].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_conversions.png')

ax[2, 0].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['CTR'], color='orange')
ax[2, 0].set_title('CTR by Campaign')
ax[2, 0].set_xlabel('Campaign')
ax[2, 0].set_ylabel('CTR (%)')
ax[2, 0].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[2, 0].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_ctr.png')

ax[2, 1].bar(campaign_summary['Campaign'].cat.codes, campaign_summary['Conversion Rate'], color='cyan')
ax[2, 1].set_title('Conversion Rate by Campaign')
ax[2, 1].set_xlabel('Campaign')
ax[2, 1].set_ylabel('Conversion Rate (%)')
ax[2, 1].set_xticks(campaign_summary['Campaign'].cat.codes)
ax[2, 1].set_xticklabels(campaign_summary['Campaign'], rotation=90)
fig.savefig('campaign_conversion_rate.png')

plt.close()
