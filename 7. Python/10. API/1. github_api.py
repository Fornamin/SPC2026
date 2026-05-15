import requests

url = 'https://api.github.com/orgs/apache/repos'
res = requests.get(url)
repo_list = res.json()

repo_data = []

for item in repo_list:
    name = item['name']
    url = item['url']
    description = item['description']
    repo_data.append({'name': name, 'url': url, 'description': description})

for item in repo_data:
    print(f'{item['name']:<20}, {item['url']:<150}')
