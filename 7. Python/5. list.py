list = [1, 2, 3, 4, 5]
print(list)
print(len(list))
print(list[0]) # 모든 언어의 index는 0부터 시작
print(list[4])
print(list[-1]) # 리스트를 거꾸로부터 순회 -> 마지막 idx
print(list[-2])

print(list[1:3]) # idx 1부터 3 미만까지 -> 1, 2
print(list[:-1])
print(list[3:])

print('-' * 25, 'add & delete', '-' * 25)
# 원본 리스트에 요소 추가하기
list.append(6)
print(list)
# 특정 위치에 요소 추가하기
list.insert(2, 99)
print(list)
# 해당 값의 요소 삭제하기
list.remove(99)
print(list)
# 해당 idx의 요소 삭제하기
list.pop() # append와 pop은 기본적으로 가장 뒤의 idx에 값을 추가하거나 삭제
print(list)
# list 삭제
list.clear()
print(list)

print('-' * 25, 'sort', '-' * 25)
list = [5, 4, 2, 5, 1, 3, 8, 64, 24, 13, 4]
print(list)
list.sort() # sort를 호출하는 순간 raw data의 idx가 변경됨
print(list)
list = [5, 4, 2, 5, 1, 3, 8, 64, 24, 13, 4]
print(sorted(list)) # raw data를 변경하지 않고 정렬해서 보여줌

print('-' * 25, 'copy', '-' * 25)
copied_list = list.copy()
print(copied_list)
copied_list.sort(reverse=True)
print(copied_list)
print(list)

print('-' * 25, 'make number list', '-' * 25)
number = [x for x in range(11)] # start value 지정 없으면 0부터 시작
print(number)
number = [x ** 2 for x in range(1, 6)]
print(number)
number = [x for x in range(1, 20) if x % 2 == 0] # even num
print(number)
number = [x for x in range(1, 20) if x % 2 != 0] # odd num
print(number)

print('-' * 25, 'list', '-' * 25)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # list의 value가 아닌 list 자체를 더한다
print(list3)
print(list3 * 3) # list의 value에 곱하는 것이 아니라 list 자체를 3회 반복