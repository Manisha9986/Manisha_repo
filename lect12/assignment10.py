# 1--- Print all prime numbers between 1 to 100

for num in range(1, 101):

    if num < 2:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

print()   

# 2-- Print
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 3--Print
# 1
# 22
# 333
# 4444
# 55555

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()

# 4--Print
# 1
# 21
# 321
# 4321
# 54321

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# 5--Print
# 5
# 44
# 333
# 2222
# 11111

for i in range(5, 0, -1):
    for j in range(6 - i):
        print(i, end="")
    print()

# 6-- Print
# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****


for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 7-- Print
# 12345
# 1234
# 123
# 12
# 1

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
  
# 8-- Print  
# 1
# 23
# 456
# 78910

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()

# 9-- Print
# ----*
# ---*-*
# --*-*-*
# -*-*-*-*
# *-*-*-*-*


for i in range(1, 6):

    for j in range(5,i, - i):
        print(f"-", end="")

    print(f"*", end="")

    for k in range(1, i):
        print(f"-*", end="")
    print()




# 10--  Print
# ----1
# ---121
# --12321
# -1234321
# 123454321


for i in range(1, 6):

   
    for j in range(5 - i):
        print("-", end="")

    
    for j in range(1, i + 1):
        print(j, end="")

    
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
