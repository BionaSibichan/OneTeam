# class Animals:
#     def get_name(self,n):
#         self.name=n

# class Dog(Animals):
#     def info(self):
#         print(self.name)

# dg1=Dog()
# dg1.get_name("Cooper")
# dg1.info()

# class Animals:
#     def __init__(self,n):     #init 
#         self.name=n

# class Dog(Animals):
#     def info(self):
#         print(self.name)

# dg1=Dog("Cooper")
# dg1.info()

class Animals:
    def __init__(self,n):     #init 
        self.name=n

class Dog(Animals):
    def __init__(self,n):
        super().__init__(n)   #super
        print(self.name)

dg1=Dog("CoopeR")


