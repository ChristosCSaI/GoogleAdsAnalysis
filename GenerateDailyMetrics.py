import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\user\GoogleAdsPerformance\Updated_AdWords_exercise.xlsx'
ad_data = pd.read_excel(file_path, sheet_name=None)
ad_data_df = ad_data['Sheet1']
ad_data_df['Day'] = pd.to_datetime(ad_data_df['Day'], format='%d-%m-%Y')

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
plt.savefig('daily_metrics.png')
plt.close()
