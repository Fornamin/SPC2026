print('Hello, Python')
print('Hello,', 'Python')
print('Hello, ' + 'Python')
print("Hello, " + 'Python')
print("'Hello, '" + '"Python"')
print('Hello, ' + 'Python' + '!')

num = 5
name = '홍길동'

print("Hello, {}".format(name))
print("Hello, {}. My Lucky Number is {}".format(name, num))
print("Hello, {0}. My Lucky Number is {1}".format(name, num))
print("Hello, {1}. My Lucky Number is {0}".format(name, num))
print("Hello, %s" % name)
print("Hello, %s" % name, end="")