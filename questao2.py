import turtle
import math

tess = turtle.Turtle()


def draw_poly(t, n, sz):
  t.penup()
  t.setpos(-sz/2, -sz/(2*math.tan(180/n)))
  t.pendown()
  for i in range(n):
    t.forward(sz)
    t.left(360/n)

draw_poly(tess, 8, 50)

turtle.done()