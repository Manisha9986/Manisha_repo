# 1----Enter a number and print sum of its digits

num=int(input("Enter the number:"))

x=0
while num>0:
    x=x+num%10
    num=num//10
print(f"Total sum of digits",x)



# 2---- Enter a number and print its reverse

num1=int(input("Enter a number:"))
x=0
while num1>0:
    x=x*10+num1%10
    num1=num1//10
print(f"Reverse of digits is",x)    



# 3---- Enter a number and check whether it is palindrome or not

num2=int(input("Enter number:"))
x=0
temp=num2
while num2>0:
    x=x*10+num2%10
    num2=num2//10
if temp==x:
        print(temp,"is palindrome")
else:
        print(temp,"is not palindrome")


# 4---- Enter a number and check is it armstrong or not

num3=int(input("Enter number to check armstrong:"))

x=0
temp=num3
d=0
while num3>0:
      d=num3%10
      x=x+d**3
      num3=num3//10
if temp==x:
      print(f"{x}is an armstrong number")      
else:      
      print(f"{x}is not an armstrong number")      



# 5---- Enter a number and print it in word
      
num4 = int(input("Enter a number: "))

d = 0
x = 0


while num4 > 0:
    x = x * 10 + num4 % 10
    num4 = num4 // 10

while x > 0:
    d = x % 10

    if d == 0:
        print("Zero")
    elif d == 1:
        print("One")
    elif d == 2:
        print("Two")
    elif d == 3:
        print("Three")
    elif d == 4:
        print("Four")
    elif d == 5:
        print("Five")
    elif d == 6:
        print("Six")
    elif d == 7:
        print("Seven")
    elif d == 8:
        print("Eight")
    elif d == 9:
        print("Nine")

    x = x // 10

        





