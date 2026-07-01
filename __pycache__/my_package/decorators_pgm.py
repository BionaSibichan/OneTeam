'''def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

def greet():
    print("Hello, World!")
f=decorator(greet)
f()

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator   #decorator
def greet():
    print("Hello, World!")
greet()
'''
def my_dec(fun):
    def wrapper(a,b):
        if a>b:
            fun(a,b)
        else:
            print("a must be greater than b")
    return wrapper
@my_dec
def divide(a,b):
    print(a/b)
divide(10,5)