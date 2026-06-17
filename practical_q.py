'''#characters count
n=input("Enter the string:")
d={}

for k in n:
    if k in d:
        d[k]=d[k]+1
    else:
        d[k]=1
for m in d:
    print(f"{m}={d[m]}")

'''
#sort
l=int(input("Enter the length:"))
num=[]
for i in range(1,l+1):
    numb=int(input(f"{i}.Enter the number:"))
    num=num+[numb]
n=len(num)
for k in range(n-1):
    for v in range(n-k-1):
        if num[v] > num[v+1]:
            num[v],num[v+1]=num[v+1],num[v]
print(num)

