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
print("-"*50)
print("Bienvenue dans la bataille")
pts_vie=100
pts_attaque=20
pts_defense=15
pts_joueur= pts_vie
pts_joueur= pts_vie

def points_vies(pts_vie):
    """
    fonction qui reçoit des point de vie
    :return:
    """
    return points_vies(pts_vie)

    pass
def points_attaques(pts_attaque):
    """fonction de defense

    return:"""
    return points_attaques(pts_attaque)

def points_defenses(pts_defense):
    """fonction de defense"""
    return points_defenses(pts_defense)

def fonction_joueur1():
    """fonction pour le joueur 1"""
    return
def fonction_joueur2():
    """fonction pour le joueur 2"""
    pass
def combat():
    if fonction_joueur1() > fonction_joueur2():
        print("Joueur 1 reporte la partie la partie")
    elif fonction_joueur1() == fonction_joueur2():
        print("Les joueurs sont a égalité")
    elif fonction_joueur1() < fonction_joueur2():
        print("Le Joueur 2 remporte la partie")
    else:
        print("le joueur")
        print("")

print("-"*50)

#----------------------------------------FONCTION DE VANN SOVANNTHANANT----------------------------------------

def pourcentage_colorer(pourcentage):
    if pourcentage >=100:
        print("La pièce est déja été colorer a 100% avec cette couleur.")
    elif pourcentage <=100:
        pourcentage += 25
    return pourcentage

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