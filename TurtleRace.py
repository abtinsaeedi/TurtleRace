"""
Version 3

In this version the turtle race program is organized using modules
"""

#Design Plan
import turtle
import random
import RaceTrack
import Race

from tkinter import messagebox




#run main program using functions I've defined
RaceTrack.createRacetrack()
Race.registerRacers()
Race.positionRacers()
Race.runRace()
Race.determineWinner()

#Let user know who winner is
messagebox.showinfo("Tutle Race ", "Mikey is the winner")

#Waity for user confirmation to close program
RaceTrack.closeRacetrack()