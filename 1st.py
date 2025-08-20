import pandas as pd
from textblob import TextBlob

# Load the dataset from your local path
df = pd.read_csv(r"C:\Users\user\Desktop\ALL INTERNSHIPS (IMP)\12) CODEC (20th july - 20th august)\DATASETS\sentiment_data.csv")

# Check first few rows
print("📄 Sample Data:")
print(df.head())

# Apply sentiment polarity using TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

df['predicted_sentiment'] = df['text'].apply(get_sentiment)

# Display original vs predicted sentiments
print("\n📝 Predictions:")
print(df[['text', 'sentiment', 'predicted_sentiment']])