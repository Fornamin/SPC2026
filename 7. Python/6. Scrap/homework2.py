import requests

for page in range(1, 3):

    res = requests.get(
        f'https://makemyproject.net/shop/api/products?page={page}'
    )

    product_list = res.json()

    for item in product_list['items']:
        print(item['name'], item['final_price'], item['description'])

        # 상세 데이터
        res = requests.get(
        f'https://makemyproject.net/shop/api/product/{item['product_id']}'
        )
        
        product_info = res.json()
        print(product_info['sales_count'], product_info['reviews'])


