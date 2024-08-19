
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle
turtle.setup (width=600, height=600)

fred = turtle.Turtle()  

fred.shape('turtle')                    # Set the shape of the turtle to a turtle
fred.speed(2) 

for i in range(5):
    fred.forward(100)
    fred.right(72)