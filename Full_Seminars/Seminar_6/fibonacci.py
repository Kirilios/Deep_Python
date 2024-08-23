def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibo = fibonacci()
for _ in range(10):
    print(next(fibo))