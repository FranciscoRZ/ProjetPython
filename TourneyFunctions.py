#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:14 2018

@author: Cisco
"""


import random as rd
import math as m
import numpy as n
import scipy.stats as s

# fonction combat
def combat(genin1, genin2, attaquant):

    combattants = [genin1, genin2]
    ind_crit = False
    
    # a chaque tour un seul tape, l'autre se défend
       
    # est-ce que le défenseur esquive ? 
    var = combattants[int(not(attaquant))].agility * 4 / 100
    proba_esquive = n.random.normal(0,var)
    degat = 0
    
    if s.norm.cdf(proba_esquive, 0, var) > 0.7:
        esquive = True
    else:
        esquive = False
    
    # si le défenseur n'esquive pas
    if not(esquive):
        # combien l'attaquant inflige comme dégât ?
        proba_critique = rd.uniform(0,1)
        mult = rd.uniform(0.8, 1.2)
        if proba_critique > 0.9:
            critique = rd.randint(5,10)
            ind_crit = True
        else:
            critique = 0
            ind_crit = False
            
        degat = m.floor(( (combattants[attaquant].attack * 10) / combattants[int(not(attaquant))].defense ) * mult + critique)

        # mettre à jour les points de vie du joueur
        combattants[int(not(attaquant))].life = combattants[int(not(attaquant))].life - degat 
    
    # on change de tour
    attaquant = int(not(attaquant))
          
    return [combattants, degat, esquive, attaquant, ind_crit]
        
        

# fonction définissant l'arbre du tournoi
    # l'arbre sera en fait une liste, qui commencera avec tous les participants et
    # de laquelle on enlèver les perdants à chaque round. A la fin ce sera un singleton.
def InitializeTree(participants):
    Tourney = list(participants)
    rd.shuffle(Tourney)
    return Tourney            

# fonction enlevant les perdants de l'arbre du tournoi à chaque round
def ActualizeTree(Tourney):
    # for genin in Tourney:
    #    if genin.life <= 0:
    #        Tourney.remove(genin)
    #return Tourney
    n = len(Tourney)
    perdants = []
    for i in range(n):
        if Tourney[i].life <= 0:
            perdants.append(Tourney[i])
    for genin in perdants:
        Tourney.remove(genin)
    return Tourney

# fonction nettoyant la console
def ClearScreen():
    import platform as pt
    import subprocess as sp
    
    if pt.system() == 'Windows':
        tmp = sp.call('cls', shell = True)
    elif pt.system() == 'Linux':
        tmp = sp.call('clear', shell = True)
    elif pt.system() == 'Darwin':
        tmp = sp.call('clear', shell = True)
    
    return

# fonction interface (afficher)
def Show(genin1, genin2):
    
    gb = [["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "],
          ["/ ","/ ","/ ","/ ","/ ","/ ","/ "]]
    
    x1 = genin1.x_coord
    y1 = genin1.y_coord
    
    x2 = genin2.x_coord
    y2 = genin2.y_coord
    
    gb[y1][x1] = genin1.symbol
    gb[y2][x2] = genin2.symbol
    
    for x in gb:
        print(x)
    print("\n")
    
    return

# fonction présentant le programme et expliquant le déroulement
def InitTourney(participants):
    
    import TourneyFunctions as TF
    
    print("Bienvenue aux examens Chûnin ! \n")
    print("Cette année nous avons %s participants dans le tournoi." % len(participants))
    print("Les genins sont : ")
    for genin in participants:
        print(genin.name)
    print("\n")
    print("Le tournoi se déroule en 4 rounds. A chaque round les genin s'affrontent deux à deux, à la mort ou à l'épuisement.")
    print("A la fin un seul champion sera déclaré.")
    print("Etes-vous prêts ? (Tapper Enter pour commencer la simulation)")
    input()
    
    TF.ClearScreen()
    
    return

# fonction retournant les combats à avoir à chaque round
def SplitTourney(Tourney):
    combats = []
    k = 0
    while k < len(Tourney):
        combats.append([Tourney[k], Tourney[k + 1]])
        k += 2
    return combats
