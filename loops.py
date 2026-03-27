pin="123"
trials=0
while trials<=3:
    input_pin=input(f"trial{trials}|pin>>")
    trials+=1
    if input_pin==pin:
        print("correct")
        break
    else:
        print("incorrect")

#loops 
#for loop (range)
#syntax:for element in collection /for this in this

i=1
while i<=10:
    print(i,end=" ")
    i+=1
    #or
for i in range(1,10):
    print(i,end=" ")

bag=("green","orange","violet")
for ball in bag:
    print(ball)

#for i in range(start,stop,step)
#iterables:an object/collection that can return its elements 
# one at a time ,allowing it to be iterated over in a loop

numbers = [1,2,3,4,5,6,7,8,9]
for number in reversed(numbers):
    print(number,end = " ")
print()

numbers = (1,2,3,4,5,6,7,8,9)
for number in reversed(numbers):
    print(number,end = " ")
print()

#set

fruits = {"apple","mango","pineapple","guva","orange"}
for fruit in (fruits):
    print(fruit,end=" ")
print()

name = "ranjitha"
for charecter in name:
    print(charecter, end =" ")
print()

my_dict = {"A":1,"B":2,"C":3}
for key , value in my_dict.items():
    print(key,value)
print()
for  value in my_dict.values():
    print(value)
for key  in my_dict.keys():
    print(key)
for key , value in my_dict.items():
    print(f"{key} = {value}")

#membership operator = used to test whether a value or variable
#  is found in a sequence
#   (string,list,tuple,set,or dictionary)it works same for list,tuple,set
  #1.in 2.not in

word = "apple"
letter = input ("guess a letter in the secret word:")
if letter not in word:
    print(f"this letter {letter} not in  {word}")
else:
    print(f"{letter} was  found")

students = {"ranjitha","naveen","sinchana"}

student = input("enter the name of the student:")

if student in students:

    print(f"{student} is there in {students}")
else:

   print(f"{student} is nor there in {students}")

grades = {
    "ranjitha":"a",
    "naveen":"b",
    "prakash":"c",
    }
student = input("enter the name of a student:")
if student in grades:
    print(f"{student} present in {grades}")
else:
     print(f"{student}  not present in {grades}")


#list comprahension = a concise way to create lists in python
# compact and easier to read than traditional loops
#[expression for value in iterable if condition

#double = [expression for value in iterable if condition]

double = [x*2 for x in range(1,12)]

print(double)

fruits = ["apple","mango","pineapple","guva","orange"]
fruits1=[fruit.upper() for fruit in fruits]
print(fruits1)
fruits1_chargs=[fruit[0] for fruit in fruits]
print(fruits1_chargs)

numbers = [-1,-2,3,-4,5,-6]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num >= 0]
even_num = [num for num in numbers if num %2 == 0]
print(positive_num)
print(negative_num)
print(even_num)

grades = [85,43,56,78,89,]
passing_grades = [grade for grade in grades if grade >=60]
print(passing_grades)
for i in range (1,50,2):
    print(i,end=" ")
    

name="chandan"
for alphabets in name:
    print(alphabets*2)

name="chandan"
for index,letters in enumerate(name):
    print(letters*(index+1))

l=[1,2,3,4,5,6,7,8,9]
for num,index in enumerate(l):
    print(f"{num} in {index}th index")

l=[1,2,3,4,5,6,7,8,9]
for num in l:
 print(num)
 if num==9:
   break
 else:
   print("all printed")

#by using dictionaries
d={"name":"ranjitha","age":"18","income":0 }
for keys,values in d.items():#.items() because to convert dictionares to tuple
    print(keys,values)

#nested loop
for i in range(1,11):
    print(f"2*{i}={2*i}")

for j in range(1,11):
 for i in range(1,11):
    print(f"{j}*{i}={j*i}")

#comprahension \list input \loop construction
l=[1,23,34,56,67,78]
total=0
for num in l:
  total=num+total
  print(total)

