"""Creates race track and racers"""
import turtle

raceTrack = None

#Create race track window and configure it
def createRacetrack():
    global raceTrack
    raceTrack = turtle.Screen()
    raceTrack.bgcolor('lightgreen')
    return raceTrack

#


#Waity for user confirmation to close program
def closeRacetrack():
    
    raceTrack.exitonclick()