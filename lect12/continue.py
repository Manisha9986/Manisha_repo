# Continue statement transfers the control at the begining of the loop.
# if continue work then the statements below the continue will not be executed.

# print 1 to 10 and skip 5 and 7.

i=0
while i<=10:
    i=i+1
    if ( i==5 or i==7):
        continue
    print(i)