#for doubling the number
l=[1,23,34,45,56,67]
double=[]
for num in l:
   double.append(num*2)
print(double)

l=[1,23,34,45,56,67,78]
double=[]
for num in l:
    double.append(num**2)
    print(double)


#looping through dictionaries
students=["ranjitha","naveen","priya"]
marks=[50,30,49]
student_marks={}
for index,student in enumerate(students):
    student_marks[student]=marks[index]
    print(student_marks)

students=["ranjitha","naveen","tharun"]
marks=[23,34,45]
students_marks={}
for i in range(len(students)):
    students_marks[students[i]]=marks[i]
    print(students_marks)

students_marks={'ranjitha': 23, 'naveen': 34, 'tharun': 45}
for keys,values in students_marks.items():
    print(f"{keys}={values}")

l=[11,2,3,34,4,45,4,5]
double=[num*2 for num in l]
print(double)

l=[1,2,3,4,5,6]
dl=[num**2 for num in l]
print(dl)

l=[x*2 for x in range(1,20)]
print(l)

l=[x*2%2==0 for x in range(1,20)]
print(l)

#to get even numbers
edl=[x**2 for x in range(1,20)if x%2==0]
print(edl)

l=["chandan","naveen"]
cl=[x[1] for x in l]
print(cl)

#dictionaries comprahensions
city_population={
    "banglr":23,
    "mysore":24,
    "udupi":34,
    "mnglr":39,
}

lc={keys:values for keys, values in city_population.items()}
print(lc)

city_population={
    "banglr":23,
    "mysore":24,
    "udupi":34,
    "mnglr":39,
}

lc={keys:values for keys, values in city_population.items() if values>60 }
print(lc)

#splitting list and taking user input to list
s="this is a computer"
l=s.split()
print(l)

#taking a user input to list
print("list input practice")
x=input("enter list of integers:")
print(x)
l=x.split()
print(l)
#or
x=input("enter the integers:").split()
print(x)
l=[int(num) for num in x]
print(l)


#shoping of cart
item = input("what item would you like:")
price = float(input("what is the price of that item:"))
quantaty = float(input("the quantity of items that you bought:"))
total = price * quantaty

print(f"you have bought {quantaty} x {item}\n")
print(f"your total is:{total} ")

#circumfurance of a circle
import math

radius = float(input("enter the value of radius:"))

circumferance = 2 * math.pi * radius
print(f"the circumferance is: {circumferance}")

#area of a circle
import math
radius = float(input("enter the value of radius:"))
area = math.pi * pow(radius,2)
print(f"the area  is: {area}")

#hypotenious
import math
a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))

c = math.sqrt(pow(a,2) + pow(b,2))
print(f"side={c}")

#python calculator
operator = input("enter the operator(+,-,*,/):")
a = float(input("the value of a:"))
b = float(input("the value of b:"))

if operator== "+":
    result= a+b
    print(round(result))
elif operator== "-":
    result= a-b
    print(round(result))
elif operator== "*":
    result= a*b
    print(round(result))
elif operator== "/":
    result= a/b
    print(round(result ,3 ))#mean round after 3 digit of the point
else :
    print("input error")
import math
weight = float(input("enter your weight:"))
unit = input("kilogram or pounds(k/l):")
    
if unit == "k":
    weight = weight * 2.205
    print(weight)
elif unit == "l":
    weight = weight / 2.205
    print(weight)

else :
    print("f{unit} was not valid")

#temperature conversion
unit = input("is this temperature is in celcius/faranite(c/f): ")
temp = float(input("enter the temperature value: "))
if unit == "c":
    temp = round((temp*9/5 + 32),1)
    print(temp)
elif unit == "f":
    temp = round((5/9*(temp-3)),1) 
    print(temp)
else :
   print(f"{unit} is an invalid measurement")

#valid user input exercise
username = input("enter the username:")

if len(username) > 12:
   print("your username contain more than 12 letters")

elif not username.find(" ") == -1:
   print("your username can't contain spoaces")
else:
   print(f"welcome {username}")