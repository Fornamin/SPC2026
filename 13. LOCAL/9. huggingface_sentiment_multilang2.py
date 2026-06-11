from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

text = '재밌다!'
inputs = tokenizer(text, return_tensors='pt', trucation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()

print(f'Predicted Sentiment Score: {predicted_class + 1}')

texts = ['이 노래 들을바엔 공사장 가서 드릴 소리 들음', '굿굿굿', '걍 그럼']
inputs = tokenizer(texts, return_tensors='pt', trucation=True, padding=True)
 
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    predictions = torch.argmax(logits, dim=1)

for text, pred in zip(texts, predictions):
    print(f'Sentence {text} -> Sentiment Score: {pred.item() + 1}')