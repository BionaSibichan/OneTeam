'''try:
    a,b=7,0
    print(a/b)
except:
    print("Cant divide")
print("Prgrm executed")
print("----------------------------------")
try:
    a,b=7,5
    print(a/b)
except:
    print("Cant divide")
print("Prgrm executed")
print("----------------------------------")'''
try:
    a,b=10
    print(a/b)
except ZeroDivisionError:
    print("Cant divide")
except TypeError: #divide by zero is not a type error but if we try to divide a string by an integer then it will be a type error
    print("Type error")
except NameError:#if we try to divide a variable which is not defined then it will be a name error
    print("name error") 
except Exception as e: #This will catch all the exceptions and tell us the error occured
    print("error occured",e)
else:
    print("No error occured") #would be executed if there is no error in the try block
finally:
    print("Prgrm executed") #print this statement whether there is an error or not