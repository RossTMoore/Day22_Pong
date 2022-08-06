from turtle import Turtle

class Net(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.goto(0, -270)
      self.color("grey")
      self.shape("square")
      self.seth(90)
      self.shapesize(0.5, 2)

    def make_net(self):
      for x in range (12):
        self.stamp()
        self.forward(70)



