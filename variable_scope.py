#variable scope = where a  variable is visible and accesible
#scope resolution = (LEGB) local-> enclosed global -> built in

#local and global variable

def func1():
    a=1    #local variable inside the func and can't accessable outside the func
    print(a)

def func2():
    b=2   #local variable inside the func and can't accessable outside the func
    print(b)
func1()
func2()


def func1():
    a=1    #local variable inside the func and can't accessable outside the func
    print(a)

def func2():
    b=2   #local variable inside the func and can't accessable outside the func
    print(b)
func1() # error cz local function if fixed to that block of code not accessable on other block
func2()


def func1():
       #global variable inside the func and can accessable outside the func
    print(a)

def func2():
  
    print(a)

a=10
func1()
func2()

#built in function
import math

def func1():
    print(math.e)
func1()

#banking 
def show_balance():
    print(f"your balance is {balance:.2f}")

def deposit():
    amount = float(input("enter an amount to be deposited:"))
    if amount < 0:
        print("this is not a valid amount")

    else:
        return amount
    
def withdraw():
    amount = float(input("enter the amount to be withdrawn :"))

    if amount > balance:
        print("insufficient money ")
    elif amount<0:
        print("no amount")
    else:
        return amount
    


balance=0
is_running = True

while is_running:
    print("banking program")
    print("1. show balance")
    print("2.deposit")
    print("3.withdarw")
    print("4.exit")

    choice = input ("enter the choice(1-4):")
        
    if choice == '1':
        show_balance()

    elif choice == '2':
        balance += deposit()
        
    elif choice == '3':
        withdraw()

        
    elif choice == '4':
        is_running=False

    else:
        print("that is not avalid function")
        

print("thank you")

import random
import string

chars = " " + string.punctuation +string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars:{chars}")
print(f"key:{key}")
#ENCRYPT
plain_text = input("enter the message to encrypt :")
cipher_text = ""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text += key[index]
print(f"original message:{plain_text}")
print(f"encrypted message:{cipher_text}")
#DISCRYPT
cipher_text=input("enter the message to encript :")
plain_text = ""


for letter in cipher_text:
    index=key.index(letter)
    plain_text += chars[index]

print(f"encrypted message:{cipher_text}")
print(f"original message:{plain_text}")