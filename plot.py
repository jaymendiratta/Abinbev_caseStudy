import matplotlib.pyplot as plt

# Analysis of Sentiment and Emotion distributions
sentiment_distribution = social_data_filtered['Sentiment'].value_counts()
emotion_distribution = social_data_filtered['Emotion'].value_counts()

# Plotting the distributions
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sentiment_distribution.plot(kind='bar', color='skyblue')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Counts')

plt.subplot(1, 2, 2)
emotion_distribution.plot(kind='bar', color='lightgreen')
plt.title('Emotion Distribution')
plt.xlabel('Emotion')
plt.ylabel('Counts')

plt.tight_layout()
plt.show()

# Displaying the top comments for positive and negative sentiments
top_positive_comments = social_data_filtered[social_data_filtered['Sentiment'] == 'positive']['Social Mention/Comment'].head(5).tolist()
top_negative_comments = social_data_filtered[social_data_filtered['Sentiment'] == 'negative']['Social Mention/Comment'].head(5).tolist()

(top_positive_comments, top_negative_comments)