# 1----sub of 2 numbers
n3=9
n4=6
print("subtraction is",n3-n4)

# 2---mul of 3 numbers
n5=5
n6=6
n1=4
print("mul is",n5*n6*n1)

# 3---div of 2 numbers
n7=9
n8=6
print("div is",n7/n8)


# 4---modulus of 2 numbers
n9=2
n10=15
print("modulus is",n9%n10)


# 5---floor division 
n13=2
n14=15
print("floor divison is",n13//n14)


# 6---enter x and y print x power of y=>exponent operator x**y
x=24
y=2
print("exponent is",x**y)


# 7--- Enter marks of 5 subjects and print  total and percentage assume marks out of 100

a=float(input("Enter marks of English:"))
b=float(input("Enter marks of Hindi :" ))
c=float(input("Enter marks of Maths:" ))
d=float(input("Enter marks of Science:" ))
e=float(input("Enter marks of Social Science:"))

Total=a+b+c+d+e
percentage=(Total/500)*100
 
print(f"The total of 5 subjects is {Total} ")
print(f"percentage is :{percentage}%")



# 8--- enter principle, rate and time print simple interest


p=float(input("Enter Principal:"))
r=float(input("Enter Rate:"))
t=float(input("Enter Time:"))

interest=(p*r*t)/100

print(f"Simple interest:{interest}")


 # 9--- enter 2 numbers print their value after Swapping 


val1=int(input("Number 1:"))
val2=int(input("Number 2:"))

val1,val2=val2,val1

print (f"val1={val1}")
print (f"val2={val2}")



# 10--- Enter mrp of book,enter discount percentage also and print discount price and net price

mrp=int(input("Enter mrp of book:"))
dis=int(input("Enter discount %: "))

dp=(mrp*dis)/100
net=mrp-dp

print(f"Discount Price = ",dp)
print(f"Net Price = ",net)



# 11--- Enter basic salary of employee , hra percentage , da percentage ,pf percentage print net salary

salary=int(input("Enter salary of employee: "))
hra=float(input("Enter hra precentage:"))
da=float(input("Enter da precentage: "))
pf=float(input("Enter pf precentage: "))

hra_amt=(salary*hra)/100
da_amt=(salary*da)/100
pf_amt=(salary*pf)/100

net=salary+hra_amt+da_amt-pf_amt

print(f"Net Salary: ",net)



# 12--- enter premium/month of rd accoumt print maturity amount. rd accoumt for 5 years ,min
#premium :5,max=5x?: maturity on 5rs 345.40


month=int(input("Enter monthly premium:"))
maturity=(month/5)*345.40

print(f"Maturity Accoumt = ",maturity)



#13--- Enter child 450/- ,young 650/- old 500/- input number of child , young, old 
# output : fare of childs,youngs,olds than total fare =>


child=int(input("Enter number of childs: "))
young=int(input("Enter number of Youngs: "))
old=int(input("Enter number of olds: "))

child_fare= child*450
young_fare=young*650
old_fare=old*500

Total=child_fare+young_fare+old_fare

print(f"Fare of Childs=",child_fare)
print(f"Fare of youngs=",young_fare)
print(f"Fare of Olds=",old_fare)
print(f"Total fare=",Total)


