from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
brick_colors = "red", "blue", "yellow", "green", "purple", "orange"


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.hideturtle()
        self.paddle.shape("square")
        self.paddle.shapesize(1, 6)
        self.paddle.color("blue")
        self.paddle.setposition(0, -250)
        self.paddle.showturtle()

    def pad_left(self):
        self.paddle.fd(-100)

    def pad_right(self):
        self.paddle.fd(100)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("black")
        self.ball.right(90)
        self.x = 0
        self.y = 0
        self.ball.setposition(self.x, self.y)

    def restart(self):
        self.ball.hideturtle()
        self.ball.setposition(0, 0)
        self.ball.showturtle()

    def move(self):
        self.ball.fd(50)

    def bounds(self):
        if -375 < self.ball.xcor() < 375 and -275 < self.ball.ycor() < 275:
            return True


class Brick:
    def __init__(self):
        self.brick = Turtle()
        self.x = 300
        self.y = 275
        self.brick.hideturtle()
        self.brick.speed(0)
        self.brick.penup()
        self.brick.shape("square")
        self.brick.color("blue")
        self.brick.shapesize(1, 3)
        self.brick.setposition(self.x, self.y)
        self.brick.showturtle()

    def wall(self):
        for b in range(0, 5):
            for br in range(0, 9):
                if br == 1:
                    rnd_color = random.choice(brick_colors)
                    self.brick.color(rnd_color)
                self.brick.stamp()
                self.brick.penup()
                self.brick.setposition(self.x, self.y)
                self.brick.pendown()
                self.brick.stamp()
                self.x -= 75
            self.x = 300
            self.y -= 25


paddle = Paddle()
ball = Ball()
brick = Brick()
brick.wall()

screen.onkey(paddle.pad_left, "a")
screen.onkey(paddle.pad_right, "d")
screen.listen()

game = True
while game:
    if ball.bounds():
        ball.move()
    else:
        ball.restart()


screen.mainloop()
