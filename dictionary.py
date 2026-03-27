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

