from turtle import *

def draw_square(size):
    for i in range(4):
        forward(size)
        left(90)

if __name__=="__main__":
    print __name__
    draw_square()

    up()
    forward(200)
    down()

    draw_square()

    mainloop()
