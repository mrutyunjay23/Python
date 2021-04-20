class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer('mrutyunjay', 'swami', 50000)
dev_2 = Employee('test', 'employee', 60000)

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)