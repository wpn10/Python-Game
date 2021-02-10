import turtle

wn = turtle.Screen()
wn.title("Pong-Remasterred by Paritosh")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("black")
bat_a.shapesize(stretch_wid=5,stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)

# Paddle B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("black")
bat_b.shapesize(stretch_wid=5,stretch_len=1)
bat_b.penup()
bat_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Paritosh: 0  Opponent: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def bat_a_up():
    y = bat_a.ycor()
    y += 20
    bat_a.sety(y)

def bat_a_down():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)

def bat_b_up():
    y = bat_b.ycor()
    y += 20
    bat_b.sety(y)

def bat_b_down():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(bat_a_up, "w")
wn.onkeypress(bat_a_down, "s")
wn.onkeypress(bat_b_up, "Up")
wn.onkeypress(bat_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Paritosh: {}  Opponent: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Paritosh: {}  Opponent: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < bat_a.ycor() + 50 and ball.ycor() > bat_a.ycor() - 50:
        ball.dx *= -1 
        
    elif ball.xcor() > 340 and ball.ycor() < bat_b.ycor() + 50 and ball.ycor() > bat_b.ycor() - 50:
        ball.dx *= -1
        
