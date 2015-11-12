import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square(the_turtle):
	for squaring in range(1,5):
		the_turtle.forward(250)
		the_turtle.right(90)

def draw_circle():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(60)

	for circling in range (1,36):
		draw_square(brad)
		brad.right(10)

def draw_things():
	draw_circle()
	window.exitonclick()

draw_things()