from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
      super().__init__()
      self.x_cor = x_cor
      self.y_cor = y_cor
      self.goto(x_cor,y_cor)
      self.penup()
      self.shape("square")
      self.seth(90)
      self.shapesize(1, 5)

    def move_up(self):
      self.forward(20)
    def move_down(self):
      self.backward(20)




