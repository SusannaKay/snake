from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total = 0
        #self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()


    def score(self):
        self.total += 1
        self.update_scoreboard()
    def reset(self):
        if self.total > self.high_score:
            self.high_score = self.total
            with open("data.txt", mode="w") as file:
                file.write(str(self.total))

        self.total = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.total}. High Score {self.high_score}", False, align="center", font=("Courier", 20, "normal"))


    # def game_over(self):
    #     self.goto(0, 0)
    #
    #     self.write("GAME OVER", False, align="center", font=("Courier", 20, "normal"))



