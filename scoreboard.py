from turtle import Turtle
import os

ALIGN = "center"
FONT = ("Courier", 23, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        data_file = os.path.join("text_folder", "data.txt")
        with open(data_file) as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore =  self.score
            data_file = os.path.join("text_folder", "data.txt")
            with open(data_file, mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()