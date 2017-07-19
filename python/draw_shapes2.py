from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(1000,600)
x_pos = 0
y_pos = 0

a = int(input('How many sides?'))
c = 180 - ((a - 2)*180/a)
### Write your code below:
###square:
t.begin_fill()
t.fillcolor("purple")
for b in range(a):
	t.forward(150)
	t.right(c)
t.end_fill()

# Close window on click.
exitonclick()

#	e = 150
#	t.forward(1)
#	e += 1
#	t.forward(1)
