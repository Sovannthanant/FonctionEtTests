# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""

"""
2. Fonction qui reçoit une liste de legos et une couleur et qui le pourcentage de blocs de cette couleur
"""

"""
3. Fonction qui reçoit une liste de legos et qui il y a combien de blocs de chaque couleur en moyenne
"""

# Répartition des tâches :
"""                     a   b   c
Nom :                   1   2   3
Nom :                   2   3   1
Nom :                   3   1   2
"""

#===========================FONCTION DE LAMARANA===========================
"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""

import random

print("-"*50)
print("Bienvenue dans la bataille")
#Initialisation des points
pts_joueur1 = 100
pts_joueur2 = 100

#Defense et attaque aléatoire
#la fonciton randint choisi des nombre la syntaxe est la suivante

pts_defense1 = random.randint(1, 20)
pts_defense2 = random.randint(1, 20)
attaque1 = random.randint(1, 20)
attaque2 = random.randint(1, 20)
def combat(pts_joueur1,pts_joueur2,pts_defense1,pts_defense2,attaque1,attaque2):
    compteur = 0
    while True:
        if attaque1 > 0 and attaque2 > 0:
            print(f"Tour {compteur + 1}")
        print(f"Attaque Joueur 1: {attaque1} | Défense Joueur 2: {pts_defense2}")
        print(f"Attaque Joueur 2: {attaque2} | Défense Joueur 1: {pts_defense1}")

        if attaque1>0 and attaque2>0:
            return f"Je me defends:{pts_joueur2 - attaque1 and attaque2 or pts_defense2}"
            return f""
        elif attaque2 >attaque1:
            return f"Je me defends:{pts_joueur1-attaque2 and attaque1 or pts_defense1}"
        compteur+=1

if __name__ == '__main__':
    pts_joueur1,pts_joueur2=combat(pts_joueur1,pts_joueur2,pts_defense1,pts_defense2,attaque1,attaque2)

print("-"*50)

import random

legos=["lego1","lego2","lego3","lego4"]
couleurs=["rouge", "jaune","vert","bleu"]
pourcentage=["1%","2%","3%,4%"]
def liste_code(legos,couleurs,pourcentage,):
    #Entrer les données suivantes:

    choix_lego=random.choice(legos)
    choix_couleur=random.choice(couleurs)
    choix_pourcentage=random.choice(pourcentage)
    print(f"Le lego choisi est: {choix_lego}")
    print(f"La couleur choisi est: {choix_couleur}")
    print(f"Le lego choisi est: {choix_pourcentage}")
       for lego in legos:
           if choix_lego = lego:



#----------------------------------------FONCTION DE VANN SOVANNTHANANT----------------------------------------
<<<<<<< HEAD
"""
#def colorer_lego():
=======

def pourcentage_colorer(pourcentage):
    if pourcentage >=100:
        print("La pièce est déja été colorer a 100% avec cette couleur.")
    elif pourcentage <=100:
        pourcentage += 25
    return pourcentage
>>>>>>> origin/master

#Une liste avec des pièces de légos.
pourcentage = 0
liste_legos = ["lego 1x1x1","lego 1x2x2","lego 1x2x4"]
print(f"Lego disponibles: {liste_legos}.")

#Choisir une couleur pour peinturer.
while True:
    couleur = str.lower(input("Qu'elle couleur voulez vous appliquer? "))
    piece = input("Quelle pièce de légos voulez vous peinturez? ")
    pourcentage = pourcentage_colorer(pourcentage)
    print(f"{piece} et colorer de {couleur} à {pourcentage}%.")
    continuer = bool(int(input("Apuyez 1 pour continuer à peinturer: ")))
    if continuer == True:
        continue
    else:
        break


print("-"*50)
"""






