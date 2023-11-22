# Créez une fonction nommée "moyenne" qui prend en paramètre trois notes et retourne
# la moyenne de ces notes.
# Demandez à l'utilisateur de saisir trois notes, puis enregistrez le résultat de la fonction
# "moyenne" dans une variable appelée "moyenne_etudiant".

# Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
# ➔ Très bon élève si la moyenne est comprise entre 20 et 15.
# ➔ Bon élève si la moyenne est comprise entre 14 et 11.
# ➔ Élève moyen si la moyenne est comprise entre 10 et 8.
# ➔ Élève devant faire des efforts si la moyenne est comprise entre 0 et 7.

def moyenne(a, b, c):
    return (a+b+c)/3

a=float(input("note1: "))
b=float(input("note2: "))
c=float(input("note3: "))

moyenne_etudiant= moyenne(a, b, c)
print("lamoyenne de l'étudiant est", moyenne_etudiant)

if moyenne_etudiant>15 and moyenne_etudiant<20:
    print ("très bon élève")
elif moyenne_etudiant>11 and moyenne_etudiant <14:
    print("bon élève")
elif moyenne_etudiant>10 and moyenne_etudiant <8:
    print("eleve moyen") 
elif moyenne_etudiant>7 and moyenne_etudiant <0:
    print("faire des efforts")  

