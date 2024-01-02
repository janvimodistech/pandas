import os
os.environ["NLTK_DATA"] = "D:/path/to/nltk_data"
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
text = "NLTK is awesome!"
sentiment_score = sia.polarity_scores(text)
print(sentiment_score)
