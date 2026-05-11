my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(my_list)
print(my_tuple)
print(my_list[2])
print(my_tuple[2])

my_list[2] = 99
# my_tuple[3] = 99 -> tuple은 읽기 전용이라 data를 변경할 수 없음

print(my_list[0:1])
print(my_tuple[0:1]) # tuple임을 알려주기 위해 요소가 하나일때면 ,가 보임

t_list = list(my_tuple) # tuple을 list로 변환
print(t_list)
l_tuple = tuple(my_list) # lisf를 tuple로 변환
print(l_tuple)

a, b, c = (1, 2, 3) # tuple unpacking
print(a, b, c)

# example
p = ('John', 23, 'student')
name, age, occ = p
print(name)
print(age)