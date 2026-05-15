import requests

url = 'https://api.github.com/search/repositories'
keyword = 'python'

max_pages = 10
per_page = 100

result = []

for page in range(1, max_pages + 1):
    params = {
        'q': keyword,
        'per_page': per_page,
        'page': page
    }

    res = requests.get(url, params=params)
    data = res.json()
    items = data['items']

    for item in items:
        name = item['name']
        full_name = item['full_name']
        git_url = item['git_url']
        desc = item['description']

        result.append({
            'name': name,
            'full_name': full_name,
            'git_url': git_url,
            'description': desc
        })

        print(f'''
            name        : {name}
            full_name   : {full_name}
            git_url     : {git_url}
            description : {desc}
            ''')