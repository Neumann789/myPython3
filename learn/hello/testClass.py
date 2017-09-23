__author__ = 'fanghuabao'

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)

print(bob.name)
print(sue.name)
sue.giveraise(0.10)
print(sue.pay)
