from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# class Paddle:
#     def __init__(self):
#             self.paddle=Turtle()
#             self.create_paddle(self.paddle.xcor())
#
#
#
#     def create_paddle(self,x_cordinate):
#             self.paddle.shape("square")
#             self.paddle.shapesize(stretch_wid=5, stretch_len=1)
#             self.paddle.color("white")
#             self.paddle.penup()
#             self.paddle.goto(x=x_cordinate, y=0)
#
#
#     def go_up(self):
#             new_ycor = self.paddle.ycor() + 20
#             self.paddle.goto(self.paddle.xcor(), new_ycor)
#
#     def go_down(self):
#             new_ycor = self.paddle.ycor() - 20
#             self.paddle.goto(self.paddle.xcor(), new_ycor)




