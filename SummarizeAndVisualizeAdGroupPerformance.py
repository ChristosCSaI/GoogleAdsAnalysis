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

# Display the summary
tools.display_dataframe_to_user(name="AdGroup Performance Summary", dataframe=adgroup_summary)

adgroup_summary
