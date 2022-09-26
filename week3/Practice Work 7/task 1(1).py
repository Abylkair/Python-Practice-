from collections import namedtuple
from math import sqrt, pi
 
# Side lengths
Triangle = namedtuple("Triangle", "a b c")
 
# Length and height of the top and bottom
Trapezoid = namedtuple("Trapezoid", "a b h")
 
# One half of the major and minor axes of the ellipse
Ellipse = namedtuple("Ellipse", "a b")
 
def triangle_area(triangle):

    p = (triangle.a + triangle.b + triangle.c) / 2
    return sqrt(p * (p - triangle.a) * (p - triangle.b) * (p - triangle.c))
 
 
def trapezoid_area(trapezoid):
    return (trapezoid.a + trapezoid.b) * trapezoid.h / 2
 
 
def ellipse_area(ellipse):
    return pi * ellipse.a * ellipse.b
 
 
def input_triangle():
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    return Triangle(float(a), float(b), float(c))
 
 
def input_trapezoid():
    a = input("a = ")
    b = input("b = ")
    h = input("h = ")
    return Trapezoid(float(a), float(b), float(h))
 
 
def input_ellipse():
    a = input("a = ")
    b = input("b = ")
    return Ellipse(float(a), float(b))
 
inputs = {1: input_triangle, 2: input_trapezoid, 3: input_ellipse}
areas = {1: triangle_area, 2: trapezoid_area, 3: ellipse_area}
 
def calculate_area():
    figure_number = int(input("Input 1 to the select triangle, 2 - trapezoid, 3 - ellipse:"))
    figure = inputs[figure_number]()
    area = areas[figure_number](figure)
    print(str.format("{0} area is {1}", figure, area))
 
 
def main():
    while True:
        try:
            calculate_area()
        except Exception as e:
            print(e)
            print("Exit")
            break
 
main()