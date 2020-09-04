#!/bin/python3
from random import choice
from turtle import *


screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

robots = {}

file = open("cards.txt")

for line in file.read().splitlines():
    name, battery, intelligence, image = line.split(', ')
    robots[name] = [battery, intelligence, image]
file.close()

while True:
    robot = input("Choose a robot:")
    if robot in robots:
        stats = robots[robot]
        #print(robots[robot])
        style = ('Arial', 14, 'bold')
        setheading(-90)
        write('Name: ' + robot , font=style, align='center')
        forward(25)
        write('battery: ' + stats[0], font=style, align='center')
        forward(25)
        write('Intelligence' + stats[1], font=style, align='center')
    else:
        print('Robot doesn\'t exist!' )
        break





