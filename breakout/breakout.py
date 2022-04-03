from turtle import Turtle, Screen
import random
import time


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.hideturtle()
        self.paddle.shape("square")
        self.paddle.shapesize(1, 5)
        self.paddle.color("blue")
        self.paddle.setposition(0, -250)
        self.paddle.showturtle()

    def pad_left(self):
        self.paddle.fd(-50)
        print(self.paddle.pos())

    def pad_right(self):
        self.paddle.fd(50)
        print(self.paddle.pos())


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("black")
        self.x = 0
        self.y = 0
        self.ball.setposition(self.x, self.y)

    def restart(self):
        self.ball.hideturtle()
        self.ball.setposition(0, 0)
        self.ball.setheading(270)
        self.ball.showturtle()

    def move(self):
        self.ball.fd(40)

    def bounce(self):
        if self.ball.xcor() > 365:
            self.ball.right(self.ball.xcor() * -1)
        elif self.ball.xcor() < -375:
            self.ball.right(self.ball.xcor() * 1)
        elif self.ball.distance(paddle.paddle.pos()) < 50:
            self.ball.right((self.ball.ycor() * -1))
        elif self.ball.ycor() < -265:
            Ball.restart(self)
        elif self.ball.ycor() > 250:
            self.ball.right(self.ball.ycor() * -1)


class Brick:
    def __init__(self):
        self.brick = Turtle()
        self.x = 300
        self.y = 275
        self.brick.hideturtle()
        self.brick.speed(0)
        self.brick.penup()
        self.brick.shape("square")
        self.brick_colors = "red", "blue", "yellow", "green", "purple", "orange"
        self.brick.shapesize(1, 3)
        self.brick.setposition(self.x, self.y)
        self.brick.showturtle()

    def wall(self):
        for b in range(0, 6):
            for br in range(0, 9):
                self.brick.penup()
                self.brick.setposition(self.x, self.y)
                self.brick.pendown()
                rnd_color = random.choice(self.brick_colors)
                self.brick.color(rnd_color)
                self.brick.stamp()
                self.x -= 75
            self.x = 300
            self.y -= 25


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
brick = Brick()
brick.wall()

screen.onkey(paddle.pad_left, "a")
screen.onkey(paddle.pad_right, "d")
screen.listen()

game = True
new_game = True
while game:
    screen.update()
    time.sleep(0.1)
    if new_game:
        ball.restart()
        new_game = False
    else:
        ball.move()
        ball.bounce()


screen.mainloop()
