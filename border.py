from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        self.goto(290, 290)
        self.goto(290, -290)
        self.goto(-290, -290)
        self.goto(-290, 290)
