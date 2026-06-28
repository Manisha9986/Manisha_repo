# 1---sum of two numbers

n1=int(input("Enter 1st number to add:"))
n2=int(input("Enter 2nd number to add:"))

sum=n1+n2

print(f"The sum of {n1} and {n2} is {sum}")
print(f"The sum is {sum}")
print(f"The sum of 2 numbers is",sum)

# 2-- Subtraction of two numbers

n3=int(input("Enter 1st num to sub:"))
n4=int(input("Enter 2nd num to sub:"))

Diff=n3-n4

print(f"The diff of two numbers is{Diff}")


# 3--Multiplication of two numbers


n5=int(input("Enter 1st value for mul:"))
n6=int(input("Enter 2nd value for mul:"))

Mul=n5*n6

print(f"The multiplication of 2 numbers is{Mul}")


# 4--Division of two numbers


n7=int(input("Enter value 1 to divide:"))
n8=int(input("Enter value 2 to divide:"))

Div=n7/n8

print(f"The division of 2 numbers is{Div}")


# 5---Modulus of 2 numbers


n9=int(input("Enter 1st for modulus:"))
n10=int(input("Enter 2nd for modulus:"))

Modulus=n9%n10

print(f"The modulus of 2 numbers is {Modulus}")
print(f"The modulus of {n9} and{n10}  is {Modulus}")



# 6---Enter marks of 5 subjects and print percentage and total

a=float(input("Enter marks of English:"))
b=float(input("Enter marks of Hindi :" ))
c=float(input("Enter marks of Maths:" ))
d=float(input("Enter marks of Science:" ))
e=float(input("Enter marks of Social Science:"))

Total=a+b+c+d+e
percentage=(Total/500)*100
 
print(f"The total of 5 subjects is {Total} ")
print(f"percentage is :{percentage}%")




# 7---Swapping two numbers


val1=int(input("Number 1:"))
val2=int(input("Number 2:"))

val1,val2=val2,val1

print (f"val1={val1}")
print (f"val2={val2}")
