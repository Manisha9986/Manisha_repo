# 1--- Enter sale price and cost price of a product & calculate profit or loss

sale_price=float(input("Enter sale price of product:"))
cost_price=float(input("Enter cost price of product:"))

if sale_price>cost_price:
    profit=sale_price - cost_price
    print(f"Profit = ",profit)
elif sale_price<cost_price:
    loss=cost_price - sale_price
    print(f"Loss = ",loss)
else:
    print(f"No profit , No loss")    




# 2----Enter 2 numbers and print which one is greater


n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

if n1>n2:
    print(n1, "is greater")
elif n1<n2:
    print(n2, "is greater")
else:
    print( "Both numbers are equal")        



# 3--- Enter a number and check is it even or odd


num=int(input("Enter number:"))


if num%2==0:
    print(num ,"is even")

else:
    print(num,"is odd")    



# 4--- Enter a number and check is it positive or negative


number=int(input("Enter the number:"))

if number>0:
    print(number,"is positive")

elif number<0:
    print(number,"is negative")

else:
    print("Zero")        



# 5--- Enter marks of 5 subjects & calculate total and percentage .Print pass or fail if
#percentage is greater than 40 then pass


marks1=int(input("Enter marks of Hindi: "))
marks2=int(input("Enter marks of English: "))
marks3=int(input("Enter marks of Maths: "))
marks4=int(input("Enter marks of Punjabi: "))
marks5=int(input("Enter marks of Science: "))

Total=marks1+marks2+marks3+marks4+marks5

percentage=Total/5

print(f"Total marks=",Total)
print(f"Percentage=",percentage)

if percentage>=40:
    print("Pass")
else:
    print("Fail")



#6----enter basic salary of employee and calculate net salary.
#Rule: if basic salary is less than 10000 then HRA=10% of basic, DA=90% of basic
# if basic salary is greater than 10000 then HRA=20% of basic, DA=95% of basic



basic_salary=int(input("Enter Basic salary of employee: "))

if basic_salary<10000:
    hra=basic_salary*10/100
    da=basic_salary*90/100

else:
    hra=basic_salary*20/100
    da=basic_salary*95/100


net_salary=basic_salary+hra+da

print("HRA=",hra)
print("DA=",da)
print("Net salary=",net_salary)


