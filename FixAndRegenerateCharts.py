# Regenerate charts for campaigns and save them

# Create and save visualizations for campaigns
campaign_images = [
    ('Total Clicks by Campaign', '/mnt/data/campaign_clicks_fixed.png'),
    ('Total Impressions by Campaign', '/mnt/data/campaign_impressions_fixed.png'),
    ('Total Cost by Campaign', '/mnt/data/campaign_cost_fixed.png'),
    ('Total Conversions by Campaign', '/mnt/data/campaign_conversions_fixed.png'),
    ('CTR by Campaign', '/mnt/data/campaign_ctr_fixed.png'),
    ('Conversion Rate by Campaign', '/mnt/data/campaign_conversion_rate_fixed.png')
]

fig, ax = plt.subplots(3, 2, figsize=(14, 14))
ax[0, 0].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['Clicks'], color='b')
ax[0, 0].set_title('Total Clicks by Campaign')
ax[0, 0].set_xlabel('Campaign')
ax[0, 0].set_ylabel('Clicks')
fig.savefig(campaign_images[0][1])

ax[0, 1].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['Impressions'], color='g')
ax[0, 1].set_title('Total Impressions by Campaign')
ax[0, 1].set_xlabel('Campaign')
ax[0, 1].set_ylabel('Impressions')
fig.savefig(campaign_images[1][1])

ax[1, 0].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['Cost'], color='r')
ax[1, 0].set_title('Total Cost by Campaign')
ax[1, 0].set_xlabel('Campaign')
ax[1, 0].set_ylabel('Cost ($)')
fig.savefig(campaign_images[2][1])

ax[1, 1].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['Conversions'], color='purple')
ax[1, 1].set_title('Total Conversions by Campaign')
ax[1, 1].set_xlabel('Campaign')
ax[1, 1].set_ylabel('Conversions')
fig.savefig(campaign_images[3][1])

ax[2, 0].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['CTR'], color='orange')
ax[2, 0].set_title('CTR by Campaign')
ax[2, 0].set_xlabel('Campaign')
ax[2, 0].set_ylabel('CTR (%)')
fig.savefig(campaign_images[4][1])

ax[2, 1].bar(campaign_summary_cleaned['Campaign'], campaign_summary_cleaned['Conversion Rate'], color='cyan')
ax[2, 1].set_title('Conversion Rate by Campaign')
ax[2, 1].set_xlabel('Campaign')
ax[2, 1].set_ylabel('Conversion Rate (%)')
fig.savefig(campaign_images[5][1])
plt.close()

# Create and save visualizations for ad groups
adgroup_images = [
    ('Top 10 Ad Groups by Clicks', '/mnt/data/adgroup_clicks_fixed.png'),
    ('Top 10 Ad Groups by Impressions', '/mnt/data/adgroup_impressions_fixed.png'),
    ('Top 10 Ad Groups by Cost', '/mnt/data/adgroup_cost_fixed.png'),
    ('Top 10 Ad Groups by Conversions', '/mnt/data/adgroup_conversions_fixed.png'),
    ('Top 10 Ad Groups by CTR', '/mnt/data/adgroup_ctr_fixed.png'),
    ('Top 10 Ad Groups by Conversion Rate', '/mnt/data/adgroup_conversion_rate_fixed.png')
]

top_adgroups_clicks = adgroup_summary_cleaned.nlargest(10, 'Clicks')

fig, ax = plt.subplots(3, 2, figsize=(14, 14))

ax[0, 0].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['Clicks'], color='b')
ax[0, 0].set_title('Top 10 Ad Groups by Clicks')
ax[0, 0].set_xlabel('AdGroup')
ax[0, 0].set_ylabel('Clicks')
fig.savefig(adgroup_images[0][1])

ax[0, 1].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['Impressions'], color='g')
ax[0, 1].set_title('Top 10 Ad Groups by Impressions')
ax[0, 1].set_xlabel('AdGroup')
ax[0, 1].set_ylabel('Impressions')
fig.savefig(adgroup_images[1][1])

ax[1, 0].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['Cost'], color='r')
ax[1, 0].set_title('Top 10 Ad Groups by Cost')
ax[1, 0].set_xlabel('AdGroup')
ax[1, 0].set_ylabel('Cost ($)')
fig.savefig(adgroup_images[2][1])

ax[1, 1].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['Conversions'], color='purple')
ax[1, 1].set_title('Top 10 Ad Groups by Conversions')
ax[1, 1].set_xlabel('AdGroup')
ax[1, 1].set_ylabel('Conversions')
fig.savefig(adgroup_images[3][1])

ax[2, 0].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['CTR'], color='orange')
ax[2, 0].set_title('Top 10 Ad Groups by CTR')
ax[2, 0].set_xlabel('AdGroup')
ax[2, 0].set_ylabel('CTR (%)')
fig.savefig(adgroup_images[4][1])

ax[2, 1].bar(top_adgroups_clicks['AdGroup'], top_adgroups_clicks['Conversion Rate'], color='cyan')
ax[2, 1].set_title('Top 10 Ad Groups by Conversion Rate')
ax[2, 1].set_xlabel('AdGroup')
ax[2, 1].set_ylabel('Conversion Rate (%)')
fig.savefig(adgroup_images[5][1])
plt.close()

