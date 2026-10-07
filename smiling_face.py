import turtle


def draw_smiley():
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("lightcyan")
    screen.title("Python Smiley")

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)

    # 1. Draw yellow head circle
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # 2. Draw Left Eye
    t.penup()
    t.goto(-35, 30)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(12)
    t.end_fill()

    # 3. Draw Right Eye
    t.penup()
    t.goto(35, 30)
    t.pendown()
    t.begin_fill()
    t.circle(12)
    t.end_fill()

    # 4. Draw Smile
    t.penup()
    t.goto(-40, -10)
    t.setheading(-60)
    t.pendown()
    t.pensize(6)
    t.color("black")
    t.circle(45, 120)

    # Hide cursor and finish
    t.hideturtle()
    turtle.done()


if __name__ == "__main__":
    draw_smiley()
