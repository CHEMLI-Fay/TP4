class polynome: 

    def __init__(self, P):
        self.P = P  # Utilisation cohérente de self.P pour stocker les coefficients

    def afficher(self):
        for i in range(len(self.P)):
            if self.P[i] != 0:  # Afficher uniquement les termes non nuls
                if i == 0:
                    print(f"{self.P[i]}*X^{len(self.P)-1-i}", end="")
                elif i != len(self.P)-1 and i != len(self.P)-2:
                    print(f" + {self.P[i]}*X^{len(self.P)-1-i}", end="")
                elif i == len(self.P)-2:
                    print(f" + {self.P[i]}*X", end="")
                else:
                    print(f" + {self.P[i]}", end="")
        print()  # Pour s'assurer que l'affichage passe à la ligne à la fin

    def get_valeur(self, x):
        s = 0
        n = len(self.P) - 1  # Le degré du polynôme
        for i in range(len(self.P)):  # Correction : Utilisation de self.P au lieu de self.p
            s += self.P[i] * (x ** (n - i))  # Calcul correct de chaque terme
        return s

# Exemple d'utilisation
poly = polynome([0.1, 0.1, -1.3, -0.1, 1.2])
poly.afficher()  # Affiche : 0.1*X^4 + 0.1*X^3 - 1.3*X^2 - 0.1*X + 1.2
s = poly.get_valeur(2)  # Calcul la valeur pour x = 2
print(s)  # Affiche le résultat de l'évaluation
