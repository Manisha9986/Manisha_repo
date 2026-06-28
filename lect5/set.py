#set

  #set() function
s1=set("Python")
print(s1)

#union()

s2={2,4,2,1,2}
s3={2,5,2,6,7}
print(s2.union(s3))

#intersection()

s2={2,4,2,1,2}
s3={2,5,2,6,7}
print(s2.intersection(s3))

#difference()

s2={2,4,2,1,2}
s3={2,5,2,6,7}
print(s2.difference(s3))


#built in set methods


#add()

set1={"hii","users","of","python"}
set1.add("Welcome")
print(set1)


#update()

set1={"hii","users","of","python"}
set1.update("Welcome coders","developers")
print(set1)


#clear()
set2={1,2,3}
set2.clear()
print(set2)


#copy()

set3=set2.copy()
print(set3)

#discard()

set1.discard("h")
print(set1)         #if we give unexisted value it does not give error

#remove()

set3={3,3,4,5}
set3.remove(5)
print(set3)          #gives error for unexisted value
