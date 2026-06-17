'''
for k in "Biona":
    print(k)
for k in {"Name":"Biona","Age":20}:
    print(k)
for i in range(5):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(10,0,-1):
    print(i)
#fibonacci series
a=0
b=1
for i in range(10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c '''
#multiplication table
print("Multiplication Table")
n=int(input("Enter a number:"))
for i in range(1,7):
    print(n,"x",i,"=",n*i)#print(f"{n} x {i} = {n*i}")
