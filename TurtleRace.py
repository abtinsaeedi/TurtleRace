"""
Version 1
In this version the turtle race has a flat single file structure
"""

#Design Plan
import turtle
import random
from tkinter import messagebox

#Create race track window and configure it
raceTrack = turtle.Screen()
raceTrack.bgcolor('lightgreen')

#Create the racers
larry = turtle.Turtle()
larry.shape("turtle")
larry.color("darkgreen")
larry.turtlesize(3, 3, 1)
larry.penup()

curly = turtle.Turtle()
curly.shape("turtle")
curly.color("darkred")
curly.turtlesize(3, 3, 1)
curly.penup()

moe = turtle.Turtle()
moe.shape("turtle")
moe.color("blue")
moe.turtlesize(3, 3, 1)
moe.penup()

#Position racers on starting line
# Position racers on starting line, 200 pixels apart sideways
    #use penup in initialization of turtles to not draw lines while they lineup


larry.left(180) #turns larry all the way to the left 
larry.forward(200) #makes larry go forward 200 pixels
curly.left(90) #turns curly upright
moe.forward(200) #moves curly to the right 200 pixels, no need to turn as hes already facing to the right
 #now ill make them upright
moe.left(90)
larry.right(90)

#now use pendown to put the linesback
larry.pendown()
curly.pendown()
moe.pendown()

#Run race
dist = random.randint(10,100)
larry.forward(dist)

dist = random.randint(10,100)
curly.forward(dist)

dist = random.randint(10,100)
moe.forward(dist)

#Determine winner
#user branching to determine which turtle advanced the most
winnner = moe

#Let user know who winner is
messagebox.showinfo("Tutle Race ", "Moe")
#Waity for user confirmation to close program
raceTrack.exitonclick()