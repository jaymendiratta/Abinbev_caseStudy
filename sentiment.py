from textblob import TextBlob

# Sentiment analysis of the reviews
def analyze_sentiment(review):
    return TextBlob(review).sentiment.polarity

# Applying sentiment analysis to the reviews
e_commerce_reviews['Sentiment Score'] = e_commerce_reviews['Review'].apply(analyze_sentiment)

# Grouping by Flavour Name for insights
flavour_sentiment = e_commerce_reviews.groupby('Flavour Name')['Sentiment Score'].mean().sort_values(ascending=False)

# Displaying the sentiment scores per flavour
flavour_sentiment