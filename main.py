from Produit import Produit
from Categorie import Categorie
from Produit import ProduitElectronique
from Produit import ProduitAlimentaire

p1 = ProduitElectronique("KB-001", "Clavier mécanique RGB", 10, 3, 24, 0.5)
p2 = ProduitElectronique("KB-001", "Souris", 12, 4, 28, 0.5)
p3 = ProduitElectronique("KB-001", "Clavier mécanique RGB", 18, 93, 4, 0.5)


c1 = Categorie("Périphériques","Ici ma description de périphériques")
c1.ajouter_produit(p1)
c1.ajouter_produit(p2)
c1.ajouter_produit(p3)

clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print(clavier.calculer_frais_livraison())  # 11.0
print(fromage.calculer_frais_livraison())  # 15.0

clavier.afficher_details()
fromage.afficher_details()
p1.afficher_details()
p2.afficher_details()
p3.afficher_details()


print(fromage.est_perime())


print(Produit.prix_ttc)