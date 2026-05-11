users = [
    {"name": "김민준", "age": 29, "location": "서울", "car": "현대 아반떼"},
    {"name": "이서연", "age": 34, "location": "부산", "car": "기아 K5"},
    {"name": "박지훈", "age": 41, "location": "대구", "car": "제네시스 G80"},
    {"name": "최유진", "age": 26, "location": "인천", "car": "현대 코나"},
    {"name": "정하은", "age": 31, "location": "광주", "car": "기아 쏘렌토"},
    {"name": "조민석", "age": 38, "location": "대전", "car": "현대 싼타페"},
    {"name": "윤지우", "age": 24, "location": "울산", "car": "기아 모닝"},
    {"name": "강서준", "age": 45, "location": "수원", "car": "제네시스 GV80"},
    {"name": "한지민", "age": 28, "location": "성남", "car": "현대 아이오닉5"},
    {"name": "송현우", "age": 36, "location": "고양", "car": "기아 K8"},
    {"name": "김민준", "age": 33, "location": "서울", "car": "BMW 320i"},
    {"name": "이서연", "age": 27, "location": "부산", "car": "현대 아반떼"},
    {"name": "박지훈", "age": 22, "location": "인천", "car": "기아 레이"},
    {"name": "최유진", "age": 39, "location": "대전", "car": "제네시스 G70"},
    {"name": "정우성", "age": 44, "location": "서울", "car": "벤츠 E클래스"},
    {"name": "강민지", "age": 30, "location": "광주", "car": "기아 스포티지"},
    {"name": "윤서준", "age": 25, "location": "대구", "car": "현대 투싼"},
    {"name": "한지민", "age": 32, "location": "수원", "car": "테슬라 모델 3"},
    {"name": "이도윤", "age": 37, "location": "울산", "car": "기아 K9"},
    {"name": "박서준", "age": 28, "location": "성남", "car": "현대 쏘나타"},
]

def findUserAndPrint(name):
    for user in users:
        # if user['name'] == name <- 정확하게 일치하는가
        if user['name'].startswith(name):
            print(user)

findUserAndPrint('이')
print('-' * 50)

def findUserByName(name):
    userList = []
    for user in users:
        if user['name'].startswith(name):
            userList.append(user)
    return userList

findUserList = findUserByName('이')
print('find user: ', findUserList)
print('-' * 50)

def findUsersByNameOrAge(name = None, age = None):
    userList = []
    for user in users:
        if name is not None and age is not None:
            if user['name'] == name and user['age'] == age:
                userList.append(user)
        elif name is not None:
            if user['name'] == name:
                userList.append(user)
        elif age is not None:
            if user['age'] == age:
                userList.append(user)
    return userList

findUserList = findUsersByNameOrAge('강민지', 30)
print('find user(name & age): ', findUserList)
findUserList = findUsersByNameOrAge('강민지')
print('find user(name): ', findUserList)
findUserList = findUsersByNameOrAge(age = 30)
print('find user(age): ', findUserList)
print('-' * 50)

def findUser(name = None, age = None, loc = None):
    # 인자가 늘어나도 수정하기 편함
    userList = []
    for user in users:
        if (name is None or user['name'] == name) \
            and (age is None or user['age'] == age) \
            and (loc is None or user['location'] == loc):
            userList.append(user)
    return userList

findUserList = findUser('강민지', 30, '광주')
print('find user(name & age): ', findUserList)
findUserList = findUser('강민지')
print('find user(name): ', findUserList)
findUserList = findUser(age = 30)
print('find user(age): ', findUserList)
print('-' * 50)

searchCondition1 = {
    'name': '조민석'
}

searchCondition2 = {
    'name': '강민지',
    'age': 25
}

searchCondition3 = {
    'age': 27
}

def findUserBest(condition):
    # 검색 조건을 dict 형태로 받음
    userList = []
    for user in users:
        if user.get('name') == condition.get('name', '') and \
           user.get('age') == condition.get('age', '') and \
           user.get('location') == condition.get('location', ''):
            userList.append(user)
    return userList

print(findUserBest(searchCondition1))
print(findUserBest(searchCondition2))
print(findUserBest(searchCondition3))
