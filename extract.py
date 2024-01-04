# Selecting relevant columns for analysis
relevant_columns = ['Date', 'Title', 'Social Mention/Comment', 'Sentiment', 'Emotion']
social_data = social_listening_data[relevant_columns].dropna()

# Basic overview of the data - checking for the range of dates, sentiment and emotion distributions
overview = {
    "Date Range": [social_data['Date'].min(), social_data['Date'].max()],
    "Number of Mentions": len(social_data),
    "Sentiment Distribution": social_data['Sentiment'].value_counts(),
    "Emotion Distribution": social_data['Emotion'].value_counts()
}

# Extracting relevant columns for focused analysis
relevant_columns = ['Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 8', 'Unnamed: 9']  # Columns corresponding to Date, Title, Social Mention/Comment, Sentiment, Emotion
social_data_filtered = social_listening_data[relevant_columns].dropna().rename(columns={
    'Unnamed: 3': 'Date',
    'Unnamed: 4': 'Title',
    'Unnamed: 5': 'Social Mention/Comment',
    'Unnamed: 8': 'Sentiment',
    'Unnamed: 9': 'Emotion'
})

# Displaying a snippet of the filtered data for verification
social_data_filtered.head()