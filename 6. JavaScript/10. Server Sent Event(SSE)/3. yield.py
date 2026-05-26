def numbers():
    for i in range(1000000):
        yield i

for n in numbers():
    print(n)
    if n >= 100:
        break