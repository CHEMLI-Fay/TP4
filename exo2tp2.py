# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:51:05 2024

@author: cheml
"""

def afficher_grille(grille):
    for v in grille:
        for m in v:
            if m == 1:
                print('X', end=' ')  # Jeton du joueur 1
            elif m == 2:
                print('O', end=' ')  # Jeton du joueur 2
            else:
                print('.', end=' ')  # Case vide
        print()  # Passer à la ligne suivante après avoir affiché une ligne entière


"""def jouer(grille, joueur , colonne ):
    for v in grille : 
        for m in v :
            if (grille[0][colonne != 0 ]) :
                return False
            elif joueur == 1  : 
                print('X', end=' ')  # Jeton du joueur 1
            elif joueur == 2:
                print('O', end=' ')
            else : 
                print('.')
                return True
        print() """

def jouer(grille, joueur, colonne):
    # Vérifie si la colonne est valide
    if colonne < 0 or colonne >= len(grille[0]):
        return False

    # Vérifie si la case en haut de la colonne est occupée
    if grille[0][colonne] != 0:
        return False

    # Parcourt la colonne de bas en haut pour trouver une case vide
    for i in range(len(grille) - 1, -1, -1):  # De la dernière ligne à la première
        if grille[i][colonne] == 0:  # Si la case est vide
            grille[i][colonne] = joueur  # Place le jeton du joueur
            return True  # Retourne True car le coup a été joué avec succès

    return False  # Retourne False si aucune case n'est vide (cela ne devrait pas arriver grâce à la vérification initiale)

    

    
    
    
# Exemple de création d'une grille 6x7
grille = [
    [0, 0, 0, 0, 0, 0, 0],  # Ligne 1 (vide)
    [0, 1, 0, 0, 0, 0, 2],  # Ligne 2 (1 jeton du joueur 1, 1 jeton du joueur 2)
    [0, 0, 1, 0, 2, 0, 0],  # Ligne 3 (1 jeton du joueur 1, 1 jeton du joueur 2)
    [0, 0, 0, 2, 0, 0, 0],  # Ligne 4 (1 jeton du joueur 2)
    [1, 0, 0, 0, 0, 0, 0],  # Ligne 5 (1 jeton du joueur 1)
    [0, 0, 0, 0, 0, 0, 0]   # Ligne 6 (vide)
]

# Affichage de la grille
#afficher_grille(grille)
#print(jouer(grille, 2 , 2))
afficher_grille(grille)
