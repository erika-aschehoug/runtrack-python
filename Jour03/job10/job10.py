# Créer une fonction qui vérifie que le nombre est pair ou impair.
# Penser à vérifier si le nombre est bien un chiffre entier et positif. Appeler cette fonction
# plusieurs fois avec des valeurs différentes.


def paire_impair(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("le nombre est paire")
        else:
            print("le nombre est impaire")
    else:
        print("Entrer un nombre entier et positif")

paire_impair (7)
paire_impair (5)
paire_impair (-3)
paire_impair (2)
paire_impair (8)