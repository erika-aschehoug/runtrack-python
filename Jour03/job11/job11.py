# Créer une fonction nommée “time_to_text” qui prend en paramètre un nombre entier de
# minutes et affiche en console une chaine de caractère sous la forme de “X heures et Y
# minutes”.

def time_to_next(minute):
    heures = int(minute/60)
    minute_restante = int(minute % 60)
    return (f"{heures} heures et {minute_restante} minutes")


print (time_to_next (68))
print (time_to_next (167))
print (time_to_next (250))
print (time_to_next (432))