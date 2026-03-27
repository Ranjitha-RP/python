#function = a block of reusable code 
#place () after the function name to invaoke it
#positional argu

def happy_birthday(name,age):
    print(f"happy birthday to {name} ")
    print(f"you are of {age} ")
    print("again happy birthday to you")
    print()

happy_birthday("bro",30)#number and order of arguments of must be same
happy_birthday("steev",35)
happy_birthday("ranjitha",40)
#when you are calling a function number of arguements and its order should be same

def display_invoice(username,amount,due_date):
    print(f"hello {username}")
    print(f"your bill of {amount:.2f} is due on :{due_date}")

display_invoice("ranjitha",1234.456,"12/4/25")

#return = satatement used to end a function
# and send a result back to the caller 


def add(x,y):
    z=x + y
    return z
 
def substract(x,y):
    z=x - y
    return z

def multiply(x,y):
    z=x * y
    return z
print(add(1,2))
print(substract(1,2))
print(multiply(1,2))

def create_name(first,last):
    first = first.upper()
    last = last.upper()
    return first + " " + last
full_name = create_name("ranjitah","RP")
print(full_name)



#defult arguments = a defult value for certain parameters
# defult is used when that argument is omitted
# make your functions more flexible ,reduces # of arguments
# 1,positional 2.defult 3.keyword 4.arbitary

def net_price(list_price,discount,tax):
#(o)rdef net_price(list_price,discount=0,tax=0.05):
    return list_price * (1- discount) * (1 + tax)
print(net_price(500,0,0.05))

#defult arguments
import time

def count(start,end):
    #def count(start=0,end): if any of the arg is pre difined as a defult it has to after 
    #the non defined func mean def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done")    
count(15,20)


#key word arguments= an arg preceded by an identifier
    # help with readability
    # order of arg doesn't matter

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

hello(greeting="hello",title="mrs.",first="ranjitah",last="rp")
#here order doesn't matter
#hello(title="mrs.",greeting="hello",first="ranjitah",last="rp")this also work

#print('1','2','3','4','5',sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1,area=123,first=456,last=7890)
print(phone_num)

#ARBITARY ARGUEMENTS
#*args = allows you to pass multiple non-keys arguments
#**kwargs =(keyword arguments) allows you to pass muiltiple keyword-arguments
         # *unpacking operator

def add (*args):
    total = 0
    for arg in args:
        total += arg
        return total
print(add(1))

#args

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("ranjitha","naveen","hallo")
    
#kwargs

def print_address(**kwargs):
   #print(type(kwargs))
   for key, value in kwargs.items():
      print(f"{key}:{value}")

print_address(street="123 strret",
            city="banglr",
            state="karnataka",
            )
            

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
    print()
    if "apt"  in kwargs:
        print(f"{kwargs.get("apt")}")
    else:
        print("not present")
    print(f"{kwargs.get("state")}")

    
shipping_label("ranjitha","dr","rayasandra","iit",
               strret="rabbit",
               apt="100",
               city="detol",
               state="karnatak"

            )

    