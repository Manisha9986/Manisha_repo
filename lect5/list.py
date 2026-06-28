#list


items=["computer","laptop","mobile"]
print(items[2])

#operations

# concatenate

l1=[2,4,3]
l2=[4,3,2]

l3=l1+l2
print(l3)

#repetition

print(l1*5)


#slice[]

print(l1[1])

#range slice[:]

print(l3[3:7])


#in

print(4 in l1)

#not in

print(9 in l1)



#built in methods


#len()

name=["Manisha","Khushi","Nishita"]
print(len(name))
print(max(name))


#max()

num=[4,9,1]
print(max(num))


#min()

print(min(num))


#append

l4=["java","python"]
l4.append("C")
print(l4)

#insert

l4.insert(0,"C++")
print(l4)

#remove

l4.remove("C")
print(l4)


#pop

l4.pop()
print(l4)


#reverse

l4.reverse()
print(l4)

#sort()

num.sort()
print(num)

#sort(reverse=True)

num.sort(reverse=True)
print(num)


#tuple or string into list

t2=(2,3,4,5)
list(t2)
print(t2)

s1="hello"
list(s1)
print(s1)

#string and tuple into list

t1=(9,4,3,2)
tuple(t1)
print(t1)


s2="users"
tuple(s2)
print(s2)