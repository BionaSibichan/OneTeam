def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

add(7,12,3)

def greet(**kwargs):
    print(f'Hello {kwargs["name"]} you are {kwargs["age"]} years old')
greet(name="Anas",age=26,place="Kottayam")
#return
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

s=add(7,12,3)
print(s)
# recursive
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(7))

#fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

#lambda

add=lambda a,b:a+b
print(add(7,16))

is_even=lambda num:num%2==0
print(is_even(7))