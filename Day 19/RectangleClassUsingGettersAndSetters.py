'''1️⃣ Create the Rectangle class
Name the class Rectangle.
The constructor (_init_) takes width and height.
Store these in private attributes:
__width
__height
2️⃣ Implement Properties
Use the @property decorator to create getters:
width() → Returns the value of __width.
height() → Returns the value of __height.
Use the @<attribute>.setter decorator to create setters:
Validate that the value is greater than or equal to 0.
If it's negative, raise a ValueError with an appropriate message.
3️⃣ Implement the area() method
Returns the area as __width * __height.
4️⃣ Test the Class
Instantiate an object:
rectangle = Rectangle(5, 10)
Call the area() method:
print(rectangle.area())  # Should print 50
Change the dimensions:
rectangle.width = 7
rectangle.height = 3
print(rectangle.area())  # Should print 21
Try setting a negative value:
rectangle.width = -5  # Should raise a ValueError'''
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width cannot be negative.")
    @property
    def height(self):
        return self.__height
    @width.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Height cannot be negative.")
    def area(self):
        return self.width * self.height
    
rectangle = Rectangle(5, 10)
print(rectangle.area())
rectangle.width = 7
rectangle.height = 3
print(rectangle.area()) 
rectangle.width = -5
