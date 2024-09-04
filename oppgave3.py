import turtle

def drawHexagon(turtle: turtle, x: float, y: float, sidelength: int) -> None:
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for i in range(6):
        turtle.forward(sidelength)
        turtle.left(60)
    turtle.up()
    
drawHexagon(turtle, 0, 0, 100)
drawHexagon(turtle, 300, 0, 20)
drawHexagon(turtle, 120, 200, 50)
drawHexagon(turtle, 0, 200, 30)
turtle.mainloop()