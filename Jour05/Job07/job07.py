import math

notes=list(range(101))       #note de 0 a 100
n=(66, 26, 35, 48, 96)      #ma liste de note

def note(n):
    for i in range (len(n)):
        if n[i] > 40:
            print(f"L'élève a réussi le test avec une note de {n[i]}")
        else:
            print(f"L'élève a échoué au test avec une note de {n[i]}")

note(n)

def arrondi(note_base):
    return math.ceil(((note_base) - 3)/ 5) * 5

note_base=len(n)

liste_note_arrondie=[arrondi(note)for note in n]

print(f"note initiale {n}")
print(f"note arrondie {liste_note_arrondie}")