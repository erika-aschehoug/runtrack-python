#gain initial
montant_investissement=1500
taux_rendement=15
gain=(montant_investissement*taux_rendement)/100
print(gain)

#gain après augmentation du capital
ajout_investissement=float(montant_investissement+5000+gain)
augmentation_taux=float(taux_rendement+2)
nouveaugain=(ajout_investissement*augmentation_taux)/100
print(nouveaugain)


#gain après diminution de 10%
derniermontant=(ajout_investissement+nouveaugain)
après_retrait=(derniermontant)-(derniermontant*10/100)
réductiontaux=augmentation_taux-1
gain_final=(après_retrait*réductiontaux)/100
print (gain_final)

