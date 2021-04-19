'''def outerfunc(func):
    def infunc(name):
        if name == "ABCD":
            print("Bad Luck")
        else:
            func(name)
    return infunc

def wish1(name):
    print("Again Hello {}".format(name))


innerfunc = outerfunc(wish1)

wish1("abhishek")
innerfunc("abhishek")
wish1("ABCD")
innerfunc("ABCD")

@outerfunc
def wish2(name):
    print("Hello {}, Good Luck".format(name))

wish2("abhishek")
wish2("ABCD")

'''



def decfunc1(func):
    print("inside decfunc1")
    def inner():
        x = func()
        print(x*x)
        return x*x
    return inner


def decfunc2(func):
    print("inside decfunc2")
    def inner():
        x = func()
        print(2*x)
        return 1000
    return inner


# @decfunc1
@decfunc2
def num():
    return 5


print(num())
