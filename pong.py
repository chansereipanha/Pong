import turtle as t

#Create our screen interface
screen = t.Screen()
width, height = 1000 ,900
screen.title("PingPong Game")
screen.bgcolor("Black")
screen.setup(width ,height)
screen.tracer(0)
score_a = 0
score_b =  0
max_score = 5

#Create a left paddle
left_paddle = t.Turtle()
left_paddle.color("white")
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
left_paddle.penup()
left_paddle.goto(-480,0)

#Create a right paddle
right_paddle = t.Turtle()
right_paddle.color("white")
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
right_paddle.penup()
right_paddle.goto(480,0)

#Create our ping pong ball
ball = t.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.pu()
ball.goto(0,0)
ball.dx = 0.1       
ball.dy = 0.1


#Create our scoreboard to keep track of the players score
score_board = t.Turtle()
score_board.penup()
score_board.color("white")
score_board.goto(0, 400)
score_board.write(f"Player A: {score_a}              Player B: {score_b}", align="center", font=("Roboto", 15, "bold"))
score_board.hideturtle()

#Create a function so that the left paddle can move up
def left_paddle_up():
    y_up = left_paddle.ycor()
    y_up += 30
    left_paddle.sety(y_up)

#Create a function so that the left paddle can move down
def left_paddle_down():
    y_up = left_paddle.ycor()
    y_up -= 30
    left_paddle.sety(y_up)

#Create a function so that the right paddle can move up
def right_paddle_up():
    y_up = right_paddle.ycor()
    y_up += 30
    right_paddle.sety(y_up)

#Create a function so that the right paddle can move down
def right_paddle_down():
    y_up = right_paddle.ycor()
    y_up -= 30
    right_paddle.sety(y_up)

#These codes will let you interact with the screen. 
screen.listen()   #listen() method allows you to capture any input given from the user onto the screen
screen.onkeypress(left_paddle_up, "w")  #onkeypress() method let's the user designate a key(from keyboard) as a command for a action
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")


#A while true loop so that the code in it will keep running until the end of the game
while True:
    screen.update()

    #These pair of codes will allow your ball to move and the speed at how fast they'll move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #These if statements will decide how the ball will interact onec they made impact with the edge of the screen 
    if ball.ycor() > 450:
        ball.sety(450)
        ball.dy *= -1

    if ball.ycor() < -450:
        ball.sety(-450)
        ball.dy *= -1

    #This if statement decide that if the ball were to touch the 
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_board.clear()
        score_board.write(f"Player A: {score_a}              Player B: {score_b}", align="center", font=("Roboto", 15, "bold"))



    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_board.clear()
        score_board.write(f"Player A: {score_a}              Player B: {score_b}", align="center", font=("Roboto", 15, "bold"))


    if 470 < ball.xcor() < 480 and (right_paddle.ycor()-40)< ball.ycor() < (right_paddle.ycor()+40):
        ball.dx*=-1
    if -480 < ball.xcor() < -470 and (left_paddle.ycor()-40)< ball.ycor() < (left_paddle.ycor()+40):
        ball.dx*=-1


    if score_a == max_score:
        screen.clear()
        screen.bgcolor("black")
        winner = t.Turtle()
        winner.color("white")
        winner.write("Player A is the winner", align= "center", font=("Arial", 30, "bold"))
        winner.hideturtle()
        break
    elif score_b == max_score:
        screen.clear()
        screen.bgcolor("black")
        winner = t.Turtle()
        winner.color("white")
        winner.write("Player B is the winner", align= "center", font=("Arial", 30, "bold"))
        winner.hideturtle()
        break


t.done()