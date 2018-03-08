import turtle


def draw_square(romeo):
    for i in range(1, 5):
        romeo.forward(100)
        romeo.right(90)


def draw_graphic():
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("pink")
    brad.color("green")
    brad.shape("turtle")
    brad.speed(20)
    for i in range(1,73):
        draw_square(brad)
        brad.right(5)

    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(90)
    brad.left(110)
    brad.forward(100)
    brad.left(70)
    brad.forward(100)
    brad.left(70)
    brad.forward(100)
    brad.left(110)
    brad.forward(70)

    window.exitonclick()

draw_graphic()
