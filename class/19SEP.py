class student:
    '''developed by durga fur python demo'''
    def __init__(self):
        self.name='Durga'
        self.age=40
        self.marks=80

    def talk(self):
        print("Hello I am:",self.name)
        print("My Age is:",self.age)
        print("My Marks are:",self.marks)

a=student()
a.talk()