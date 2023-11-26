# Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste

compte=0
L = [8, 24, 48, 2, 16]
for i in(L):
    if i % 3 == 0:
        compte=compte+1

print(compte)

