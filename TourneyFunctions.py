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
def combat(genin1, genin2):
    attaquant = rd.randint(0,1)

    combattants = [genin1, genin2]
    
    
    combattants = [genin1, genin2]

    while genin1.life > 0 and genin2.life > 0:
        # a chaque tour un seul tape, l'autre se défend
       
        # est-ce que le défenseur esquive ? 
        var = combattants[int(not(attaquant))] * 4 / 100
        proba_esquive = n.random.normal(0,var)

        if s.norm.cdf(proba_esquive, 0, var) > 0.7:
            esquive = True
        else:
            esquive = False
        
        if not(esquive):
            # combien l'attaquant inflige comme dégât ?
            proba_critique = rd.uniform(0,1)
            mult = rd.uniform(0.8, 1.2)
            if proba_critique > 0.9:
                critique = rd.randint(5,10)
            else:
                critique = 0
                
            degat = m.floor(( (combattants[attaquant].attack * 10) / combattants[int(not(attaquant))].defense ) * mult + critique)

            # mettre à jour les points de vie du joueur
            combattants[int(not(attaquant))].life = combattants[int(not(attaquant))].life - degat 
        
        # on change de tour
        attaquant = int(not(attaquant))
                
    for genin in combattants:
        if genin.life != 0: 
            return genin
        

# fonction définissant l'arbre du tournoi
    # l'arbre sera en fait une liste, qui commencera avec tous les participants et
    # de laquelle on enlèver les perdants à chaque round. A la fin ce sera un singleton.
def InitializeTree(participants):
    Tourney = list(participants)
    rd.shuffle(Tourney)
    return Tourney
            
def ActualizeTree(Tourney, perdants):
    for genin in perdants:
        Tourney.remove(genin)
    return Tourney

# fonction interface (afficher)
    # gameboard, mouvements, actions...
