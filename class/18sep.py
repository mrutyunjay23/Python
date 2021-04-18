class Test:
    staticVar1 = 10  # Static Variable
    staticVar2 = 102

    def __init__(self, initVar):
        self.instancVar1 = 20  # Instance Variable
        self.initVar1 = initVar
        print(self.staticVar1)
        self.staticVar1 = 100
        print(Test.staticVar1)

    def display(self):
        self.instancVar2 = 30
        print(self.staticVar1)
        print(Test.staticVar1)


t1 = Test(50)
t1.instanceVar3 = 40
print(t1.instancVar1, t1.instanceVar3, t1.staticVar1, Test.staticVar1)
t1.display()

t2 = Test(50)

# print(t2.instanceVar3) #Gives error as instance3 variable is not defined for t2 object of class Test

t1.staticVar1 = 20  # New instance Variable is created with name staticVar1

print(t1.instancVar1, t1.instanceVar3, t1.staticVar1, Test.staticVar1)

print(t2.staticVar1)

Test.staticVar1 = 1000  # Changed the value of static Variable

print(t1.staticVar1)
print(t2.staticVar1)
print(Test.staticVar2)
t1.staticVar2 = 103
# Test.staticVar2 = 103
print(t1.staticVar2)
print(t2.staticVar2)
print(Test.staticVar2)
