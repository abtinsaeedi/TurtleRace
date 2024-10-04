"""runs the actual race, finds winner"""

import turtle
import random

leo = mikey = don = None


#Create the racers
def registerRacers():
    global leo, mikey, don
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
def positionRacers():
    global leo, mikey, don
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
def runRace():
    global leo, mikey, don
    dist = random.randint(10,100)
    leo.forward(dist)

    dist = random.randint(10,100)
    mikey.forward(dist)

    dist = random.randint(10,100)
    don.forward(dist)
    
    #Determine winner
def determineWinner():
    global don
    winnner = don