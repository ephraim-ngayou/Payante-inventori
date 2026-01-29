class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self._description = description
        self._produits = []

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le nom doit être une chaîne.")
        if len(valeur) < 2:
            raise ValueError("Le nom doit contenir au moins 2 caractères.")
        self._nom = valeur

    def ajouter_produit(self, produit):
        self._produits.append(produit)

    def retirer_produit(self, reference):
        self._produits = [p for p in self._produits if p.reference != reference]

    @property
    def nb_produits(self):
        return len(self._produits)

    @property
    def valeur_totale(self):
        return sum(p.valeur_stock for p in self._produits)

    @property
    def produits_disponibles(self):
        return [p for p in self._produits if p.stock > 0]

    def lister_produits(self):
        for p in self._produits:
            p.afficher()
