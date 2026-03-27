from currency_converter import CurrencyConverter
c = CurrencyConverter()
p= c.convert(100,"USD","INR")
print(p)

import qrcode
from PIL import Image
image = qrcode.make("https://open.spotify.com")
image.save("lyk_in.png")
print("qr geneartion successfull")

class ATM:
    def __init__(self,balance):
        self._balance=balance

    def deposit(self,amount):
        self._balance+=amount
        print(f"deposited {amount}:the new balance if {self._balance}")

    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            print(f"withdrawn {amount}: the new balance is {self._balance}")

        else:
            print("insufficient amount to withdraw")
atm = ATM(1000)
atm.deposit(200)
atm.withdraw(400)

class user:
    def __init__(self,user):
        self.user=user
    def login(self):
        print(f"{self.user} logged in")
class admin(user):
    def delete(self):
        print("admin deleted this account")
a=admin("ranjitha")
print(a.user)
a.login()
a.delete()

class animal:
    def makesound(self):
        pass
class cat(animal):
        def makesound(self):
            print("cat make sound")
class dog(animal):
        def makesound(self):

            print("dog make sound")
class cheetha(animal):
        def makesound(self):
            print("CHEETHA MAKE SOUND")
class human(animal):
        def makesound(self):
            print("HUMAN MAKE SOUND")
animal=[cat(),dog(),cheetha(),human()]
for animals in animal:
      animals.makesound()
        
def class_name(func):
    def wrapper(a,b):
        print("result=",end="")
        func(a,b)
    return wrapper

@class_name
def add(a,b):
    print(a+b)
add(10,20)

def logger(func):
    def wrapper(a,b):
        print(f"function {func.__name__} was called here")
        func(a,b)
    return wrapper

@logger
def add(a,b):
    print(a+b)
 
@logger
def sub(a,b):
    print(abs(a-b))

add(10,20)
sub(20,30)

l=[1,2,3,4,5]
def double(x):
    return x**2

result=map(double,l)
print(list(result))
l=[2,3,4,5,6]
res=map(lambda x:x**2,l)
print(list(res))

a=[1,2,3,4,5]
b=[1,2,3,4,5]

res=map(lambda a,b:a+b,a,b)
print(list(res))

l=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x%2==0

res=filter(even,l)
print(list(res))

l=[1,2,3,4,5,6,7,8,9,10]
res=filter(lambda a:a%2==0,l)
print(list(res))

from functools import reduce
l=[1,2,3,4,5]
# def add(a,b):
#     return a+b

res=reduce(lambda a,b: a+b,l)
print(res)

class countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <=0:
            raise StopIteration 
        num=self.start
        self.start-=1
        return num
cd=countdown(5)
for i in (cd):
    print(i)

import sys
l=[x*x for x in range(1,100)]
print(type(l))
print(sys.getsizeof(l))

l=(x*x for x in range(1,100))
print(type(l))
print(sys.getsizeof(l))

def simple():
    yield 1
    yield 2
    yield 3
gen =simple()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

iterator = iter([1,2,3])

while True:
    try:
        value = next(iterator)
        print(type(value))
    except StopIteration:
        break
