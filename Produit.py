from abc import ABC, abstractmethod
from datetime import date

class Produit(ABC):
    tva = 20        # en pourcentage
    nb_produits = 0

    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock


    @property
    def reference(self):
        return self._reference
    
    @reference.setter
    def reference(self, valeur):
        if len(valeur) < 3 :
            raise ValueError("La référence doit contenir au moins 3 caractères.")
        self._reference = valeur

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        if len(valeur) <= 2:
            raise ValueError("Le nom doit contenir plus de 2 caractères.")
        self._nom = valeur

    @property
    def prix_ht(self):
        return self._prix_ht
    
    @prix_ht.setter
    def prix_ht(self, valeur):
        if valeur < 0 :
            raise ValueError("Le prix ne peut pas être négatif.")
        self._prix_ht = round(valeur, 2)

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valeur):
        if valeur < 0 :
            raise ValueError("Le stock ne peut pas être négatif.")
        self._stock = valeur

    @property
    def prix_ttc(self):
        return self._prix_ht * (1 + Produit._tva / 100)


    def afficher(self):
        print(f"{self.reference}|{self.nom}|{self.prix_ht}|{self.stock}")

    def est_disponible(self):
        if self.stock > 0:
            return True
        else :
            return False
        
    def ajouter_stock(self, quantite):
        if not isinstance(quantite, int):
            raise TypeError("la quantité doit être un entier ")
        if quantite < 0 :
            raise ValueError("Impossible d'ajouter une quantité négative")
        self.stock += quantite
        
    def retirer_stock(self, quantite):
         if quantite < 0: 
            print("Impossible de retirer une quantité négative.")
            return
         if quantite > self.stock:
             print("Stock insuffisant.")
             return
         self.stock -= quantite

    def valeur_stock(self):
        return self.prix_ht * self.stock
        
    @abstractmethod
    def calculer_frais_livraison(self):
        pass 
    @abstractmethod
    def afficher_details(self):
        pass

class ProduitElectronique(Produit):
    def __init__(self, reference, nom, prix_ht, stock, garantie_mois, poids_kg):
             super().__init__(reference, nom, prix_ht, stock)
             self._garantie_mois = garantie_mois
             self._poids_kg = poids_kg
             
    def calculer_frais_livraison(self):
                 return 10 + (self._poids_kg * 2)
        
    def afficher_details(self):
        print(f"[Électronique] {self.reference} - {self.nom}")
        print(f"Prix HT : {self.prix_ht}€ | Stock : {self.stock}")
        print(f"Garantie : {self._garantie_mois} mois")
        print(f"Poids : {self._poids_kg} kg")

class ProduitAlimentaire(Produit):
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
         super().__init__(reference, nom, prix_ht, stock)
         self._date_peremption = date.fromisoformat(date_peremption)
     
    def calculer_frais_livraison(self):
             return 15.0 # réfrigéré
    
    def afficher_details(self):
        print(f"[Alimentaire] {self.reference} - {self.nom}")
        print(f"Prix HT : {self.prix_ht}€ | Stock : {self.stock}")
        print(f"Péremption : {self._date_peremption}")
                 
    def est_perime(self):
        return self._date_peremption < date.today()