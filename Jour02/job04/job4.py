n=int(input("tapez la valeur:"))
print("table de la valeur saisie", n, "est:")

for i in range(1, n+1):
    print(f"la table de {i}:")
    for j in range(1, 11):
        resultat = i * j
        print(f" {i} * {j} = {resultat} ")