#---nested if-else:
   #when we use an if else statement in another if else statement

# example

#enter age of a person & check LIC eligibility as per following criteria
#age should be 18 - 45

age=int(input("Enter an age:"))

if age>18:
    if age<45:
       print("You are eligible")
    else:
        print("Not eligible")
else:
    print("Not eligible for LIC")



#----Logical operators used to combine two or more than two relations and give the result 
# either true or false 

#Logical and
#Logical or
#Logical not

#the above program can be simplified by logical operators

age1=int(input("Enter an age:"))

if age1>18 and age1<45:
       print("You are eligible")
else:
        print("Not eligible")




#----if-elif-else is used for many conditions

#example
#Enter the day of the week and print name of the day

day=int(input("Enter day of week between 1-7 : "))

if day==1:
     print("Monday")

elif day==2:
     print("Tuesday")

elif day==3:
     print("Wednesday") 

elif day==4:
     print("Thrusday")  

elif day==5:
     print("Friday")  

elif day==6:
     print("Saturday")  

elif day==7:
     print("Sunday")  

else:
     print("Enter invalid week day")  


#----- Ternary operations

   #syntax---  expression1 if condition else expression2

#Enter biggest of 2 numbers

a=int(input("Enter number a :"))
b=int(input("Enter number b :"))

print("A is greater") if a>b else print("B is greater") 
