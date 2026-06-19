# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Subclass Dog
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Subclass Cat
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
dog = Dog()
cat = Cat()

# Calling overridden methods
dog.sound()
cat.sound()