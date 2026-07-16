n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

print("Perfect Number" if total == n else "Not a Perfect Number")


for n in range(1, 10001):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print(n, end=" ")