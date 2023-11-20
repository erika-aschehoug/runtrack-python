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
retrait_10_pourcent=(ajout_investissement-10)
baissetaux=(augmentation_taux-10)
gain_final=(retrait_10_pourcent*baissetaux)/100
print (gain_final)

