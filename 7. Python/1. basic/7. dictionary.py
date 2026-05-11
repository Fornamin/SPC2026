# key-value로 쌍을 이루고 있는 자료 구조
dict = {'name': 'Alice', 'age': 25, 'loc': 'Seoul'}

print(dict['name'])
print(dict['age'])

dict['car'] = 'BMW'
print(dict)

del dict['loc']
print(dict)

dict.pop('age') # pop을 조금 더 자주 씀
print(dict)

dict.clear()
print(dict)

my_squares = {x: x ** 2 for x in range(10)}
print(my_squares)

# list: []
# tuple: ()
# dict: {}