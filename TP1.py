class Produit:
    nb_produits = 0
    tva = 0.2
    def __init__(self, reference, nom, prix, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix
        self.stock = stock

    def afficher(self):
        print(f"produit {self.reference}|{self.nom}|{self.prix_ht}€ HT ({self.prix_ht * (1 + Produit.tva / 100)}€) |stock:{self.stock}")
    
    def prix_ttc(self):
        return self.prix_ht * (1 + Produit.tva / 100)
    
    def est_disponible(self):
         if self.stock > 0:
            return True
         else:
            return False
         
    def ajouter_stock(self, quantite):
        self.stock = self.stock + quantite

    def retirer_stock(self, quantite):
        self.stock = self.stock - quantite

    def valeur_stock(self):
        return self.prix_ht * self.stock

p1 = Produit("KB-001","clavier mécanique RGB",79.99, 15 )
p2 = Produit("MS-002","Souris gaming 16000 DPI",49.99, 25 )

p1.afficher()
p2.afficher()

p1.prix_ttc()
p2.prix_ttc()

p1.est_disponible()
p2.est_disponible()
