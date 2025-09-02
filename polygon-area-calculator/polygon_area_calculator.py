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
        return self.width * 2 + self.height * 2
    def get_diagonal(self):
        # (width ** 2 + height ** 2) ** .5
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        for _ in range(self.height):
            print('*'*self.width + '\n')
    def get_amount_inside(self, other):
        return self.get_area() / other.get_area()
    def __str__(self):
        # Should look like 'Rectangle(width=5, height=10)'
        # Wonder if I could use {type(self)} for Rectangle
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    pass
