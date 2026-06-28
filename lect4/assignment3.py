"Data types decides which type of data a variable can hold"

#---Data types

a=1234  #int
b=3.45  #float
c="String"  #string   immutable
d=6+4j  #complex
e=[1,2,3,4]  #list    mutable
f=(5,6,7,8)  #tuple    immutable
g={"name":["manisha","abc"],"age":17} #dictionary     mutable
h={5,6,6,6,7,8}   #sets are mutable but its elements are immutable

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

 

 # mutable and immutable 

# str="Hello"
# str[1]=a
# print(str)    not allowed


list=[1,2,3,4]
list[1]=5
print(list)  #allowed


# arithmetic operations

#add
n1=5
n2=6
print("addition is",n1+n2)

#sub
n3=9
n4=6
print("subtraction is",n3-n4)

#mul
n5=5
n6=6
print("mul is",n5*n6)

#div
n7=9
n8=6
print("div is",n7/n8)


#modulus
n9=2
n10=15
print("modulus is",n9%n10)

#exponemt
n11=24
n12=2
print("exponent is",n11**n12)

#floor division
n13=2
n14=15
print("floor divison is",n13//n14)



#---- escape sequence

h1="Bell\asound"
i="Bell\bsound" #bel sound ouput one l backspace
j="Bell\fsound" #next line with space
k="Bell\nsound" #next line
l="\101"        #octal
m="Bell\tsound" #tab space
n="\x16"        #hexadecimal

print(h1)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)

"operator is special symbol which is used to operates on data & the data on which operator "
"operates is called operands"

"classification of operators"
"unary,binary,ternary"

#----string operations

   #-- concatenate(+)

o="Hello "
p="users" 

print(o+p)

  #---multiple copies(*)

q="Hii"
print(q*3)


  #---returns character of that value

print(q[2])  


  #---slicing

r="i am a python learner"
print(r[7:13])  

  
  # ---in (if character in true comes)


print("am" in r) 


  # --- not in

print("python" not in r) 


  
#conversion in str


str=(12.4)
print(type(str))



#---bulit in string methods

  #--capitalize()

s="hello i am a python developer"
print(s.capitalize())

  #---upper()

print(s.upper())


  #---lower()

print(s.lower())

  #---title() gives capital letter of each word

print(s.title())


  #---find()  if not -1 returns

print(s.find("developer"))


  #---count()

print(s.count("a"))

  #---isalpha()   if space so it is false

print(s.isalpha())

  #---isdigit()   if all are character it is true

print(s.isdigit())


  #---islower()  if all are lower it is true

print(s.islower())

  #---isupper()  if all are upper it is true

print(s.isupper())  




