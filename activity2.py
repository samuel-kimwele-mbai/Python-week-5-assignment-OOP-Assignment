# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.move()

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Polymorphic behavior
travel(my_car)
travel(my_plane)
travel(my_boat)
