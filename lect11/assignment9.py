# 1 --- Print
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5



i=1
while i<=5:
    j=1
    while j<=i:
        print(j, end=" ")
        j=j+1
    print()
    i=i+1       



# 2 ---Print 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


i=1
while i<=5:
    j=1
    while j<=i:
        print(i, end=" ")
        j=j+1
    print()
    i=i+1       


# 3--- print
#  1
#  2 1 
#  3 2 1
#  4 3 2 1 
#  5 4 3 2 1 

i = 1

while i <= 5:
    j = i
    while j >= 1:
        print(j, end=" ")
        j = j - 1
    print()
    i = i + 1


#  4--- print 
#  5
#  4 4 
#  3 3 3 
#  2 2 2 2 
#  1 1 1 1 1 

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(6 - i, end=" ")
        j = j + 1
    print()
    i = i + 1


# 5--- print
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *    




i = 5

while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i - 1



i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1


# 6--- print
#  1 2 3 4 5
#  1 2 3 4 
#  1 2 3
#  1 2
#  1


i = 5

while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i - 1



# 7--- Print
# 1 
# 2 3
# 4 5 6
# 7 8 9 10

i = 1
num = 1

while i <= 4:
    j = 1
    while j <= i:
        print(num, end=" ")
        num = num + 1
        j = j + 1
    print()
    i = i + 1



# 8--- Print 
# ----*
# ---*-*
# --*-*-*
# -*-*-*-*
# *-*-*-*-*

i = 1
while i <= 5:
    j = 1

    
    while j <= 5 - i:
        print("-", end="")
        j = j + 1

    k = 1

    
    while k <= i:
        print("*", end="")
        if k != i:
            print("-", end="")
        k = k + 1

    print()
    i = i + 1

# 9--- Print
# ----1
# ---121
# --12321
# -1234321
# 123454321



i = 1
while i <= 5:

    j = 1
    while j <= 5 - i:
        print("-", end="")
        j += 1

    k = 1
    while k <= i:
        print(k, end="")
        k += 1

    k = i - 1
    while k >= 1:
        print(k, end="")
        k -= 1

    print()
    i += 1



