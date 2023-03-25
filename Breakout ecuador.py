import random
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Atari Breakout - Ecuador")
screen.bgcolor("blue")
screen.setup(width=640, height=480)

# Set up the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("yellow")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -220)

# Set up the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.speed("fast")
ball.dx = 3 * random.choice([-1, 1])
ball.dy = -3

# Set up the bricks
brick_colors = ["yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow",
                "red", "red", "red", "red", "red", "red", "red", "red",
                "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue",
                "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow",
                "red", "red", "red", "red", "red", "red", "red", "red"]
bricks = []
brick_width = 60
brick_height = 20
brick_x = -260
brick_y = 150
for i in range(5):
    for j in range(8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[i * 8 + j])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(brick_x + j * (brick_width + 10), brick_y - i * (brick_height + 10))
        bricks.append(brick)

# Set up the score and lives
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("yellow")
score_turtle.penup()
score_turtle.goto(-290, 220)
score_turtle.write("Score: {}".format(score), font=("Arial", 16, "normal"))
lives = 3
lives_turtle = turtle.Turtle()
lives_turtle.hideturtle()
lives_turtle.color("yellow")
lives_turtle.penup()
lives_turtle.goto(200, 220)
lives_turtle.write("Lives: {}".format(lives), font=("Arial", 16, "normal"))

# Define functions for moving the paddle
def move_left():
    x = paddle.xcor()
    if x > -260:
        x -= 20
        paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 260:
        x += 20
        paddle.setx(x)

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Set up the game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for a collision with the wall
    if ball.xcor() > 310 or ball.xcor() < -310:
        ball.dx *= -1
