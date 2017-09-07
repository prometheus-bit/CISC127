#Name: Thomas Hunter
#Date: September 6, 2017
#This program prints: a Spiral of increasing pen sizes using turtle module

import turtle

def spiral():
    pen = turtle.Turtle()
    for num in (range(10,55,5)):
        pen.pensize(num)
        pen.forward(num)
        pen.left(50)

if __name__ == '__main__':
    spiral()