#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:16:32 2020

@author: utilisateur
"""
import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
#    def _set_x(self, x):
#        x1 = str(x)
#        if x1.isnumeric():
#            self._x = int(x1)
#    def _get_x(self):
#        return self._x
#    x = property(_get_x,_set_x)
#    
#    def _set_y(self, y):
#        y1 = str(y)
#        if y1.isnumeric():
#            self._y = int(y1)
#    def _get_y(self):
#        return self._y    
#    y = property(_get_y,_set_y)  
    
    def adjacentes(self, jeu):
        ''' trouve les cases adjacentes à la case de l'objet jeu de Jeu'''
        self.caseAdj = []
        xpos= [0, +1, -1]
        
        adj = [[(i,j) for i in xpos]for j in xpos]
        op = [item for sublist in adj for item in sublist]
                
        for i in range(1,len(op)):
            self.caseAdj.append(Case(jeu.x+op[i][0], jeu.y+op[i][1]))
        return self.caseAdj
    
#    def __eq__(self,other):
#        return (self.x == other.x and self.y == other.y)
    
    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)
    
class Creature:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
    
    def _set_nom(self, nom):
        self._nom = str(nom).upper()
    def _get_nom(self):
        return  self._nom   
    nom = property(_get_nom,_set_nom )        
      
    def _set_position(self, position):
        self._position = position
    def _get_position(self):
        return  self._position   
    position = property( _get_position,_set_position)  
    
    def choisirCible(self,jeu): 
        ''' Choisir la cible = choisir la case où aller parmi les cases 
        adjacentes définies dans la classe Case''' 
        for pos in self.position.adjacentes(jeu):
            if jeu.estOccupee(jeu):
                return pos
            else:
                return random.choice(self.position.adjacentes(jeu))
        

    def __str__(self):
        return 'nom: ' +self.nom +', position: '+self.position
        
        
class Jeu(Case):
    def _init__(self, x,y, listesDesCases, listeDesCreatures, tour, actif):
        Case.__init__(x,y)
        self.listesDesCases = listesDesCases
        self.listeDesCreatures = listeDesCreatures
        self.tour = 1
        self.actif = actif
        
    def _set_listesDesCases(self, listesDesCases):
        if str(type(listesDesCases)) == "<class 'list'>":
            self._listesDesCases = listesDesCases
    def _get_listesDesCases(self):
        return  self._listesDesCases   
    listesDesCases = property(_get_listesDesCases,_set_listesDesCases )  
      
    def _set_listeDesCreatures(self, listeDesCreatures):
        if str(type(listeDesCreatures)) == "<class 'list'>":
            self._listeDesCreatures = listeDesCreatures
    def _get_listeDesCreatures(self):
        return  self._listeDesCreatures   
    listeDesCreatures = property(_get_listeDesCreatures,_set_listeDesCreatures)
    
    def _set_tour(self, tour):
        self._tour = tour
    def _get_tour(self):
        return  self._tour   
    tour = property(_get_tour,_set_tour)  

    def _set_actif(self, actif):
        self._actif = actif
    def _get_actif(self):
        return  self._actif   
    actif = property(_get_actif,_set_actif)  
    
    
    def estOccupee(self, case):
        ''' une case est occupée si ses coordonnées (x et y) coincident avec
            les coordonnées de la position de l'une des créatures dans la liste de créatures '''
        res = any((creature.position.x == case.x and creature.position.y == case.y) for creature in self.listeDesCreatures)
        return res
        
    def deplacer(self, creature, case):
        ''' si la case est occupée, la créature va prendre cette place et gagner
            sinon, sa position devient celle de la case et c'est le tour d'une autre créature.
            J'ai fait le choix de séléctionner aléatoirement de la liste cette autre créature '''
        if self.estOccupee(case):
            self.tour = 0 
            statement = "Le vainqueur est :"+creature.nom   
        else:
           self.tour += 1 
           self.actif = random.choice([x for x in self._listeDesCreatures if x != creature])
           statement = ""
        creature.position = case
        return print(statement)
        
    def __str__(self):
        return 'Tour : %s, Créature active : %s' % (self.tour, self._actif.nom)
    
    
# Initialisation du plateau
plateau =[[Case(i,j) for i in range(4)] for j in range(4)]
# Définition des créatures du jeu
creatures = [Creature('Bruna', plateau[0][0]), Creature('Hakila', plateau[3][3])]        

# Le jeu commence !

# initialisation :
init = Jeu(creatures[0].position.x, creatures[0].position.y)
init.listeDesCreatures = creatures
init.listeDesCases = plateau
init.actif = creatures[0]
init.tour=1

# Lancement du jeu
while init.tour != 0:
    print('Tour :', init.tour)
    # choix de cible
    cible = init.actif.choisirCible(init)
    # déplacement vers la cible
    init.deplacer(init.actif, cible)