#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:16:32 2020

@author: utilisateur
"""

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def _set_case(self, case):
        
    def __str__(self):
        return '%s ,%s' % (self.x, self.y)

class Creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
    def __str__(self):
        return 'nom: ' +self.nom +', position: '+self.position
        
        
class Jeu:
    def _init__(self, listesDesCases, listeDesCreatures, tour, actif):
        self.listesDesCases = listesDesCases
        self.listeDesCreatures = listeDesCreatures
        self.tour = tour
        self.actif = actif
    def __str__(self):
        return 'Les cases : ' +self.listeDesCases +', Les Créatures : '+self.listeDesCreatures+ 'Le tour : ' +self.tour+ 'Activité : '+self.actif
    
