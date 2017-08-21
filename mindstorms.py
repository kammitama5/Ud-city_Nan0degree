import turtle
"""
draw a square in turtle
"""

def draw_square():
	window = turtle.Screen()
	window.bgcolor("green")
	
	brad = turtle.Turtle()
	
	brad.color("violet", "yellow")
	brad.begin_fill()
	
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.end_fill()

	window.exitonclick()

draw_square()
