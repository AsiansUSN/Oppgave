# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:12:23 2018

@author: Tommy
"""

from random import randint

antall = 5
upperScores = []
for i in range(6):
    upperScores.append(str(i+1) + "ere")

pointTableNames = tuple(upperScores) +\
        (
        "delsum",
        "bonus",
        "total"
        )

def rollDice(diceList, hold=" "):
    print(hold)
    for i in range(len(diceList)):
        try:
            pos = hold.index(str(i - 1))
        except:
            diceList[i] = randint(1,6)

def showHelp():
    print("Masse hjelpetekst her")

def showScores():
    for i in range(len(pointTableNames)):
        print("%-15s %d" % (pointTableNames[i], 0))

def showDice(diceList):
    for dice in diceList:
        print(dice,end=" ")

def play_yatzy():
    print("Nå spiller vi yatzy")
    #Trekker fra 3 fordi delsum, bonus og total ikke skal trilles
    for i in range(len(pointTableNames) - 3):
        diceList = [0]*5
        rollDice(diceList)
        throwCount = 1
        while throwCount < 3:
            userInput = input("Hva vil du gjøre? ('h' for hjelp) ")
            if userInput == "h":
                showHelp()
            elif userInput == "s":
                showScores()
            elif userInput == "q":
                return
            else: 
                rollDice(diceList, userInput)
                showDice(diceList)



play_again = True
while play_again:
    play_yatzy()
    play_again = input("Vil du spille en gang til? (Ja/Nei): ") == "ja"