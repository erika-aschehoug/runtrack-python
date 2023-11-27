# Écrivez un programme qui supprime les doublons de la liste suivante :
# [10,20,30,20,10,50,60,40,80,50,40].

def suppr_doublons(input_list):
    print(f"Liste avant suppression des doublons : {liste}")
    unique_liste = []  # Liste pour stocker les éléments uniques
    for chiffre in input_list:
        if chiffre not in unique_liste:
            unique_liste += [chiffre]
    return unique_liste

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(f"Liste après suppression des doublons : {suppr_doublons(liste)}")