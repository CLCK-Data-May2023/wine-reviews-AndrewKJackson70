import pandas as pd
#Bring in the whole csv as a dataframe
df = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
#This creates the dataframe we're using and I'm using agg to summarize the data
country_overview = df.groupby('country').agg({'country': 'count', 'points': 'mean'}).rename(columns={'country': 'count'})
#Round the average point amount to 1 decimal place
country_overview['points'] = country_overview['points'].round(1)
#This makes sure that the index column is reset to "country"
country_overview.reset_index(inplace=True)
#Writing my results to CSV
country_overview.to_csv('data/reviews-per-country.csv', index=False)

#Personal test to check my work
print(country_overview.head)
