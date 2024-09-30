"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error


# TODO)
#   1. Create a turtle.
fred = turtle.Turtle()
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass
def square():
    for i in range(4):
        fred.forward(100)
        fred.right(90)
def triangle():
    for i in range(3):
        fred.forward(100)
        fred.right(120)
def circle():
    fred.circle(100)
opp = input("What shape do you want to draw, a circle, a triangle, or a square? ")
opp = opp.lower()
if opp == "triangle":
    triangle()
elif opp == "circle":
    circle()
elif opp == "square":
    square()
else:
    print("Check your spelling and/or make sure the shape is one of the options.")        
turtle.exitonclick()