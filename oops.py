class human:
    def  __init__(self,name):
        self.name = name
       
    def walk(self):
        print(f"{self.name} is walking")

c = human("cahndan")
d = human("darshan")
c.walk()

class human:
    def __init__(self,name,age,salary=-1):#-1 seting as defult where i dont know salary there type it -1
        self.name=name
        self.age=age
        self.salary=salary
        
    def walk(self):
        print(f"{self.name} is walking")

c = human("ranjitha",19)
d = human("naveen",14,10)
print(c.salary)
print(d.age)
print(c.age)



#4 piilers of opps
# 1) abstraction
#2)  encapsulation
#3) inheritance
# 4) polymorphism

# Abstraction

class car:
    def __init__ (self,enginestarted):
        print("engine satrted")

    def __init__ (self,accelerate):
        print("car accelerated")

    def __init__ (self,brake):
        print("car stoped")

car = car()
car.accelerate()
        
           
class database:
    def __init__(self):
        #self.storage = {} #public attribute
        #self._storage = {} #protected attribute
        self.__storage = {} #private

    def write(self,key,value):
        self.__storage[key] = value

    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("db itezm not found")
        #return self.storage[key]
    
db = database()
db.write("sub","100k")
db.write("name","rp")
db.read("name")
#print(db.__storage)


#encapsulation
class ATM:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__amount=amount

        print(f"deposited{self.__amount} .new balance is{self.__balance}")


    def withdraw(self,amount):
       # self.amount=amount
        if amount<=self.__balance:
            print(f"withdraw{amount}.new balance is {self.__balance}")
        else:
            print("insufficient balance")

atm = ATM(10000)
atm.deposit(1000)
atm.withdraw(200)
print(atm.get_balance())


#inheritance

#inheritance allows class to inherit attribute and methods fron another class ,(facilitating reuse)

class user:
    def __init__(self,username):
        self.username=username

    def login(self):
        print(f"{self.username} logged in")

class admin(user):
    def delete_user(self):
        print("admin deleted the user")

a = admin("clg")
print(a.username)
a.login()
a.delete_user()

#polymorphism()
# it allows objects of defect classes to be treated as object of a common superclass
# but they can behave differently depending on the object type

class animal:
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("bark")

class cat(animal):
    def make_sound(self):
       # return super().make_sound()
        print("meow")

animals = [dog(),cat()]
for animal in animals:
    animal.make_sound()


#example 2

class notification:
    def send(self):
        print("notification sent")

class email_notification(notification):
    def send(self):
        print("email sent")

class sms_notification(notification):
    def send(self):
        print("sms was sent")



Notification = email_notification()
Notification = notification()
Notification = sms_notification()
Notification.send()


#getter and setter
#getter and setter are the methods that follow controlled access to an object's attribute

class student:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name=name

S=student("ranjitha",18)
print(S.get_name())
S.set_name("naveen")
print(S.get_name())

#method overloading

#method overloading is the ability to define multiple method with the same name but different parameters
#  note :python doesn't support method overlaping directly
# by using defult parameter or by handling varying number of arguments with *args and **kwargs

class calculator :
    def add (self,a,b,c=0):
        print(a+b+c)
c=calculator()
c.add(1,2)
c.add(2,3,1)

#super() function: is used in child class to call a method from a parent class ,enabling access to inherited 
# method @ attributes

class animal:
    def make_sound(self):
        print ("animal is making sound ")

class dog(animal):
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        super().make_sound()
        print("bark")
d=dog("doggy")
d.make_sound()

#method overriding:it allows a child to provide a specific implementation for a method that is already defined in its 
# parent class
#it enables the child class to alter or extend the behaviour of a parent class method

class animal:
    def sound(self):
        print("this animal makes sound")
class animal(dog): 
    def sound(self):
        print("dog bark")

Animal = animal()
print(Animal.sound())
Dog = dog()
print(Dog.sound())


#abstract class = an abstract class in python is a class that cannot be instantialated directly it can have abstract  method which must be implemented 
#  by subclass 
#  it provide blueprint for other classes enforcing a structures where subclass must implement certain methods 

from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):  #private class
        pass
class bike(vehicle): 
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("start engine")
b = bike ("royal enfield")
print(b.name)

class account:
    def __init__(self,id,holder_name,):
        self.id=id
        self.holder_name=holder_name
        self._balance=0 #encapsulation

    def check_balance(self):
        print(f"balance: {self._balance}")

    def deposit(self,amount):
        self._balance+=amount
        print(f"deposit sucessful:updated balance:{self._balance}")

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance-=amount
            print("withdraw sucessfull")

        else:
            print("no money left")


class savingaccount(account): #inheritance
    
    def calculate_intrest(self):
        interest_rate=0.04
        interest=self._balance *interest_rate
        print("intrest:{interest}")


class currentaccount(account): #inheritance

    def withdraw(self, amount):  #polymorphism
        overdraft_limit=1000
        if self._balance+overdraft_limit >=amount:
            self._balance-=amount
            print(f"withdraw sucessful.updated balance: {self._balance}")

        else:
            print("balance is over drifted")
        
    

class bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts={}

    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_account= savingaccount(id,holder_name)

        elif type=="corrent":
            new_account = currentaccount(id,holder_name)

        self.__accounts[id] = new_account
        print("account creation sucessful")
        return new_account

       

cbk = bank("state bank of indiia","banglore")

s1 = cbk.create_account("1","ranjitha","savings")
c1 = cbk.create_account("2","sanjitha","current")

s1.deposit(2000)
c1.deposit(200)

s1.withdraw(5000)
c1.withdraw(2000)

#object = a bundle of related attributes (variables)and methods (functions)
# ex.phone.cup,book,
#you need a class to create many objects
# class = (blueprint) used to design the structure and layyout of an object

from ocar import car

car1 = car("ertiga","bmw",2023,True)
car2 = car("fortuner","toyata",2025,False)

print(car1.model)
print(car1.year)
print(car1.for_sale)
print(car1.name)

print(car2.model)
print(car2.year)
print(car2.for_sale)
print(car2.name)
car1.stop()
car2.drive()
car2.describe()


#CLASS VARIABLES
#class variables =shared among all instance of a class
# defined outside the constructor
# allow you to share data among all objects created from that class

class students:

    class_year = 2024 #class variable
    num_students = 0


    def __init__(self,name,age):
        self.name = name
        self.age = age
        students.num_students += 1 #if u are modifying a class variiable
        #dont use self use a name of the class like students 

student1 = students("ranjitha",23)
student2 = students("usha",19)
student3 = students("neha",20)
student4 = students("nithya",22)

print(f"my graduating class of {students.class_year}has {students.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)


print(student1.name)
print(student2.age)

print(student1.class_year)#class variable can be better to access with
# a class name that u created insted of creating a variable like 
#students1,students2 (print(student1.class_year))or we can use directly the 
#class name (print(students.class_year))like this
print(students.class_year)
print(students.num_students)

# inheritance
#allows a class to inherit attributes and methods from another class helps with code reusability 
#and extensibility
#class child (parent)

class animal:
    def __init__(self,name):
        self.name= name
        self.is_alive= True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is slping")

class dog(animal):
    def speak(self):
        print("bow")
class cat(animal):
    def speak(self):
        print("meow")

Dog = dog("retriver")
Cat = cat("scooby")

print(Dog.name)
Dog.eat()
print(Cat.name)
Cat.sleep()
Cat.speak()

#multiple inheritance = inherit from more than one perent class C(A,B)
#multilevel inheritance = inherit from a parent which inherits from another parent
#                 C(B) <-B(A) <-A

class Animal:               #grand parent class (A)
    def eat (self):
        print("this animal is eating")

    def sleep (self):
        print("this animal is sleeping")

class prey(Animal):              #parent class B(A)
    def flee(self):
        print("this animal is fleeing")
class predator(Animal):
    def hunt(self):
        print("this animal is hunting")

class rabbit(predator):          #children class C(B)
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass


Rabbit = rabbit()

Hawk = hawk()
Fish = fish()


Rabbit.hunt()
Hawk.hunt()
Rabbit.eat()
Hawk.sleep()



#super() = function used in a child class methods from a parent class(superclass).
#allows you to extend the functionality of the inherited methods

class shapes:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

    def describe(self):
        print(f"it is{self.color} and {"filled" if self.filled else"6 not filled"}")
        
    
class circles(shapes):
    def __init__(self,color,filled,radius):
       self.color = color
       self.filled = filled
       self.radius=radius
        
       super().__init__(color,filled)
       self.radius=radius
    
    def describe (self):
        
        print(f"it is a circle of area {3.14*self.radius*self.radius}")
        super().describe()
        


class square(shapes):
     def __init__(self,color,filled,side):
        self.color= color
        self.filled= filled
        super().__init__(color,filled)
        self.side =side

     def describe (self):
        
        print(f"it is a squaree of area {self.side*self.side}")
        super().describe()
    
class triangles(shapes):
    def __init__(self,color,filled,angle):
        self.color = color
        self.filled=filled
        super().__init__(color,filled)
        self.angle=angle

    def describe (self):
        
        print(f"it is a triangle of angle{self.angle}")
        super().describe()


Circle=circles("red",True,5)
print(Circle.color)
print(Circle.filled)

Square=square("green",False,40)
print(Square.color)
print(Square.filled)
print(Square.side)

Triangle=triangles("orange",True,60)
print(Triangle.color)
print(Triangle.filled)
print(Triangle.angle)

Circle.describe()
Square.describe()
Circle.describe()


Square.describe()
Triangle.describe()


#polymoorphism = greek word that means to "have many forms or faces"
 # poly = many
 #  morphe = form
 #    TWO WAYS TO ACHIVE POLYMORPHISM
 #    INHERITANCE = An object could be treated of the same type as a parent class
 #     "duck typing" = object must have necessary attributes / methods


#polymorphism = greek word that means to "have many forms or faces

from abc import ABC ,abstractmethod

class shapes:
    @abstractmethod
    def area (self):
        pass

class circle(shapes):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(f"the are of the circle is {3.14*self.radius*self.radius}")

class square(shapes):
    def __init__(self,side):
        self.side=side

    def area(self):
        print(f"the area of square is {self.side*self.side}")
    
    

class triangle(shapes):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        print(f"the area of the triangle is {self.base*self.height/2}")

class pizza(circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)
        

Shapes = [circle(3),square(4),triangle(4,5),pizza("butter",20)]

for shape in Shapes:
    print(f"the shape area is {shape.area()}cm^2")
# duck typing = another way to achieve polymorphism besides inhritance 
# object must have the minimum necessary attributes / methods
# "if it looks a duck and quacks like a duck, it must be a duck . "

class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("woof")

class cat(animal):
    def speak(self):
        print("meow")

class car:
    alive = True
    def speak(self):
        print("honk")

Animals=[dog(),cat(),car()]

for animal in Animals:
    animal.speak()
    print(animal.alive)

# static methods = a method that belong to a class rather than any object from that class (instances) usually used for general utility functions
#
#INSTANCE METHODS =  best for operations on instances of the class (objects)
#
#STATIC METHODS = best for utility functions that do not need access to class data


class employee:

    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def get_info(self):
        return f"{self.name}={self.position}"


    @staticmethod

    def is_valid_poisition(position):
        valid_positions =["manager","cashier","cook","janitor"]

        return position in valid_positions
    
Employee1 = employee("ravi","teacher")
Employee2 = employee("vishwa","cashier")
Employee3 = employee("alifa","janitor")
    
print(employee.is_valid_poisition("doctor"))
print(Employee1.get_info())
print(Employee2.get_info())
print(Employee3.get_info())


#class methods = allow operations related to the class itself take (cls) as the first parameter ,which reports the class itself

class student:
    count = 0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count += 1
        student.total_gpa += gpa

   #  instance method

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f" total # of the students {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count ==0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"
    
Student1 = student("ranjitha",8)

Student2 = student("shilpa",7)

Student3 = student("samruddi",9)


print(student.get_count())
print(student.get_average_gpa())

#magic methods = dunder methods (double  underscore) ,__init__ , __str__ , __eq__,__lt__
#           they are automatically called by many of pythons builtin operations
#           they allow developers to define or custamize the behaviour of objects


class book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self): #string 
        return f"'{self.title}' by {self.author} with page of{self.num_pages}"
    
    def __eq__(self,other):   #equal
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other): #less than
        return self.num_pages < other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key=="title":
            return self.title
        elif key=="author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} not found"
    

