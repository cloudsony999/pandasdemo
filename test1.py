def test():
    print('I am amitava')

test()
test()

def call(a,b):
    return a+b

x=input('enter 1st no')
y=input('enter 2nd no')
x=int(x)
y=int(y)
print('the sum is ',call(x,y))

l=[1,2,3,4,5,6]
print(type(l))
for i in l:
    print(i)

t=('a','b','c','d','e')
print(type(t))
for i in t:
    print(i)

class Person:
    def __init__(self):
        print('I am constructor')
    def callme(self):
        print('call ME PLEASE!!!!')



p1=Person()
p2=Person()
p1.callme()
p2.callme()

