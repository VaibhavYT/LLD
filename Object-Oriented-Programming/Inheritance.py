# Defining the parent class called "Vehicle"
class Vehicle:
    def __init__(self,color) -> None:
        self.color = color

    def honk(self):
        print("Honk honk")

#Defining the child class "Car" that inherits form Vehicle 

class Car(Vehicle):
    def __init__(self, color,speed) -> None:
        super().__init__(color)
        self.speed = speed

    def accelerate(self):
        self.speed +=10 

my_car = Car("Red",40)
my_car.honk()