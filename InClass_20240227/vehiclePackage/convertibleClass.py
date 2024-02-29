#convertible Class
from vehiclePackage.Car import Car;       

class Convertible(Car):
    def __init__(self, type, make, model, doors):
        self.doors = doors;
        Car.__init__(self, type, make, model);
        
    def printDoors(self):
        print(self.foors);