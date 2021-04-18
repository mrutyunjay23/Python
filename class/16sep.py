class A:
    div = 'A'

    def __init__(self, x):
        self.name = x


a1 = A('p')
a2 = A('q')
print(a1.name)
print(a2.name)
a1.name = 'r'
print(a1.name)
print(a2.name)
print(a1.div)
