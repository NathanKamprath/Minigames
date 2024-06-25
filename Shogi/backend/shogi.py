#A place to test out some of the board drawing abilities

'''
from turtle import Turtle, Screen
import turtle

turtle.hideturtle()
t= turtle.Turtle()
t.hideturtle()

speed = t.speed()
width = 9
board = width ** 2

def Create_Board(turtle):
    for blocks in range(width):
        direc = [turtle.right, turtle.left][blocks % 2 == 1]

        for _ in range(0, board, speed):
            turtle.forward(speed)
            yield(0)
        direc(90)

        for _ in range(0, width, speed):
            turtle.forward(speed)
            yield(0)
        direc(90)

        for _ in range(0, board, speed):
            turtle.forward(speed)
            yield(0)

walk = Turtle()
walk.speed(0)
walk.penup()
walk.goto(-board, -board)
walk.pendown()
walk.left(90)

jog = Turtle()
jog.speed(0)
jog.penup()
jog.goto(0, -board * 2)
jog.pendown()
jog.left(180)

gen1, gen2 = Create_Board(walk), Create_Board(jog)

while (next(gen1, 1) + next(gen2, 1) < 2):
    pass

walk.hideturtle()
jog.hideturtle()
screen = Screen()
screen.exitonclick()
'''


'''
player_blocks = []
def createBoard(board, blocks):
    width = 9
    i = 0
    for i in range(width * width):
        block = board.append({"id": i})
        blocks.append(block)
        i += 1

createBoard(playerBoard, playerBlocks)
'''