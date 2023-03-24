import turtle

alex = turtle.Turtle()

def spiral(tam, angle):
    alex.right(90)
    alex.forward(1)
    for i in range(tam-1):
        for j in range(2):
            alex.forward((i+1)*4)
            alex.right(angle)
    alex.forward(tam*4)
    alex.right(90)

spiral(50, 90)

turtle.done()