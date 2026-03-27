#python compound intrest calculator

principle = 0
rate = 0
time =0

while principle <= 0:
    principle = float(input("enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less  than equal to zero")

while rate <= 0:
    rate = float(input("enter the intrest of rate: "))
    if rate <= 0:
        print("intrest of rate can't be less  than equal to zero")


while time <= 0:
    time = float(input("enter the time: "))
    if time <= 0:
        print("time can't be less  than equal to zero")

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100),time)
print(f"balance after {time} years:{total:.2f}")

principle = 0
rate = 0
time =0

while True:
    principle = float(input("enter the principle amount: "))
    if principle < 0:
        print("principle can't be less  than equal to zero")
    else:
        break
while True:
    rate = float(input("enter the intrest of rate: "))
    if rate < 0:
        print("intrest of rate can't be less  than equal to zero")
    else:
         break

while True:
    time = float(input("enter the time in year: "))
    if time < 0:
        print("time can't be less  than equal to zero")
    else:
         break
print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100),time)
print(f"balance after {time} years:{total:.2f}")
#for loop
#execute the block of code for the fixed number of times

#for example
for x in range (1,11):
    print (x)


for x in reversed (range (1,11)):
    print (x)

print("happy new year")

for x in reversed (range (1,11,2)):
    print (x)

print("happy new year")

credit_card = "234546"

for x in (credit_card):
    print(x)

for x in range(1,21):
    if x == 13:
      break
    else:
       print(x)

for x in range(1,21):
    if x == 13:
      continue
    else:
       print(x)

#count down timer
import time

my_time = int(input("enter the time in sec:"))
for x in range(0,my_time):
    print(x)
    time.sleep(1)
print("time to wake up")


import time

my_time = int(input("enter the time in sec:"))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("time to wake up")

#nested loop
for x in range (3):
    for y in range(1,10):
        print(y,end="")
    print()

rows = int(input("enter the no of rows:"))
columns = int(input("enter the no of columns:"))
symbol = input("enter symbol:")
for x in range (rows):
    for y in range(columns):
        print(symbol,end="")
    print()

 





