#string manipulation
#cancardination
first_name="sangeetha"
last_name="gowda"
full_name= first_name +" " + last_name
print(full_name)

#repitation
#multiple message as to be repeated
message="warning!"*10
print(message)

#string method
message="warning!"
print(message.upper())#convert all letter to caps
print(message.lower())#convert all letter to small

#"strip()" =not give a space between the message
message="warning!"*10
print(message.strip())

#to replace sommething 
print(message.replace("warning","error"))

#length of string
message= "this_is_chandan"
print(len(message))

#accesing string charecter
name = "chandan" 
#  0 1 2 3 4 5 6 (index)
#  c h a n d a n
#  1 2 3 4 5 6 7 (position)
print(name[2]) #[index] where; index=position-1
print(name[2:5]) # 2:5 means in between 2 and 5 letter had be printed
print(name[ :3])# from first to 3rd index i want 

#from back side we count
#1  2  3  4  5  6  7 (position)
#c  h  a  n  d  a  n
#-7 -6 -5 -4 -3 -2 -1 (position)
print(name[-4])

#to find alterante letter
name = "chandan"
print(name[ : :3]) #[:: n] ,n=no of step skip+1

#assighnment operator
x=5
x=x+5
x+=5#add 5 to x
x-=10
x*=10
print(x)

a=10
a+=100
print(a)

a=20
b=40
print(a>b and b>a)#and operator (if the sentance are true :then only output is true,or else 
#it shows false)
print(a==b) #equal to operator
print(a<b)
print(a>b)
print(a!=b)

#logical operator
print(a>b and a<b) #and operator if both crct it shows true else it shows false
print(a>b or a<b) #or operator :if any one statement is true it shows true
print(not(a>b)) #shows opposite to exact answer

#memeber ship operator
s="ranjitha"
print(["c" in s])
print(["r" in s])
print(["s" not in s])
print(["r" in s] and ["p" in s])
print(["r" in s] or ["p" in s])
print(not["r" in s])




