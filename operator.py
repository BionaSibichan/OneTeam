"""
1.Arthmetic Operators
a=2
b=5

print(a+b) #addition
print(a-b)
print(a*b)
print(a/b)
print(b/a)
print(a//b)
print(a**2)
print(b%a)

2.Assignment Operators
a=10
a+=5
print(a)
a=7
a-=5
print(a)
a*=5
print(a)
a//=5
print(a)


3.Comparison Operators
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=8)
print(a<=12)

4.Logical Operators
a=10
b=5
print(a>5 and b<10)
print(a>5 or b>10)
print(not(a>5 and b<10))

5.membership operators
string="hahaha"
print("h" in string)
print("z" in string)
print("h" not in string)

string -->mutable
list -->mutable
tuple -->immutable
set -->mutable
"""

#6.identity operators

a=[7,5,"woww",[6,9],14]
b=[7,5,"woww",[6,9],14]
c=[1,2,3]
d=c
e="Anzo"
f="Anzo"
print(a is b)
print(a is not b)
print(c is d)
print(e is f)

