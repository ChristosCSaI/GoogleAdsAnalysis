# Convert 'Day' column to datetime
ad_data_df['Day'] = pd.to_datetime(ad_data_df['Day'], format='%d-%m-%Y')

# Summarize overall performance
summary = ad_data_df.describe()

# Display the summary
import ace_tools as tools; tools.display_dataframe_to_user(name="Overall Performance Summary", dataframe=summary)

summary
