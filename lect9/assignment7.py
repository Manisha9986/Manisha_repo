# 1--- Print 1 to 10

i=1
while i<=10:
    print(i)
    i=i+1


# 2--- Print 10 to 1 (Reverse)

i=10
while i>=1:
    print(i)
    i=i-1


# 3--- Print 1,4,9,16,25,36,49,64,81,100
i=1
while i<=10:
    print(i*i)
    i=i+1


# 4--- Print 1,2,4,8,16,32,64,128,256,512

i=1
while i<=512:
    print(i)
    i=i*2


# 5--- Enter a number & print its  table

num=int(input("Enter a number: "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

    
# 6--- Enter a number & print sum of all natural numbers upto it

num1=int(input("Enter the number : "))
i=1
sum=0

while i<=num1:
    sum=sum+i
    i=i+1
    print("Sum=",sum)


# 7--- Enter a number & prints its factorial

num2=int(input("Enter number: "))
fact=1
i=1
 
while i<=num2:
    fact=fact*i
    i=i+1
    print("Factorial=",fact)


# 8--- Enter m and n print product of m,n items

m=int(input("Enter m: "))
n=int(input("Enter n: "))

product=1
i=1

while i<=n:
    product=product*m
    i=i+1
    print("Product= ",product)


# 9--- Print all even nos.upto 100

i=2
while i<=100:
    print(i)
    i=i+2


# 10--- Print all odd nos. upto 50

i=1
while i<=50:
    print(i)
    i=i+2

# 11--- Take input of 2 numbers and print sum everytime until user want to exit 

ch="yes"

while ch=="yes":
    a=int(input("Enter value of A = "))
    b=int(input("Enter value of B = "))

    print("Sum=" ,a+b)

    ch=input("Do you want to continue? (yes/no): ")