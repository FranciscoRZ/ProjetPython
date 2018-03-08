#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:13:11 2018

@author: Cisco
"""

# Création de l'arbre du tournoi
    # 10 combatants, qui s'entrecombattent deux à deux 
class Tourney():
    def __init__(self):
        self.comb1 = None
        self.comb2 = None
        self.comb3 = None
        self.comb4 = None
        self.comb5 = None
        self.comb6 = None
        self.comb7 = None
        self.comb8 = None
        self.comb9 = None
        self.comb10 = None
        self.name = None
        self.score = None
        self.opponents = None

Combattants = []

ChuninExam = Tourney()
ChuninExam.name = "Champion"

ChuninExam.comb1 = Tourney()
ChuninExam.comb1.name = "Naruto"
Combattants.append(ChuninExam.comb1.name)
 
ChuninExam.comb2 = Tourney()
ChuninExam.comb2.name = "Sasuke"
Combattants.append(ChuninExam.comb2.name)

ChuninExam.comb3 = Tourney()
ChuninExam.comb3.name = "Shino"
Combattants.append(ChuninExam.comb3.name)

ChuninExam.comb4 = Tourney()
ChuninExam.comb4.name = "Sakura"
Combattants.append(ChuninExam.comb4.name)

ChuninExam.comb5 = Tourney()
ChuninExam.comb5.name = "Gaara"
Combattants.append(ChuninExam.comb5.name)

ChuninExam.comb6 = Tourney()
ChuninExam.comb6.name = "Choji"
Combattants.append(ChuninExam.comb6.name)

ChuninExam.comb7 = Tourney()
ChuninExam.comb7.name = "Tenten"
Combattants.append(ChuninExam.comb7.name)

ChuninExam.comb8 = Tourney()
ChuninExam.comb8.name = "Neji"
Combattants.append(ChuninExam.comb8.name)

ChuninExam.comb9 = Tourney()
ChuninExam.comb9.name = "RockLee"
Combattants.append(ChuninExam.comb9.name)

ChuninExam.comb10 = Tourney()
ChuninExam.comb10.name = "Kankuro"
Combattants.append(ChuninExam.comb10.name)

ChuninExam.comb1.opponents = [genin for genin in Combattants if genin != ChuninExam.comb1.name]
ChuninExam.comb2.opponents = [genin for genin in Combattants if genin != ChuninExam.comb2.name]
ChuninExam.comb3.opponents = [genin for genin in Combattants if genin != ChuninExam.comb3.name]
ChuninExam.comb4.opponents = [genin for genin in Combattants if genin != ChuninExam.comb4.name]
ChuninExam.comb5.opponents = [genin for genin in Combattants if genin != ChuninExam.comb5.name]
ChuninExam.comb6.opponents = [genin for genin in Combattants if genin != ChuninExam.comb6.name]
ChuninExam.comb7.opponents = [genin for genin in Combattants if genin != ChuninExam.comb7.name]
ChuninExam.comb8.opponents = [genin for genin in Combattants if genin != ChuninExam.comb8.name]
ChuninExam.comb9.opponents = [genin for genin in Combattants if genin != ChuninExam.comb9.name]
ChuninExam.comb10.opponents = [genin for genin in Combattants if genin != ChuninExam.comb10.name]

