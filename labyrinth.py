#Name: Thomas Hunter
#Date: September 1, 2017
#This program prints: A labyrinth like spiral

import turtle

def labyrinth():
    sketcher = turtle.Turtle()
    def draw():
        for steps in (range(10, 251, 10)):
            sketcher.forward(steps)
            sketcher.left(90)

    return draw()

if __name__ == '__main__':
    labyrinth()