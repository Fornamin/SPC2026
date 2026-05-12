# 
with open('7. Python/File/file.txt', 'r', encoding = 'UTF-8') as file:
    data = file.read()
    print(data)

# 2. Legacy -> file.close()가 필요
# file = open('file.txt', 'r', encoding='UTF-8')

# 3. 용량이 큰 file read
with open('7. Python/File/file.txt', 'r', encoding = 'UTF-8') as file:
    lines = file.readlines()