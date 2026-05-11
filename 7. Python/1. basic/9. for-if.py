nums = [1, 2, 3, 4, 5]

# for n in [1, 2, 3, 4, 5]:
#     print(n)

# for n in range(1, 6):
#     print(n)

for n in nums:
    if n % 2 == 0:
        print(f'{n} is Even Number')
    else:
        print(f'{n} is Odd Number')
print('-' * 50)

evenNum = []
oddNum = []

for n in nums:
    if n % 2 == 0:
        evenNum.append(n)
    else:
        oddNum.append(n)

print(f'Even Numbers: {evenNum}')
print(f'Odd Numbers: {oddNum}')
print('-' * 50)

import time

n = 100
cnt = 0
startTime = time.time()
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                cnt += 1
endTime = time.time()
execTime = endTime - startTime

print(f'Total: {cnt}')
print(f'{execTime:.1f} Sec')

# 시간 복잡도: O(n^4) / 공간 복잡도