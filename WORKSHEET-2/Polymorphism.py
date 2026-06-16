# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Accepting input from the user
radius = float(input("Enter the radius of the circle: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Creating objects
circle = Circle(radius)
rectangle = Rectangle(length, width)

# Displaying areas
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())