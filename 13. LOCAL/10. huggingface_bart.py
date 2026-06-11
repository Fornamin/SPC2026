from transformers import pipeline
import torch

classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
# MNLI: Multi-genre Natural Language Inference
# 문장-문장 연관성
# 1. 함의(Entaliment) EX. 오늘 비가 많이 내린다 - 우산이 필요할 수 있다
# 2. 모순(Contradiction) EX. 오늘 비가 많이 내린다 - 오늘은 맑은 날이다
# 3. 중립(Neutral) EX. 오늘 비가 많이 내린다 - 나는 피자를 좋아한다

texts = [
    "The new smartphone uses an advanced AI chip for faster image processing.",
    "The football team won the championship after a dramatic penalty shootout.",
    "Add two teaspoons of sugar and simmer the sauce for 15 minutes.",
    "The parliament passed a controversial bill after weeks of debate.",
    "Python is one of the most popular programming languages for data analysis.",
    "The athlete broke the world record in the 100-meter sprint.",
    "To make fluffy pancakes, mix the batter gently and avoid over-stirring.",
    "The presidential candidate announced a new economic policy.",
    "Researchers developed a quantum computing algorithm that improves efficiency.",
    "The basketball coach focused on defensive strategies during practice.",
    "The government invested heavily in artificial intelligence research.",
    "A famous athlete entered politics after retirement.",
    "The chef used a smart oven connected to the internet.",
    "The sports minister announced new regulations for professional leagues.",
    "Data analysis is changing how teams prepare for matches."
]

candidate_labels = ['technology', 'sports', 'cooking', 'politics']

for text in texts:
    result = classifier(text, candidate_labels=candidate_labels)

    print(f'[SENTENCE] {text}')
    for label, score in zip(result['labels'], result['scores']):
        print(f'- {label.upper():12} {score:3f}')

    print(f'[FINAL CLASSIFICATION] {result['labels'][0].upper()}')
    print('-' * 100)