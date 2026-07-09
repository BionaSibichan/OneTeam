# name="Biona"
# for i in name:
#     print(i)
# dic={"name":"Bee","age":21}
# for key,value in dic.items():
#     print()

# i=0
# while (i<7):
#     i+=1
#     print(i)

# i=1
# while i<=7:
#     if i==5:
#         break
#     print(i)
#     i+=1

# i=1
# while i<=9:
#     if i==3:
#         continue
#     i+=1
#     print(i)

# for i in range(1,4):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# n=int(input("Eter"))
# r=1
# for i in range(1,n+1):
#     r*=i
# print(r)

num=int(input("Enter num:"))
is_prime=True
if num<2:
    is_prime=False
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print("Prime")
else:
    print("not prime")