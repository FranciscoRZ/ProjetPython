#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:14 2018

@author: Cisco
"""
import random as rd

# fonction combat


# fonction définissant l'arbre du tournoi
    # l'arbre sera en fait une liste, qui commencera avec tous les participants et
    # de laquelle on enlèver les perdants à chaque round. A la fin ce sera un singleton.
def InitializeTree(participants):
    Tourney = participants
    rd.shuffle(Tourney)
    return Tourney
            
def ActualizeTree(Tourney, perdants):
    for chunin in perdants:
        Tourney.remove(perdants)
    return Tourney


# fonction interface (afficher)
    # gameboard, mouvements, actions...
