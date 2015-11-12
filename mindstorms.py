# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(2)

	squaring = 0
	while squaring < 4:
		brad.forward(100)
		brad.right(90)
		squaring += 1

def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

def draw_triangle():
	george = turtle.Turtle()
	george.shape("turtle")
	george.color("green")
	george.speed(1)

	triangling = 0
	while triangling < 3:
		george.forward(100)
		george.right(120)
		triangling += 1

def draw_things():
	draw_square()
	draw_circle()
	draw_triangle()
	window.exitonclick()

draw_things()