import simple_draw as sd
from .roof import triangle
from .wall import wall


def full_house(x, y):
    wall(x, y)
    triangle(x - 50, y + 300, 0, 550, 5)
