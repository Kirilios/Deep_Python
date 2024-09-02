from logging import raiseExceptions


class Worker:


    def __init__(self, hours, rate):
        if hours < 0:
            raise ValueError('HoursValue Denied')
        if rate < 0:
            raise ValueError('RateValue Denied')
        self.hours = hours
        self.rate = rate

    def calculation(self):
        return self.rate * self.hours

if __name__ == '__main__':
    w = Worker(-10, 100)
    print(w.calculation())
    w.hours = -10
    print(w.calculation())