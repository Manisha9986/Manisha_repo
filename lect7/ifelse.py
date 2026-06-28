"Decision control instruction:"
"As we know a problem cannot be solved without decision so to take decision in python "
"we use if-else statement"

"Syntax :"

# if(condition):
#     statement1
#     statement2
# else:
#     statement1
#     statement2    


#condition is when someone buy a book of mrp more than 500 give 10% discount and 
# if someone buy less than 500 give 5% discount
 
mrp=float(input("Enter mrp of book:"))

dis=0
net=0

if mrp>=500:
    dis=mrp*10/100
    net=mrp-dis
    print(f"mrp= {mrp},dis= {dis},net= {net}")

else:
    dis=mrp*5/100
    net=mrp-dis
    print(f"mrp= {mrp},dis= {dis},net= {net}")

