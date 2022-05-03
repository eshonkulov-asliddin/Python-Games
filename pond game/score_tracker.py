from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.draw()
        self.color("red")
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        # self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align='center', font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align='center', font=("Courier", 50, "normal"))

    def l_point(self):
        self.score_l += 1
        self.update_score()

    def r_point(self):
        self.score_r +=1
        self.update_score()

    def draw(self):
        new_turtle = Turtle()
        new_turtle.color("black")
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.setheading(270)
        new_turtle.forward(290)
        for _ in range(31):
            new_turtle.setheading(90)
            new_turtle.pendown()
            new_turtle.forward(10)
            new_turtle.penup()
            new_turtle.forward(10)

