# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:53:03 2024

@author: cheml
"""

def afficher(p):
    for i in range(len(p)):
        if p[i] != 0:  # On ignore les termes avec coefficient nul
            if i == 0:
                print(f"{p[i]}*X^{len(p)-1-i}", end="")
            elif i != len(p)-1 and i != len(p)-2:
                print(f" + {p[i]}*X^{len(p)-1-i}", end="")
            elif i == len(p)-2:
                print(f" + {p[i]}*X", end="")
            else:
                print(f" + {p[i]}", end="")

        
        


def get_valeur(p, x):
    s = 0
    n = len(p) - 1  # Le degré du polynôme
    for i in range(len(p)):
        s += p[i] * (x ** (n - i))  # Calcul de la valeur du terme p[i] * x^(n-i)
    return s


    
def deriver(p):
    for i in range(len(p)):
        
        if i == 0:
            # Premier terme (sans signe "+")
            print(f"{(len(p)-1-i) * p[i]}*X^{len(p)-2-i}", end="")
        elif(i != len(p)-1 and i != len(p)-2):
            # Autres termes (avec "+" entre eux)
            print(f" + {(len(p)-1-i) * p[i]}*X^{len(p)-2-i}", end="")
        elif( i == len(p) -2 ) : 
            print(f"+ {p[i]}", end ="")
        else :
            print(' ',end ="")


    
# Exemple d'utilisation :

p = [3, 2, 1]  # Correspond à 3*X^2 + 2*X^1 + 1*X^0
afficher(p)
#deriver(p)
        
    # Exemple d'utilisation :
p = [3, 2, 1]
s = get_valeur(p , 1) # Correspond à 3*X^2 + 2*X^1 + 1*X^0
#print(s)