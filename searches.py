# Extracting relevant sections of the data for analysis
# Top Related Queries/Search
top_related_queries = google_search_data.iloc[7:19, [1, 2]].dropna().rename(columns={'Unnamed: 1': 'Query', 'Unnamed: 2': 'Interest Score'})

# Weekly Interest Scores by Region
weekly_interest_scores = google_search_data.iloc[7:19, [4, 5, 7, 8]].dropna().rename(columns={'Unnamed: 4': 'Week', 'Unnamed: 5': 'Interest Score', 'Unnamed: 7': 'Region', 'Unnamed: 8': 'Region Interest Score'})

# Average Monthly Searches
avg_monthly_searches = google_search_data.iloc[7:19, [12, 13]].dropna().rename(columns={'Unnamed: 12': 'Keyword', 'Unnamed: 13': 'Avg. Monthly Searches'})

# Displaying a snippet of each section for verification
(top_related_queries.head(), weekly_interest_scores.head(), avg_monthly_searches.head())