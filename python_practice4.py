#lists in python
#syntax: my_list=["element1",2,3....]


items=["bru","cfe powder","pen","pencil","book",]
#to remove 1st element 
items.pop(0)
print(items)

#to remove last element
items.pop(-1)
print(items)

#to add something at last
items.append("cup")
print(items)

#to remove something in middle
items.remove("pencil")
print(items)

#to add something in middle
items.insert(3,"keyboard") #here 3 is a index of that element
print(items)

#to remove all the elements from the list
items.clear()
print(items)

#to replace something 
#items[[0]]="naveen"
print(items)

#slicing
items=["pen","pencil",2,3,4,5,6,7,"ranjitha",]
print(items)
items[2:6:1]
print(items)

#sorted
items=[1,2,4,7,6,5,9,0,5,4,3,2]
print(sorted(items))#to write in assending manner
print(sum(items))
print(items.index(1))
print(items.count(4))#how many times it is repeated

#decending order
n=[3,6,8,0,6,4,2,1,6]
sorted_n=print(sorted(n))
print(sorted_n)
#revsorted_n=reverse()
#print(sorted_n)

#nestid list
#[list(list(list))]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1][1]) #[index of 1 st index matrix] [index of element]
print(type(matrix))

#tuples: collection of items but cannot be change the list after creating the touple
#syntax: my_tuple=("element1",:"element2"......)
#if any single element is there in a tuple we had put (,) for that element too
 
genders=("male","female","others")
print(genders)
print(type (genders))
print(len(genders))
print(genders[0])
print(genders[0:3:1])


#tuple concatination(adding)
tuple1=(1,3,4)
tuple2=(2,3,5)
total_tuple=tuple1+tuple2
print(total_tuple)

# tuple repitation(* by astricks symbol)
repeated_tuple=(1,2,3)*7
print(repeated_tuple)

#checking membership

print("apple" in tuple1)
print(1 in tuple1)

#counting

names=("ranjitha","sangeetha","usha","vaishnavi","shravani","thanu","shravani","thanu")
print(names.count("thanu"))
print(names.index("thanu")) # shows the index of 1st occurance of name


#sets in python: collection of unique items of unordered and unindexed
s={1,2,3,4,5,6,7,8,}
print(type(s))
#print(s[5])# set object is not indexed

#to create empty sets
s=set()
print(s)

#set operations
s1={1,2,3,4}
s2={4,3,5,6}
union=(s1|s2) #union operator to add two sets (|)
print(union)
intersection=(s1 & s2)
print(intersection)

difference=(s1-s2)
print(difference)

#symmetric difference
sym_difference_set=s1^s2
print(sym_difference_set)
s={2,3,4,5}
print(s)
s.add(6)
print(s)
s.remove(5)
print(s)
s.discard(10)
print(s)
s.pop()
print(s)
s.clear()
print(s)






