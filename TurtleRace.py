"""
Version 2

In this version the turtle race program is organized using multiple functions
"""

#Design Plan
import turtle
import random
from tkinter import messagebox

#Create race track window and configure it
def createRacetrack():
    raceTrack = turtle.Screen()
    raceTrack.bgcolor('lightgreen')
    return raceTrack


#Create the racers
def registerRacers():
    leo = turtle.Turtle()
    leo.shape("turtle")
    leo.color("darkgreen")
    leo.turtlesize(3, 3, 1)
    leo.penup()

    mikey = turtle.Turtle()
    mikey.shape("turtle")
    mikey.color("darkred")
    mikey.turtlesize(3, 3, 1)
    mikey.penup()

    don = turtle.Turtle()
    don.shape("turtle")
    don.color("blue")
    don.turtlesize(3, 3, 1)
    don.penup()
    return leo,mikey,don



#Position racers on starting line
def positionRacers(leo, mikey, don):
    # Position racers on starting line, 200 pixels apart sideways
    #use penup in initialization of turtles to not draw lines while they lineup
    
    leo.left(180) #turns larry all the way to the left 
    leo.forward(200) #makes larry go forward 200 pixels
    mikey.left(90) #turns curly upright
    don.forward(200) #moves curly to the right 200 pixels, no need to turn as hes already facing to the right
 #now ill make them upright
    don.left(90)
    leo.right(90)

#now use pendown to put the linesback
    leo.pendown()
    mikey.pendown()
    don.pendown()



#Run race
def runRace(leo, mikey, don):
    dist = random.randint(10,100)
    leo.forward(dist)

    dist = random.randint(10,100)
    mikey.forward(dist)

    dist = random.randint(10,100)
    don.forward(dist)



#Determine winner
def determineWinner(don):
    winnner = don

#Let user know who winner is
    messagebox.showinfo("Tutle Race ", "Mikey is the winner")

#run main program using functions I've defined
raceTrack = createRacetrack()
leo, mikey, don = registerRacers()
positionRacers(leo, mikey, don)
runRace(leo, mikey, don)
determineWinner(don)

#Waity for user confirmation to close program
raceTrack.exitonclick()