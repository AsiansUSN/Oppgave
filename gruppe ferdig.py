# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:46:55 2018

@author: Tommy
"""

import random

print("det er 2 spillere med uendelige kort.")
print("kortene har et tilfeldig nummer fra 1 til 13.")
print("spilleren med størst nummer får +1 poeng.")
print("det trekkes et nytt kort for hver runde.")
print("vinneren er den første med 10 poeng.")

spiller1_navn = input("Spillernavn 1: ")
spiller2_navn = input("Spillernavn 2: ")


def play_game():
    poengspiller1 = 0
    poengspiller2 = 0
    runde_teller = 0
    

    while 1:
        kortspiller1 = random.randint(1,13)
        kortspiller2 = random.randint(1,13)
        runde_teller = runde_teller + 1
        if kortspiller1 == kortspiller2:
            print("Like nummer, ingen får poeng")
            print("Runde", runde_teller)
            print(spiller2_navn, "har : ",poengspiller2, "poeng  ----- ", spiller1_navn, "har : ", poengspiller1 , "poeng.")

        elif kortspiller1 < kortspiller2:

            poengspiller1 = poengspiller1 + 1
            print("Runde", runde_teller)
            print(spiller1_navn, "fikk høyere tall enn ", spiller2_navn)
            print(spiller2_navn, "har : ",poengspiller2, "poeng  ----- ", spiller1_navn, "har : ", poengspiller1, "poeng.")

        elif kortspiller1 > kortspiller2:
            poengspiller2 = poengspiller2 + 1
            print("Runde", runde_teller)
            print(spiller2_navn, "fikk høyere tall enn ", spiller1_navn)
            print(spiller2_navn, "har : ",poengspiller2, "poeng  ----- ", spiller1_navn, "har : ", poengspiller1, "poeng.")

        if poengspiller1 >= 10:
            print(spiller1_navn + " vant!")
            print("du spilte : ", runde_teller, "runder.")
            break 
        elif poengspiller2 >= 10:
            print(spiller2_navn + " vant!")
            print("du spilte : ", runde_teller, "runder.")
            break

play_again = True
while play_again:
    play_game()
    play_again = input("Vil du starte en ny runde? (Ja/Nei): ") == "ja"