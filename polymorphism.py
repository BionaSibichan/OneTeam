class Animal():
    def sound(self):
        print("makes sound")
class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow meow")

d=Dog()
d.sound()
c=Cat()
c.sound()