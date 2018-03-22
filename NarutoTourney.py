#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:00:52 2018

@author: Cisco
"""

import TourneyFunctions

# Character initialization

class Genin():
    def __init__(self):
        self.name = None
        self.life = None
        self.attack = None
        self.defense = None
        self.agility = None
        self.opponents = None
        self.score = None    

participants = []

Naruto = Genin()
Naruto.name = "Naruto"
Naruto.defense = 60
Naruto.attack = 70
Naruto.agility = 70
Naruto.life = 100
participants.append(Naruto.name)

Sasuke = Genin()
Sasuke.name = "Sasuke"
Sasuke.defense = 70
Sasuke.attack = 70
Sasuke.agility = 90
Sasuke.life = 70
participants.append(Sasuke.name)

Shikamaru = Genin()
Shikamaru.name = "Shikamaru"
Shikamaru.defense = 100
Shikamaru.attack = 40
Shikamaru.agility = 50
Shikamaru.life = 60
participants.append(Shikamaru.name)

Sakura = Genin()
Sakura.name = "Sakura"
Sakura.defense = 80
Sakura.attack = 60
Sakura.agility = 60
Sakura.life = 50
participants.append(Sakura.name)

Gaara = Genin()
Gaara.name = "Gaara"
Gaara.defense = 80
Gaara.attack = 50
Gaara.agility = 60
Gaara.life = 100
participants.append(Gaara.name)

Choji = Genin()
Choji.name = "Choji"
Choji.defense = 40
Choji.attack = 90
Choji.agility = 40
Choji.life = 70
participants.append(Choji.name)

Tenten = Genin()
Tenten.name = "Tenten"
Tenten.defense = 70
Tenten.attack = 30
Tenten.agility = 70
Tenten.life = 40
participants.append(Tenten.name)

Neji = Genin()
Neji.name = "Neji"
Neji.defense = 60
Neji.attack = 50
Neji.agility = 90
Neji.life = 70
participants.append(Neji.name)

RockLee = Genin()
RockLee.name = "Rock Lee"
RockLee.defense = 40
RockLee.attack = 90
RockLee.agility = 90
RockLee.life = 70
participants.append(RockLee.name)

Kankuro = Genin()
Kankuro.name = "Kankuro"
Kankuro.defense = 70
Kankuro.attack = 70
Kankuro.agility = 50
Kankuro.life = 80
participants.append(Kankuro.name)

Ino = Genin()
Ino.name = "Ino"
Ino.defense = 60
Ino.attack = 50
Ino.agility = 50
Ino.life = 50
participants.append(Ino.name)

Shino = Genin()
Shino.name = "Shino"
Shino.defense = 80
Shino.attack = 30
Shino.agility = 60
Shino.life = 60
participants.append(Shino.name)

Hinata = Genin()
Hinata.name = "Hinata"
Hinata.defense = 70
Hinata.attack = 30
Hinata.agility = 50
Hinata.life = 40
participants.append(Hinata.name)

Kiba = Genin()
Kiba.name = "Kankuro"
Kiba.defense = 70
Kiba.attack = 70
Kiba.agility = 50
Kiba.life = 80
participants.append(Kiba.name)

Rin = Genin()
Rin.name = "Rin"
Rin.defense = 80
Rin.attack = 20
Rin.agility = 40
Rin.life = 50
participants.append(Rin.name)

Kago = Genin()
Kago.name = "Kago"
Kago.defense = 80
Kago.attack = 60
Kago.agility = 40
Kago.life = 30
participants.append(Kago.name)

Naruto.opponents = [genin for genin in participants if genin != Naruto.name]
Sasuke.opponents = [genin for genin in participants if genin != Sasuke.name]
Shikamaru.opponents = [genin for genin in participants if genin != Shikamaru.name]
Sakura.opponents = [genin for genin in participants if genin != Sakura.name]
Gaara.opponents = [genin for genin in participants if genin != Gaara.name]
Choji.opponents = [genin for genin in participants if genin != Choji.name]
Tenten.opponents = [genin for genin in participants if genin != Tenten.name]
Neji.opponents = [genin for genin in participants if genin != Neji.name]
RockLee.opponents = [genin for genin in participants if genin != RockLee.name]
Kankuro.opponents = [genin for genin in participants if genin != Kankuro.name]
Ino.opponents = [genin for genin in participants if genin != Ino.name]
Shino.opponents = [genin for genin in participants if genin != Shino.name]
Hinata.opponents = [genin for genin in participants if genin != Hinata.name]
Kiba.opponents = [genin for genin in participants if genin != Kiba.name]
Rin.opponents = [genin for genin in participants if genin != Rin.name]
Kago.opponents = [genin for genin in participants if genin != Kago.name]    



