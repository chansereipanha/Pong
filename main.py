from pong import *

def window():
    width, height = 1000 ,900
    screen = t.Screen()
    screen.title("PingPong Game")
    screen.bgcolor("Black")
    screen.setup(width ,height)
    screen.tracer(0)
    score_a = 0
    score_b =  0

def main():
    while True:
        window()




if __name__ == "__main__":
    main()