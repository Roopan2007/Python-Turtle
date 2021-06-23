import turtle
hex=turtle.Pen()
colours = ["red","blue","green","purple","orange","pink"]
turtle.bgcolor("black")
for i in range(360):
    hex.pencolor(colours[i%6])
    hex.width(i/100+1)
    hex.forward(i)
    hex.left(59)