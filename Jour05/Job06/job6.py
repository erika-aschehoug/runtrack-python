marche=100
hauteur=5
resultat=0

def trajet(x,y):
    
    z=x*(y/100)*5*2*7
    return z

resultat=trajet(marche,hauteur)
print(f"Il effectue {resultat} m par semaine pour aller aux toilettes.")