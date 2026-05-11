students = {
    '김민수': 70,
    '이지수': 45,
    '박현진': 88,
    '최서연': 62,
    '정지호': 91,
    '강동현': 54,
    '조유나': 77,
    '윤태현': 83,
    '장소민': 49,
    '임민지': 68,
    '한준서': 95,
    '신혜진': 73,
    '서우빈': 58,
    '황지연': 81,
    '안성민': 66
}

print(students)
print('-' * 50)

def get_a_student(students):
    s = []
    for name, score in students.items():
        if score >= 90:
            s.append(name)
    return s

print(get_a_student(students))
