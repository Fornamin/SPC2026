# 분류 (Text Classification)

# pip install transformers
from transformers import pipeline

sentiment_analyzer = pipeline(
    'sentiment-analysis', 
    model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
    # {Architectur} - {Size} - {Preprocessing} - {Learning Method} - {Dataset}

result = sentiment_analyzer(['hamburger', 'cheese', 'milk'])
print(result)

result = sentiment_analyzer('could you teach me english?')
print(result[0]['label'])