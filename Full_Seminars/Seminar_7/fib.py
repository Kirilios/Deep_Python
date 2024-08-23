def fibonacci():
    a = 0
    b = 1
    lst = []
    for _ in range(10):
        a, b = b, a + b
        lst.append(b)
    return lst

print(*fibonacci(), sep='\n')