Book1 = book("the habbit","jhony",310)
Book2 = book("harry potter","j.k.rolling",223)
Book3 = book("hunter adeline","lewis",590)
Book4 = book("the habbit","jhony",310)


print(Book1)
print(Book1  + Book2)


print("habbit" in Book4)
print(Book3["title"])
print(Book3["author"])
print(Book3["num_pages"])
    
    

#property = decorator used to define a method as a property (it can be accessed like an attribute)
# benefit : add additional logic when read ,write,or delete attributes
# give you getter,setter,and deletor method


class rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height= height

    @property

    def width(self):
        return f"{self._width}cm"
    
    @property

    def height(self):
        return f"{self._height}cm"
    
    @width.setter
    def widtht(self,new_width):
        if new_width > 0:
            self._width = new_width

        else:
            print("width must be greater than zero")

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("height had to be greater than zero")


    @width.deleter
    def widtht(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")



Rectangle = rectangle(12,23)

Rectangle.width = 5
Rectangle.height = 6

del Rectangle.width
del Rectangle.height


print(Rectangle.height)
print(Rectangle.height)

print(Rectangle._width)
print(Rectangle._height)



#decarator function = a function that extends the  behaviour of another function w/o modifying the base function 
#  pass the base function as an arguments to the decorator
#   @add_sprinkles
#   grt_ice_cream("vanilla")


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add a sprinkles🪸")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you add a fudge")
        func(*args, **kwargs)
    return wrapper
    
@add_sprinkles
@add_fudge

def get_ice_cream(flavor):
    print(f"here is your {flavor} icecream🍧")

def get_fudge(cream):
    print(f"here is your fudge {cream}")

get_ice_cream("vanilla")  
get_fudge("chocalate")

# exception = an event that interupts the flow of program
#  (zero division error,type error,value error)
#  1.try, 2.except 3.finally

try:

    number = int(input("enter a number:"))
    print(1/number)

except ZeroDivisionError:

    print("you can't divide by zero !")

except ValueError:
    print("enters only numbers please!")

except Exception:
    print("something went wrong!")

finally:
    print("do some clean up here")


class car:
    def __init__(self,model,name,year,for_sale):
        self.model = model
        self.name = name
        self.year = year
        self.for_sale = for_sale

#methods

    def drive(self):
        print(f"you drive the {self.model}")

    def stop(self):
        print(f"you stop the {self.model}")

    def describe(self):
        print(f"{self.model},{self.name},{self.year},{self.for_sale}")                                                                                                       









    

    









