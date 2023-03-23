import turtle

alex = turtle.Turtle()

tam = 20
n = 5

for i in range(n):
  lado = tam
  alex.penup()
  for i in range(2):
    alex.right(90)
    alex.foward(tam/2)
  alex.right(180)
  alex.pendown()
  for i in range(4):
    alex.foward(lado)
    alex.left(90)
  lado += tam

done()  
