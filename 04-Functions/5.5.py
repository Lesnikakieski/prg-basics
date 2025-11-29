####
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures

# 1. Pierwszy zestaw figur

# kwadrat w środku
figures.draw_square(pen, 80)

# trójkąt w lewym górnym rogu
pen.penup()
pen.goto(-100, 100)
pen.pendown()
figures.draw_triangle(pen, 80)

# prostokąt w prawym górnym rogu
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

# 2. Drugi zestaw figur (w innych miejscach)

# kwadrat na dole po lewej
pen.penup()
pen.goto(-150, -100)
pen.pendown()
figures.draw_square(pen, 60)

# trójkąt na dole po środku
pen.penup()
pen.goto(0, -100)
pen.pendown()
figures.draw_triangle(pen, 60)

# prostokąt na dole po prawej
pen.penup()
pen.goto(150, -100)
pen.pendown()
figures.draw_rectangle(pen, 80, 40)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
