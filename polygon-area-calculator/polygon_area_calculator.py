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
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture_string = ''
        for _ in range(self.height):
            picture_string += ('*'*self.width) + '\n'
        return picture_string
    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, width):
        self.width = width
        self.height = width
    
    def __str__(self):
        return f'Square(side={self.width})'



