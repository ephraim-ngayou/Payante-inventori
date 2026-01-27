class Categorie:

    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits = self.produits + produit

    def retirer_produit(self, reference):
        self.produits = self.produits - reference

    def lister_produits(self):
        print({self.nom})

    def nb_produits(self):
        return len(self.produits)
    
    def valeur_totale(self):
        total = 0
        return total
    
c1 = Categorie("Périphériques","Ici ma description de périphériques")
print(c1.nom)
print(c1.produits)