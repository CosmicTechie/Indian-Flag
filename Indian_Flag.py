# Import the turtle Module
import turtle

# Instance
Indian_Flag = turtle.Turtle()

# Setting Animation Speed 
Indian_Flag.speed(0)
 
#Intitial
Indian_Flag.penup()
Indian_Flag.goto(-400, 250)
Indian_Flag.pendown()

# Orange Portion
Indian_Flag.color("#FF9933")
Indian_Flag.begin_fill()
Indian_Flag.forward(800)
Indian_Flag.right(90)
Indian_Flag.forward(167)
Indian_Flag.right(90)
Indian_Flag.forward(800)
Indian_Flag.end_fill()
Indian_Flag.left(90)
Indian_Flag.forward(167)

# Green Portion
Indian_Flag.color("#138808")
Indian_Flag.begin_fill()
Indian_Flag.forward(167)
Indian_Flag.left(90)
Indian_Flag.forward(800)
Indian_Flag.left(90)
Indian_Flag.forward(167)
Indian_Flag.end_fill()


#------ Centre Portion--------#

# Large Blue Circle 
Indian_Flag.penup()
Indian_Flag.goto(70, 0)
Indian_Flag.pendown()
Indian_Flag.color("#000080")
Indian_Flag.begin_fill()
Indian_Flag.circle(70)
Indian_Flag.end_fill()

# White Circle inside the Large Blue Circle
Indian_Flag.penup()
Indian_Flag.goto(60, 0)
Indian_Flag.pendown()
Indian_Flag.color("white")
Indian_Flag.begin_fill()
Indian_Flag.circle(60)
Indian_Flag.end_fill()

# Tiny Blue Circles
Indian_Flag.penup()
Indian_Flag.goto(-57,-8)
Indian_Flag.pendown()
Indian_Flag.color("#000080")
for i in range(24):
    Indian_Flag.begin_fill()
    Indian_Flag.circle(3)
    Indian_Flag.end_fill()
    Indian_Flag.penup()
    Indian_Flag.forward(15)
    Indian_Flag.right(15)
    Indian_Flag.pendown()
 
# Small Blue Circle in center
Indian_Flag.penup()
Indian_Flag.goto(20, 0)
Indian_Flag.pendown()
Indian_Flag.begin_fill()
Indian_Flag.circle(20)
Indian_Flag.end_fill()

# Spokes
Indian_Flag.penup()
Indian_Flag.goto(0, 0)
Indian_Flag.pendown()
Indian_Flag.pensize(2)
for i in range(24):
    Indian_Flag.forward(60)
    Indian_Flag.backward(60)
    Indian_Flag.left(15)

# Output Window
turtle.done()