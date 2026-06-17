'''count=1
while count<=5:
    print(count)
    count+=1
#fibonacci series
a=0
b=1
count=0
while count<10:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count+=1
#factorial of a number
n=int(input("\nEnter a number:"))
f=1
while n>0:
    f=f*n
    n-=1
print("Factorial:",f)

#break pass continue


while True:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("a+b=",a+b)
    
    elif choice==2:
        print("a-b=",a-b)
        
    elif choice==3:
        print("a*b=",a*b)
        
    elif choice==4:
        print("a/b=",a/b)
        
    else:
        print("Invalid choice")
    print("Do you want to continue? (y/n):")
    ans=input()
    if ans=='n' or ans=='N':
     break

#vowels start print only
a=["Apple","Strawberry","Banana","Avacado","Grapes","Mango","Orange"]
for i in a:
    if i[-1] in "AEIOUaeiou":
        print(i)

#list slicing
a=["Biona","Anas","Apsa","Ebin"]
print(a[0:2])
b=["aba","baba","chapa","dada","lala","papa"]
print(b[0:6:2])'''


