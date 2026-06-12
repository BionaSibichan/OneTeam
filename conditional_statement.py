'''age=int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
if age<18:
    print("Child")
elif age>=18 and age<30:
    print("Adult")
elif age>=30 and age<60:
    print("Senior Citizen")
else:
    print("Super Senior Citizen")

num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")'''

a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
choice=int(input("Enter your choice: "))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:     
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("Invalid choice")