from lib import parseFloat
import turtle
import math

katet1: float = parseFloat("Hva er lengden til kateten langs x aksen? ")
degrees: float = parseFloat("Hvor mange grader er vinkelen? ")
rad: float = math.radians(degrees)
hypotenus: float = katet1/math.cos(rad)
opposite: float = katet1*math.tan(rad)

turtle.down()
turtle.forward(katet1)
turtle.left(90)
turtle.forward(opposite)
turtle.left(math.degrees(rad)+90)
turtle.forward(hypotenus)
turtle.mainloop()