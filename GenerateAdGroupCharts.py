import pandas as pd
import matplotlib.pyplot as plt

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

# Ensure 'AdGroup' is treated as a category
adgroup_summary['AdGroup'] = adgroup_summary['AdGroup'].astype('category')

# Generate charts for ad groups
fig, ax = plt.subplots(3, 2, figsize=(14, 14))

top_adgroups_clicks = adgroup_summary.nlargest(10, 'Clicks')

ax[0, 0].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['Clicks'], color='b')
ax[0, 0].set_title('Top 10 Ad Groups by Clicks')
ax[0, 0].set_xlabel('AdGroup')
ax[0, 0].set_ylabel('Clicks')
ax[0, 0].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[0, 0].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_clicks.png')

ax[0, 1].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['Impressions'], color='g')
ax[0, 1].set_title('Top 10 Ad Groups by Impressions')
ax[0, 1].set_xlabel('AdGroup')
ax[0, 1].set_ylabel('Impressions')
ax[0, 1].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[0, 1].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_impressions.png')

ax[1, 0].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['Cost'], color='r')
ax[1, 0].set_title('Top 10 Ad Groups by Cost')
ax[1, 0].set_xlabel('AdGroup')
ax[1, 0].set_ylabel('Cost ($)')
ax[1, 0].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[1, 0].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_cost.png')

ax[1, 1].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['Conversions'], color='purple')
ax[1, 1].set_title('Top 10 Ad Groups by Conversions')
ax[1, 1].set_xlabel('AdGroup')
ax[1, 1].set_ylabel('Conversions')
ax[1, 1].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[1, 1].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_conversions.png')

ax[2, 0].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['CTR'], color='orange')
ax[2, 0].set_title('Top 10 Ad Groups by CTR')
ax[2, 0].set_xlabel('AdGroup')
ax[2, 0].set_ylabel('CTR (%)')
ax[2, 0].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[2, 0].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_ctr.png')

ax[2, 1].bar(top_adgroups_clicks['AdGroup'].cat.codes, top_adgroups_clicks['Conversion Rate'], color='cyan')
ax[2, 1].set_title('Top 10 Ad Groups by Conversion Rate')
ax[2, 1].set_xlabel('AdGroup')
ax[2, 1].set_ylabel('Conversion Rate (%)')
ax[2, 1].set_xticks(top_adgroups_clicks['AdGroup'].cat.codes)
ax[2, 1].set_xticklabels(top_adgroups_clicks['AdGroup'], rotation=90)
fig.savefig('adgroup_conversion_rate.png')

plt.close()
