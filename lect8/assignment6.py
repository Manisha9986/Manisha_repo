#-1---Enter the age of Ram,Shyam and Mohan and print who is the eldest.

ram=int(input("Enter age of Ram : "))
shyam=int(input("Enter age of Shyam : "))
mohan=int(input("Enter age of Mohan : "))

if ram>shyam and ram>mohan:
    print("Ram is eldest")

elif shyam>ram and shyam>mohan:
    print("Shyam is eldest")

elif mohan>shyam and mohan>ram:
    print("Mohan is eldest")

elif mohan==shyam and mohan>ram and shyam>ram:
    print("Mohan and shyam are eldest")

elif mohan==ram and mohan>shyam and ram>shyam:
    print("Mohan and Ram are eldest")  

elif ram==shyam and ram>mohan and shyam>mohan:
    print("Ram and shyam are eldest")          
else:
    print("Equal age of ram,shyam and mohan")




# 2---- Enter a digit & print it in word


digit=int(input("Enter a digit between 0 - 9 : "))

if digit==0:
    print("Zero")

elif digit==1:
    print("One")   

elif digit==2:
    print("Two")       

elif digit==3:
    print("Three")   

elif digit==4:
    print("Four")   

elif digit==5:
    print("Five")   

elif digit==6:
    print("Six")   

elif digit==7:
    print("Seven")   

elif digit==8:
    print("Eight")   

elif digit==9:
    print("Nine")   

elif digit==10:
    print("Ten")   

else:
    print("Invalid digit")   




# 3--- Find biggest between 3 numbers using if-elif-else and logical operators


num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
num3=int(input("Enter 3rd number : "))

if num1>num2 and num1>num3:
    print("1st number is biggest")

elif  num2>num1 and num2>num3:
    print("2nd numberis biggest")  

elif num3>num2 and num3>num1:
    print("3rd number is biggest")   

elif num1==num2 and num1>num3 and num2>num3:
    print("1st and 2nd numbers are biggest")  

elif num2==num3 and num2>num1 and num3>num1:
    print("2nd and 3rd numbers are biggest")      

elif num1==num3 and num1>num2 and num3>num2:
    print("1st and 3rd numbers are biggest")         

else:
    print("All numbers are equal")    




# 4--- Enter working hours of a worker and calculate daily wage as per criteria
#working hours          wage

#    8                  250
#  overtime            
#  8 upto 10            50/- hr
#  10 upto 12           75/- hr
#  12 upto 14           100/- hr

#otherwise: invalid working hours



hours = int(input("Enter working hours: "))

if hours == 8:
    wage = 250
    print("Daily wage =", wage)

elif hours > 8 and hours <= 10:
    wage = 250 + (hours - 8) * 50
    print("Daily wage =", wage)

elif hours > 10 and hours <= 12:
    wage = 250 + (2 * 50) + (hours - 10) * 75
    print("Daily wage =", wage)

elif hours > 12 and hours <= 14:
    wage = 250 + (2 * 50) + (2 * 75) + (hours - 12) * 100
    print("Daily wage =", wage)

else:
    print("Invalid working hours")




#5---- Income Tax Retrun
# slab            Tax
# 0-12 lac        0
# >12 upto 16     5%
# >16 upto 20     10%
# >20 upto 24     15%
# >24             20%

# input income of a person output Tax


income = float(input("Enter income in lakh: "))
tax = 0

if income <= 12:
    tax = 0
elif income <= 16:
    tax = (income - 12) * 100000 * 5 / 100
elif income <= 20:
    tax = (4 * 100000 * 5 / 100) + (income - 16) * 100000 * 10 / 100
elif income <= 24:
    tax = (4 * 100000 * 5 / 100) + (4 * 100000 * 10 / 100) + (income - 20) * 100000 * 15 / 100
else:
    tax = (4 * 100000 * 5 / 100) + (4 * 100000 * 10 / 100) + (4 * 100000 * 15 / 100) + (income - 24) * 100000 * 20 / 100

print("Tax =", tax)
    
