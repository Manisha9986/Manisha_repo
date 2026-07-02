# Break statement transfers the control outside the loop.
# Cause of break in the loop become un natural death of the loop
# Break terminate the loop in emergency.

# Enter a numbers check is it prime or not.

# Prime numbers = numbers divide by itself or 1.

num = int(input("Enter a number: "))
i=2
while i<num:
    if num % i == 0:
        break
    i=i+1
if (i==num):
    print(num,"is prime number")
else:
    print(num,"is not prime number")
