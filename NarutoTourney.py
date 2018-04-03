#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:00:52 2018

@author: Cisco
"""

import os
os.chdir("/Users/Cisco/Desktop/M1 EIF/S2/Intro Python/ProjetPython")

import TourneyFunctions as TF
import random as rd
import time

# Character initialization

class Genin():
    def __init__(self):
        self.name = None
        self.life = None
        self.attack = None
        self.defense = None
        self.agility = None
        self.opponents = None
        self.score = 0   
        self.x_coord = 0
        self.y_coord = 0
        self.symbol = None
        
participants = []

Naruto = Genin()
Naruto.name = "Naruto"
Naruto.defense = 60
Naruto.attack = 70
Naruto.agility = 70
Naruto.life = 100
Naruto.symbol = "N "
participants.append(Naruto)

Sasuke = Genin()
Sasuke.name = "Sasuke"
Sasuke.defense = 70
Sasuke.attack = 70
Sasuke.agility = 90
Sasuke.life = 70
Sasuke.symbol = "S "
participants.append(Sasuke)

Shikamaru = Genin()
Shikamaru.name = "Shikamaru"
Shikamaru.defense = 100
Shikamaru.attack = 40
Shikamaru.agility = 50
Shikamaru.life = 60
Shikamaru.symbol = "$ "
participants.append(Shikamaru)

Sakura = Genin()
Sakura.name = "Sakura"
Sakura.defense = 80
Sakura.attack = 60
Sakura.agility = 60
Sakura.life = 50
Sakura.symbol = "<3"
participants.append(Sakura)

Gaara = Genin()
Gaara.name = "Gaara"
Gaara.defense = 80
Gaara.attack = 50
Gaara.agility = 60
Gaara.life = 100
Gaara.symbol = "G "
participants.append(Gaara)

Choji = Genin()
Choji.name = "Choji"
Choji.defense = 40
Choji.attack = 90
Choji.agility = 40
Choji.life = 70
Choji.symbol = "O "
participants.append(Choji)

Tenten = Genin()
Tenten.name = "Tenten"
Tenten.defense = 70
Tenten.attack = 30
Tenten.agility = 70
Tenten.life = 40
Tenten.symbol = "T "
participants.append(Tenten)

Neji = Genin()
Neji.name = "Neji"
Neji.defense = 60
Neji.attack = 50
Neji.agility = 90
Neji.life = 70
Neji.symbol = ":|"
participants.append(Neji)

RockLee = Genin()
RockLee.name = "Rock Lee"
RockLee.defense = 40
RockLee.attack = 90
RockLee.agility = 90
RockLee.life = 70
RockLee.symbol = "R "
participants.append(RockLee)

Kankuro = Genin()
Kankuro.name = "Kankuro"
Kankuro.defense = 70
Kankuro.attack = 70
Kankuro.agility = 50
Kankuro.life = 80
Kankuro.symbol = "K "
participants.append(Kankuro)

Ino = Genin()
Ino.name = "Ino"
Ino.defense = 60
Ino.attack = 50
Ino.agility = 50
Ino.life = 50
Ino.symbol = "I "
participants.append(Ino)

Shino = Genin()
Shino.name = "Shino"
Shino.defense = 80
Shino.attack = 30
Shino.agility = 60
Shino.life = 60
Shino.symbol = ":{"
participants.append(Shino)

Hinata = Genin()
Hinata.name = "Hinata"
Hinata.defense = 70
Hinata.attack = 30
Hinata.agility = 50
Hinata.life = 40
Hinata.symbol = ":("
participants.append(Hinata)

Kiba = Genin()
Kiba.name = "Kiba"
Kiba.defense = 70
Kiba.attack = 70
Kiba.agility = 50
Kiba.life = 80
Kiba.symbol = ":D"
participants.append(Kiba)

Rin = Genin()
Rin.name = "Rin"
Rin.defense = 80
Rin.attack = 20
Rin.agility = 40
Rin.life = 50
Rin.symbol = "oO"
participants.append(Rin)

Kago = Genin()
Kago.name = "Kago"
Kago.defense = 80
Kago.attack = 60
Kago.agility = 40
Kago.life = 30
Kago.symbol = "=3"
participants.append(Kago)

Naruto.opponents = [genin for genin in participants if genin.name != Naruto.name]
Sasuke.opponents = [genin for genin in participants if genin.name != Sasuke.name]
Shikamaru.opponents = [genin for genin in participants if genin.name != Shikamaru.name]
Sakura.opponents = [genin for genin in participants if genin.name != Sakura.name]
Gaara.opponents = [genin for genin in participants if genin.name != Gaara.name]
Choji.opponents = [genin for genin in participants if genin.name != Choji.name]
Tenten.opponents = [genin for genin in participants if genin.name != Tenten.name]
Neji.opponents = [genin for genin in participants if genin.name != Neji.name]
RockLee.opponents = [genin for genin in participants if genin.name != RockLee.name]
Kankuro.opponents = [genin for genin in participants if genin.name != Kankuro.name]
Ino.opponents = [genin for genin in participants if genin.name != Ino.name]
Shino.opponents = [genin for genin in participants if genin.name != Shino.name]
Hinata.opponents = [genin for genin in participants if genin.name != Hinata.name]
Kiba.opponents = [genin for genin in participants if genin.name != Kiba.name]
Rin.opponents = [genin for genin in participants if genin.name != Rin.name]
Kago.opponents = [genin for genin in participants if genin.name != Kago.name]    

Tourney = TF.InitializeTree(participants)

TF.InitTourney(participants)

TourneyRound = 1

# boucle définissant chaque round
while len(Tourney) > 1: 
    # boucle pour le round (sur les participants)
    if TourneyRound < 4:
        print("Round %s ! \n" % TourneyRound)
    else:
        print("Combat final ! \n")
        time.sleep(5)
    
    combats = TF.SplitTourney(Tourney)
    
    n = len(combats)
    for i in range(n):
        
        compteur_combats = 1
        
        genin1 = combats[i][0]
        genin2 = combats[i][1]
        print("%s (%s)vs %s (%s) ! \n" %(genin1.name, genin1.symbol.strip(" "), genin2.name, genin2.symbol.strip(" ")))
        # boucle combat (while genin1.life > 0 and genin2.life > 0)
        attaquant = rd.randint(0,1)
        combattants = [genin1, genin2]
        degat = 0
        esquive = False
        ind_crit = False
        outputCombat = [combattants, degat, esquive, attaquant, ind_crit]
        
        life1 = genin1.life
        life2 = genin2.life
        
        # Initialisation de l'affiche
        genin1.x_coord = 2
        genin1.y_coord = 3
        
        genin2.x_coord = 3
        genin2.y_coord = 3
        
        TF.Show(genin1, genin2)
        
        # combat
        while genin1.life > 0 and genin2.life > 0:
            # dégat / esquive
            attaquant = outputCombat[3]
            #outputCombat = TF.combat(genin1, genin2, attaquant)
            time.sleep(0.5)

            outputCombat = TF.combat(genin1, genin2, attaquant)
            
            if outputCombat[2] == True:
                print("%s a esquivé ! \n" % outputCombat[0][int(not(attaquant))].name)
                # Afficher
                possibilties = [[outputCombat[0][int(attaquant)].x_coord + 1, outputCombat[0][int(attaquant)].y_coord],
                                [outputCombat[0][int(attaquant)].x_coord, outputCombat[0][int(attaquant)].y_coord - 1],
                                [outputCombat[0][int(attaquant)].x_coord, outputCombat[0][int(attaquant)].y_coord + 1]]
                index = rd.randint(0,2)
                while possibilties[index][0] < 0 or possibilties[index][0] > 6 or possibilties[index][1] < 0 or possibilties[index][1] > 6:
                    index = rd.randint(0,2)
                
                outputCombat[0][int(not(attaquant))].x_coord = possibilties[index][0]
                outputCombat[0][int(not(attaquant))].y_coord = possibilties[index][1]
                
                TF.Show(outputCombat[0][int(attaquant)], outputCombat[0][int(not(attaquant))])
                
            else:
                if outputCombat[4] == False:
                    print("%s a infligé %d de dégat !" %(outputCombat[0][int(attaquant)].name, outputCombat[1])) 
                else:
                    print("%s a porté un coup critique ! Dégat : %d" %(outputCombat[0][int(attaquant)].name, outputCombat[1]))
         
        if genin1.life <= 0 and genin2.life > 0:
            # genin2 a gagné le combat
            genin2.score += 1
            print("Le gagnant est %s !" % genin2.name )
            print("\n \n")
            genin2.life = life2

        elif genin2.life <= 0 and genin1.life > 0:
            # genin1 a gangé le combat
            genin1.score += 1
            print("Le gagnant est %s !" %genin1.name)
            print("\n \n")
            genin1.life = life1
        
        else:
            # ils se sont entretués
            print("Les deux genin sont morts !")
            print("\n \n")
        
        print("Fin du combat")
        print("Continuer ?")
        input()
        
        # nettoyage après combat console
        TF.ClearScreen()
            
    Tourney = TF.ActualizeTree(Tourney)
    
    print("Fin du Round %s !" %TourneyRound )
    print("Les gagnants sont :")
    gagnants = []
    for genin in Tourney:
        gagnants.append(genin.name)
    print(gagnants)
    input("Tapper Enter pour contineur...")
    n = len(Tourney)
    
        
    TourneyRound += 1

print("Le champion est %s !" %Tourney[0].name)

        

