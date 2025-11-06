from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sides(self):
        pass
    
    def get_name(self):
        return self.name

class Square(Shape):
    def sides(self):
        return f"{self.name} сторон: 4"

class Triangle(Shape):
    def sides(self):
        return f"{self.name} сторон: 3"

class ShapeFactory:
    @staticmethod
    def new_shape(shape,name):
        if shape == "triangle":
            return(Triangle(name))
        elif shape == "square":
            return(Square(name))
        else:
            print(f"Неизвестная фигура - {shape}")

first_square = ShapeFactory.new_shape("square","Квадрат")
first_triangle = ShapeFactory.new_shape("triangle","Треугольник")

print(f"{first_square.sides()}")
print(f"{first_triangle.sides()}")