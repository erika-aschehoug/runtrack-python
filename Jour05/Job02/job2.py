def rectangle(width, height):      #je définis uhne fonction
    premiere_ligne= ("|"+"-"*(width-2)+"|")   # j'exprime ma première ligne qui est composée de un | et de - -2 car je retire les 2 | du début et de la fin
    print(premiere_ligne)               #j'imprime ma prmeière ligne
    deuxieme_ligne= ("|"+" "*(width-2)+"|")   #dans ma même fonction, je définis ma 2eme ligne
    i=0             #pour dire que je pars de 0
    while i< height-2:      #tant que i ne dépasse par ma hauteur (-2) pour les 2 | pour la premiere et la dernière ligne
        print(deuxieme_ligne)   #j'imprime une ligne par boucle (dépend de la hauteur)
        i+=1         # pour que ma boucle ne soit pas infini
    print(premiere_ligne) #j'imprime ma dernière ligne

rectangle(10, 3)    #j'appelle ma fonction