import turtle

alex = turtle.Turtle()

tam = 20
n = 5
lado = tam

for i in range(n):
  alex.penup()
  alex.setpos(-lado/2, -lado/2)
  alex.pendown()
  for i in range(4):
    alex.forward(lado)
    alex.left(90)
  lado += tam

turtle.done()



