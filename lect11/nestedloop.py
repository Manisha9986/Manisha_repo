# When we use loop inside another loop it is nested loop 
 #There are two situatons in loop
# Known and unknown situation
# in known we know how many times loop exexute and in unknown we do not know how many times it 
# execute


# print 2 stars in each row.

i=1
while i<=3:
    j=1
    while j<=2:
        print("*", end=" ")
        j=j+1
    print()
    i=i+1          



#    print stars if it is row 1 print 1 star if row 2 print 2 stars and so on upto 3


i=1
while i<=3:
    j=1
    while j<=i:
        print("*", end=" ")
        j=j+1
    print()
    i=i+1       