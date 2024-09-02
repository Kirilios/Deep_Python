class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        # self.first = 0
        # self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        # while self.start < self.stop:
        #     self.first, self.second = self.second, self.first + self.second
        #     if self.start <= self.first < self.stop:
        #         return self.first
        for i in range(self.start, self.stop):
            self.start += 1
            return chr(i)
        raise StopIteration


fib = Fibonacci(20, 100)
for num in iter(fib):
    print(num)

# char = (chr(i) for i in range(65, 91))
# for chars in iter(char):
#     print(chars)