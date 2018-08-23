# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:16:46 2018

@author: Tommy
"""

import random

print("det er 2 spillere med uendelige kort.")
print("kortene har et tilfeldig nummer fra 1 til 13.")
print("spilleren med størst nummer får +1 poeng.")
print("det trekkes et nytt kort for hver runde.")
print("vinneren er den første med 10 poeng.")

spiller1_navn = input("navn spiller 1: ")
spiller2_navn = input("navn spiller 2: ")

#poengspiller1 = 0
#poengspiller2 = 0

def play_game():
#    global poengspiller1
#    global poengspiller2
    poengspiller1 = 0
    poengspiller2 = 0

    while poengspiller1 < 10 and poengspiller2 < 10:
        kortspiller1 = random.randint(1,13)
        kortspiller2 = random.randint(1,13)
        if kortspiller1 == kortspiller2:
            print("Like nummer, ingen får poeng")
            print(spiller2_navn, "har : ",poengspiller2, "poeng", spiller1_navn, "har : ", poengspiller1)
            
   
        elif kortspiller1 < kortspiller2:
        
            poengspiller1 = poengspiller1 + 1
            print(spiller1_navn, "fikk høyere tall enn ", spiller2_navn)
            print(spiller2_navn, "har : ",poengspiller2, "poeng", spiller1_navn, "har : ", poengspiller1)
            
    
        elif kortspiller1 > kortspiller2:
            poengspiller2 = poengspiller2 + 1
            print(spiller2_navn, "fikk høyere tall enn ", spiller1_navn)
            print(spiller2_navn, "har : ",poengspiller2, "poeng", spiller1_navn, "har : ", poengspiller1)
            
            
        elif poengspiller1 >= 10:
            print(spiller1_navn + "vant!")
             
        elif poengspiller2 >= 10:
            print(spiller2_navn + "vant!")
            return

        
    
#continue_playing = True
#while continue_playing:
#    if poengspiller1 >= 10:
#        continue_playing = False
#    elif poengspiller2 >= 10:
#        continue_playing = False
#    else:
#        play_game()

play_again = True
while play_again:
    play_game()
    play_again = input("Vil du starte en ny runde? (Ja/Nei): ") == "ja"
    

    

