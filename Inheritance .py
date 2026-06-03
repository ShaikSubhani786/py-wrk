# Parent class
class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


# Child class
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")


# Creating an object of Car
my_car = Car()

# Calling inherited methods and child method
my_car.start()
my_car.drive()
my_car.stop()