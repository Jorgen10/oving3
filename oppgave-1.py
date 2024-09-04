import turtle
import math

katet1 = float(input("Hva er lengden til kateten langs x aksen? "))
degrees = float(input("Hvor mange grader er vinkelen? "))
rad = math.radians(degrees)
hypotenus = katet1/math.cos(rad)
opposite = katet1*math.tan(rad)

turtle.down()
turtle.forward(katet1)
turtle.left(90)
turtle.forward(opposite)
turtle.left(math.degrees(rad)+90)
turtle.forward(hypotenus)
turtle.mainloop()