from abc import abstractmethod,ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def display(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Starting bike")

class Car(Vehicle):
    def start(self):
        print("Car starting")

ob=Bike()
ob.start()
ob=Car()
ob.start()


