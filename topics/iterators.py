'''
iterators
'''
'''
if a class has __itr__ and __next__ method the class is iterator class
and the object is iterative object
'''

'''
********************************       List is a iterator
list has inbuit itr and next methods
'''
list1 = [i for i in range(101)]# created a list
'''
iteritem = iter(list1)
print(next(iteritem))
print(next(iteritem))
while iteritem:
    print(next(iteritem))  #iterat values up to last object
#print(next(iteritem))  #this line will give error at next method as iterations are completed

'''
'''***************************         Creating our own iterator'''

class DemoIterator():

    index = 0

    def __init__(self,number):
        self.value = number

    def __iter__(self):
        return self

    def __next__(self):
        if DemoIterator.index < 10:
            self.value = self.value * 2
            DemoIterator.index += 1
            return self.value
        else:
            #try:
            raise StopIteration
            #except Exception as E:
                #print("Iterations are over")


d = DemoIterator(10)
print(d.__next__())  # print next value for number 10(logic in __next__ method) this will be 20

iterator_d = d.__iter__()# we can call next method for __iter__() object from above statement
print(next(iterator_d))#next value for number 10(this will be 40
print(iterator_d)

d2 = DemoIterator(20)
for item in d2:
    print(item)
    #if item == None:
        #break

#while iterator_d:
 #   print(next(iterator_d))

'''
Multiple table
'''
class DemoIterator():
    index = 0
    sumval = 0

    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self

    def __next__(self):
        DemoIterator.sumval = DemoIterator.sumval + self.val
        if DemoIterator.sumval > 10 * self.val:
            raise StopIteration
        return DemoIterator.sumval


d = DemoIterator(5)
iteritem = iter(d)
while iteritem:
    print(next(iteritem))