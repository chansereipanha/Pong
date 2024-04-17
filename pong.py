import turtle as t

class Pong:
    def __init__(self, screen, score_a, score_b, right_paddle, left_paddle, ball, score_board):
        self.screen = screen
        self.score_a = score_a
        self.score_b = score_b
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.ball = ball
        self.score_board = score_board

    def window(self):
        width, height = 1000 ,900
        screen = t.Screen()
        screen.title("PingPong Game")
        screen.bgcolor("Black")
        screen.setup(width ,height)
        screen.tracer(0)
        self.score_a = 0
        self.score_b =  0
    
        #Create left paddle
    def paddle_a(self):
        self.left_paddle = t.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.color("white")
        self.left_paddle.shape("square")
        self.left_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
        self.left_paddle.penup()
        self.left_paddle.goto(480,0)

    #Create a right paddle
    def paddle_a(self):
        self.right_paddle = t.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.color("white")
        self.right_paddle.shape("square")
        self.right_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
        self.right_paddle.penup()
        self.right_paddle.goto(-480,0)

    def bouncing_ball(self):
        self.ball = t.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.ball.pu()
        self.ball.goto(0,0)
        self.ball.dx = 1
        self.ball.dy = 1

    def scoreboard(self):
        self.score_board = t.Turtle()
        self.score_board.penup()
        self.score_board.color("white")
        self.score_board.goto(0, 400)
        self.score_board.write("Player A: 0               Player B: 0", align="center", font=("Arial", 15, "normal"))
        self.score_board.hideturtle()




class Paddle(Pong):
    def __init__(self, screen, right_paddle, left_paddle, y_up, y_down):
        super().__init__(screen, right_paddle, left_paddle)
        self.y_up = y_up
        self.y_down = y_down

    def left_paddle_up(self):
        self.y_up = self.left_paddle.ycor()
        self.y_up += 30
        self.left_paddle.sety(self.y_up)

    def left_paddle_down(self):
        self.y_up = self.left_paddle.ycor()
        self.y_up -= 30
        self.left_paddle.sety(self.y_up)

    def right_paddle_up(self):
        self.y_up = self.right_paddle.ycor()
        self.y_up += 30
        self.right_paddle.sety(self.y_up)

    def left_paddle_down(self):
        self.y_up = self.right_paddle.ycor()
        self.y_up -= 30
        self.right_paddle.sety(self.y_up)

class key(Paddle):
    def __init__(self, screen, right_paddle, left_paddle,):
        super().__init__(screen, right_paddle, left_paddle)

    def keybinds(self):
        self.screen.listen()
        self.screen.onkeypress(Paddle.left_paddle_up, "w")
        self.screen.onkeypress(Paddle.left_paddle_down, "s")
        self.screen.onkeypress(Paddle.right_paddle_up, "Up")
        self.screen.onkeypress(Paddle.right_paddle_up, "Down")





t.done()