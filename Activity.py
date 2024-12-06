class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move method.")
class Car(Vehicle):
    def move(self):
        return "Driving..."
class Plane(Vehicle):
    def move(self):
        return "Flying..."
class Ship(Vehicle):
    def move(self):
        return "Sailing..."
vehicles = [Car(), Plane(), Ship()]
for vehicle in vehicles:
    print(vehicle.move())
