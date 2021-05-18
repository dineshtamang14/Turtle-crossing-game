from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.current_level()

    def current_level(self):
        self.goto(-280, 270)
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.!", align="center", font=FONT)


