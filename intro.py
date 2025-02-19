"""
This Turtle Graphics program creates a boat sailing on water with the sun in the background. The program makes use of turtle graphics drawing techniques, including shapes, colors, and positioning.

How It Works:
    Boat Deck – Draws the main hull of the boat using a filled polygon.
    Boat Mast – Draws the vertical stick in the center of the boat.
    Boat Sails – Creates two white triangular sails attached to the mast.
    Boat Windows – Draws three circular windows on the boat.
    Sun – Draws a yellow circle in the sky and adds sun rays around it.
    Water – Creates a blue rectangle at the bottom to represent water.
    Title Text – Displays the game title "Sink The Invaders!" in bold Cooper Black font.
How to Run:
    Run the script in any Python environment that supports turtle.
    The window will open, and the boat with the sun and water will be drawn step by step.
    The title "Sink The Invaders!" is displayed at the end.
This program is useful for game intros, graphical projects, or learning basic drawing techniques with Python Turtle. 
"""

import turtle

t=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor("SkyBlue1")#Background Color

#Draw the deck of the boat
t.color("chocolate","orange")
t.penup()
t.goto(-100,-150)
t.begin_fill()
t.pendown()
t.forward(200)
t.left(60)
t.forward(80)
t.setheading(180)
t.forward(280)
t.left(120)
t.forward(80)
t.end_fill()
t.backward(80)
t.setheading(0)
t.forward(140)
t.left(90)

#Draw the stick of the boat
t.pensize(8)
t.forward(125)
t.backward(5)
t.penup()

#draw the white left wings of the boat
t.pensize(2)
t.pendown()
t.left(130)
t.forward(4)
t.color("white")
t.begin_fill()
t.forward(165)
t.setheading(0)
t.forward(125)
t.end_fill()
t.penup()
t.left(90)
t.forward(108)
t.right(90)
t.forward(7)

#draw the right white wing of the boat
t.pensize(2)
t.pendown()
t.right(40)
t.color("white")
t.begin_fill()
t.forward(168)
t.setheading(180)
t.forward(125)
t.end_fill()
t.penup()

#Draw the three small circles of the boat
t.color("brown","white")
t.goto(-70,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(-0,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(70,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

#draw the circle of the sun
t.color("yellow","yellow")
t.goto(-200,200)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()

#sunrays
t.pensize(5)
t.goto(-200,170)
for i in range(12):
    t.pendown()
    t.backward(80)
    t.forward(80)
    t.left(30)
t.penup()

#Draw the water
t.goto(-800,-150)
t.setheading(0)
t.color("Blue","Blue")
t.pendown()
t.begin_fill()
t.forward(1500)
t.right(90)
t.forward(180)
t.right(90)
t.forward(1500)
t.end_fill()

from turtle import *
write("Sink The Invaders!", align="center", font=("Cooper Black", 25, "italic"))

turtle.done()
