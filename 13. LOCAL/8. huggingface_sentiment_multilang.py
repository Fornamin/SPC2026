# 분류 (Text Classification)

from transformers import pipeline

pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

reviews = [
    "진짜 기대 안 했는데 생각보다 너무 좋아서 놀랐어요.",
    "배송은 빨랐지만 제품 퀄리티는 솔직히 아쉽네요.",
    "가격이 조금 비싸긴 하지만 그만한 값어치는 합니다.",
    "불량품이 와서 교환받았습니다. 많이 불편했어요.",
    "몇 주째 사용 중인데 만족스럽고 추천할 만합니다.",
    "그냥 그래요. 나쁘진 않은데 특별히 좋지도 않습니다.",
    "설명과 다른 제품이 와서 화가 났습니다.",
    "부모님 선물로 드렸는데 정말 좋아하시네요.",
    "재구매 의사는 없습니다. 기대 이하였습니다.",
    "배송, 품질, 디자인 모두 만족합니다. 최고예요!"
]

for review in reviews:
    result = pipe(review)
    print(f"리뷰: {review}")
    print(f"결과: {result}")
    print("-" * 50)