
class Car():
    def Distance(self):
        print('Distance with 4 wheels')

class Motorcycle():
    def Distance(self):
        print('Distance with 2 wheels')

class Truck():
    def Distance(self):
        print('Distance with 6 wheels')


def Distance_Vehicle(vehicle):
    vehicle.Distance()

My_vehicle = Motorcycle()

Distance_Vehicle(My_vehicle)