from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

    def score(self):
        self.total += 1

    def game_over(self):
        self.goto(0, 0)

        self.write("GAME OVER", False, align="center", font=("Courier", 20, "normal"))
