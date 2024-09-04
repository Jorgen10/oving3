import turtle

def drawHexagon(sidelength: int) -> None:
    turtle.down()
    for i in range(6):
        turtle.forward(sidelength)
        turtle.left(60)
    turtle.up()
    
drawHexagon(100)
turtle.mainloop()