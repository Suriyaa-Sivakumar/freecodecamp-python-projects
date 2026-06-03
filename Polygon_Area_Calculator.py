import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        # how many times shape fits inside self (no rotation)
        count_width = self.width // shape.width
        count_height = self.height // shape.height
        return count_width * count_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"
    
rect = Rectangle(10, 5)

print(rect)
print("Area:", rect.get_area())
print("Perimeter:", rect.get_perimeter())
print("Diagonal:", rect.get_diagonal())

print(rect.get_picture())

sq = Square(5)

print(sq)
print("Area:", sq.get_area())

print("Fits inside rectangle:",
      rect.get_amount_inside(sq))