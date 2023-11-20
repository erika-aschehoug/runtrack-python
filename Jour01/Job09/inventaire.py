#inventaire
produit1="pate"
pu=2
q=10

#écriture formatée
print("produit:{}, prix unitaire:{}, quantité:{}".format(produit1, pu, q))

#maj stock
qajoutee=int(input("quantité a ajouter au stock"))
q+=qajoutee
print(q)

#inflation 10%
pi=float(pu*1.1)
print("nouveau prix",pi) 
