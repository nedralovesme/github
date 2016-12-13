from turtle import *
from draw_a_square import *

coords=[(-100,-100,50),(-100,100,20),(100,100,120),(100,-100,200)]

for coord in coords:
    up()
    home()
    x,y,size = coord
    setheading(0)
    forward(x)
    setheading(270)
    forward(y)
    down()
    draw_square(size)

mainloop()
