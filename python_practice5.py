#dictionary: collection of keyu value pairs ,mutable,unordered

birthday={
    "ranjitha":"17-08-2007",
    "naveen":"28-10-2014",
    "virat":"5-10-1988",
}
print(birthday)

#accessing dictionary elements
print(birthday.get("prakash","not found"))

#or we can use get() function to access the value
print(birthday.get("naveen"))
print(birthday.get("naveen","not found"))

#adding data to dictionary

print(birthday)
birthday["sudeep"]="02-09-1973"
print(birthday)

#updating to dictionary or modify
print(birthday)
birthday["naveen"]="29-10-2012" #updated "28-10-2014" to "29-10-2012" 
print(birthday)

# to remove an element from dictionary
print(birthday)
birthday.pop("ranjitha")
print(birthday)
#or
del birthday["naveen"]
print(birthday)
#or
print(birthday)
x = birthday.pop("virat")
print(x)

#birthday.clear()

print(birthday.keys())
print(birthday.values())

#items: returns key value pairs as tuple
print(birthday.items())

#updating th dictionary with another dict
new_birthday={"shobha":"12-10-1997"}
birthday.update(new_birthday)
print(birthday)

#randomly we can do dict also
d={
    123:"number",
    (1) : "fav num",
    "f":"fav alphabet"

}
print(d)
#note : but cannot do lists in dictionary 

#creating dictionary in manual usage of items

item1={
    "name":"sugar",
    "weight":2,
    "price": 120,
}

item2={
    "name":"milk",
    "weight": 1,
    "price": 35
}

item3={
    "name":"egg",
    "weight": 25,
    "price": 35
}

items=[item1,item2,item3]
print(items)

print(f"weight is:{item1["weight"]+item2["weight"]+item3["weight"]} kg")

weeks={
    "monday":17,
    "tuesday":18,
    "wednesday":19.
}
print(weeks)
new_weeks={
    "thursady":20,
}
weeks.update(new_weeks)
print(weeks)

#decision making :if and else condition and elif condition
x=23
if x%2==0:
    print("x is even")

else:
    print("x is odd")

signal=input("the clr is:")

if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
elif signal=="green":
    print("go")
else:
    print("go")

#logical operator
attendance=75
is_a_teacher_friend=True
if attendance>=75 or is_a_teacher_friend:
    print("attend exam")
else:
    print("no exam")

#nested if condition
gender=input("gender is:")
age = int(input("age is:"))

if gender=="female":
    print("ticket free")
else:
    if age < 5:
         print("child discount")
    elif age<=12:
         print("half ticket")
    elif age>=60:
         print("senio citizen")
    else:
        print("pay full ticket")
        
#match_case statement (switch) : an alternative to using many 
#"elif" statements execute some codes if a value matches a "case"
# benifits:cleaner and syntax is more readable

def day_of_week(day):
    if day == 1:
        return "it is sunday"
    elif day ==2:
        return "it is monday"
    elif day ==3:
        return "it is tuesday"
    elif day ==4:
        return "it is wednesday"
    elif day ==5:
        return "it is thursday"
    elif day ==6:
        return "it is friday"
    elif day ==7:
        return "it is saturday"
    else:
        print("not a valid day")

print(day_of_week(2))

#or 

def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case _:
            print("not a valid day")

print(day_of_week(5))

def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case "tuesday":
            return False
        case "wednesday":
            return False
        case "thursady":
            return False
        case "friday":
            return False
        case "saturady":
            return True
        case _:
            return False

print(is_weekend("sunday"))


#or


def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday"  | "wednesday" |"thursday" |"friday":
            return False
        case _:
            return False
print(is_weekend("sunday"))
#collection = single variable used to store in multiple value
#list = []ordered and changeble,can beduplicated
# set={}unorderd and immutable ,but can be added and remove elements,no duplication
# tupole = () ordered ammd unchangeble,duplicates ok and faster
fruits = ['apple','banana','orange','guva','guva']
#print(dir(fruits))
 #print(help(fruits))

#print(fruits.count("guva"))
foods = []
prices = []
total = 0
while True:
    food = input("enter the food to buy(q to quit):") 
    if food.lower() == "q":
        break
    else:
        price=float(input(f"enter the price of {food}:"))
        foods.append(food)
        prices.append(price)
print("---your cart---")

for food in foods:
    print(food,end=" ")
for price in prices:
    #print(prices,end=" ")
    total += price
print(f"total is:{total}")

#2d list
fruits = ['apple','banana','orange']
veg = ['tomato','garlic','onion']
meat = ['chicken','fish','pig']
groceries = [fruits,veg,meat]
print(groceries[1][2])

groceries = [
['apple','banana','orange'],
['tomato','garlic','onion'],
['chicken','fish','pig']]

print(groceries[1][2])

for collection in groceries:
    for food in collection:
     print(food,end=" ")
    print()

 #2d key
numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ('*',0,"#"))  
for row in numpad:
    for num in row:
        print(num,end=" ")
    print()

