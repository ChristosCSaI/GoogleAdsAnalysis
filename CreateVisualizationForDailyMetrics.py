import matplotlib.pyplot as plt

# Plot Clicks, Impressions, and Cost over time
plt.figure(figsize=(14, 7))

# Plot Clicks
plt.subplot(3, 1, 1)
plt.plot(ad_data_df['Day'], ad_data_df['Clicks'], label='Clicks', color='b')
plt.title('Daily Clicks')
plt.xlabel('Date')
plt.ylabel('Clicks')
plt.grid(True)

# Plot Impressions
plt.subplot(3, 1, 2)
plt.plot(ad_data_df['Day'], ad_data_df['Impressions'], label='Impressions', color='g')
plt.title('Daily Impressions')
plt.xlabel('Date')
plt.ylabel('Impressions')
plt.grid(True)

# Plot Cost
plt.subplot(3, 1, 3)
plt.plot(ad_data_df['Day'], ad_data_df['Cost'], label='Cost', color='r')
plt.title('Daily Cost')
plt.xlabel('Date')
plt.ylabel('Cost ($)')
plt.grid(True)

plt.tight_layout()
plt.show()
