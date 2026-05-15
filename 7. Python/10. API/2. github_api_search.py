import requests

url = 'https://api.github.com/search/repositories'
keyword = 'python'
params = {
    'q': keyword,
    'per_page': 100,
    'page': 2
}

res = requests.get(url, params=params)
data = res.json()
items = data['items']
result = []

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
    