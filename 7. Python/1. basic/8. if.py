score = 80
if score >= 80:
    # print('Your grade is A')
    grade = 'A'
elif score >= 70:
    # print('Your grade is B')
    grade = 'B'
elif score >= 60:
    # print('Your grade is C')
    grade = 'C'
else:
    # print('Your grade is F')
    grade = 'F'

print(f'Your score is {score}, and grade is {grade}')
print('-' * 50)

month = 7
if month in [12, 1, 2]:
    season = 'Winter'
    # print('Winter')
elif month in [3, 4, 5]:
    season = 'Spring'
    # print('Spring')
elif month in [6, 7, 8]:    
    season = 'Summer'
    # print('Summer')
elif month in [9, 10, 11]:
    season = 'Autumn'
    # print('Autumn')
else:   
    print('error')

print(f'month {month} is {season}')
print('-' * 50)

height = 175 # cm
weight = 70 # kg
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    category = '저체중'
elif bmi < 25:
    category = '정상'
elif bmi < 30:
    category = '과체중'
else:
    category = '비만'

print(f'키: {height}, 몸무게: {weight}, bmi: {bmi}\n당신은 {category}입니다')
print('-' * 50)

username = 'admin'
password = '1234'

if username and password:
    if username == 'admin' and password == '1234':
        print('Admin Login Success')
    elif username == 'user' and password == '1234':
        print('Normal Login Success')
    else:
        print('Incorrect user name or password')
else:
    print('Enter user name and password')