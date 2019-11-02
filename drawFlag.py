"""
Kelley Fischer
Midterm Project - American Flag


"""

from turtle import Turtle


#-----------------------------------------------------------------#
# Determiens if a number is odd or even for alternating sequences #
#-----------------------------------------------------------------#
def even(n):
	if n % 2 == 0:
		return True
	else:
		return False


#------------------------------------------------------------------#
# This draws the flag stripes, given turtle, height, width, and xy #
#------------------------------------------------------------------#
def drawFlag(t, height, width, x, y):
	for stripe in range(13):
		if even(stripe):
			t.pencolor("red")
			t.fillcolor("red")
		else:
			t.pencolor("white")
			t.fillcolor("white")
		t.begin_fill()
		for side in range(2):
			t.forward(width)
			t.left(90)
			t.forward(height)
			t.left(90)
		t.end_fill()
		y += height
		t.goto(x, y)


#----------------------------------------------------------------#
# Draws the rectangle where the stars are drawn			 #
#----------------------------------------------------------------#
def drawStarField(t):
        t.setheading(0)
        t.pendown()
        t.pencolor("blue")
        t.fillcolor("blue")
        t.begin_fill()
        t.forward(540)
        t.right(90)
        t.forward(280)
        t.right(90)
        t.forward(540)
        t.right(90)
        t.forward(280)
        t.end_fill()


#----------------------------------------------------------------#
# Draws a white star						 #
#----------------------------------------------------------------#
def drawStar(t):
    t.setheading(36)
    count = 0
    t.pendown()
    t.pencolor("white")
    t.begin_fill()
    t.fillcolor("white")
    while count < 5:
        t.forward(20)
        t.left(144)
        count += 1
    t.end_fill()


#----------------------------------------------------------------#
# Sets position of each star then draws it by calling drawStar   #
#----------------------------------------------------------------#
def fiftyStars(t, x, y):
    count = 0
    stars = 0
    t.penup()
    while stars < 50:
        if count % 6 == 0:
            x += 40
            y -= 25
            t.goto(x, y)
        elif count % 11 == 0:
            x -= 40
            y -= 25
            t.goto(x, y)
            count = 0
        drawStar(t)
        t.setheading(0)
        t.penup()
        t.forward(80)
        stars += 1
        count += 1


#----------------------------------------------------------------#
# This is the main function					 #
#----------------------------------------------------------------#
def main():
    t = Turtle()
    t.speed(0)
    t.screen.bgcolor(0, 0, 0)

    x = -650
    y = -260

    # Sets the initial position for the flag to be drawn
    t.goto(x, y)

    drawFlag(t, 40, 1300, x, y)
    drawStarField(t)

    (x, y) = t.position()
    # x += 10
    # y -= 10

    fiftyStars(t, x, y)

    t.hideturtle()


if __name__ == "__main__":
    main()
