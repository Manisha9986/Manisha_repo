# For loop work on sequence of data
# Syntax : for variable in sequence
# Here variable of for loop pick one by one value from sequence

# 1--- Print 1 to 10

numbers =[1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)


# 2--- Print 1 to 10 using ranga function

numbers1=range(1,11,1)
for i in numbers1:
    print(i)


# 3--- Print 10 to 1 

numbers2=range(10,0,-1)
for i in numbers2:
    print(i)


# 4 --- Print root vallues 

numbers3=range (1,11,1)
for i in numbers3:
    print(i*i)


# 5--- Print double of x


numbers4=range(1,11,1)
x=1
for i in numbers4:
    print(x)
    x=x*2


# 6--- Print a  number and print its table

numbers5=range(1,11,1)
num=int(input("Enter a number: "))
for i in numbers5:
    print(f"{num}X{i}={num*i}")


# 7--- Print two star in each row

for i in range(1, 4):
    for j in (1, 3):
        print("*", end=" ")
    print()


# 8--- Print 
# *
# * *
# * * * 
# * * * * 
# * * * * * 

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
 

# 9 --- Enter a number and its factorial

num=int(input("Enter a number: "))
f=1
for i in range (1,num + 1):
    print (f"{i} X", end=" ")
    f=f*i
print(f"\b={f}")


