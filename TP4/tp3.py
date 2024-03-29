from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    @abstractmethod
    def gains(self):
        pass

    def __str__(self):
        return f"{self.__prenom} {self.__nom}"

class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.__salaire = salaire

    def get_salaire(self):
        return self.__salaire

    def set_salaire(self, salaire):
        self.__salaire = salaire

    def gains(self):
        return self.__salaire

    def __str__(self):
        return f"Patron: {super().__str__()}, Salaire: {self.__salaire}"

class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.__salaire = salaire
        self.__commission = commission
        self.__quantite = quantite

    def get_salaire(self):
        return self.__salaire

    def set_salaire(self, salaire):
        self.__salaire = salaire

    def get_commission(self):
        return self.__commission

    def set_commission(self, commission):
        self.__commission = commission

    def get_quantite(self):
        return self.__quantite

    def set_quantite(self, quantite):
        self.__quantite = quantite

    def gains(self):
        return self.__salaire + (self.__commission * self.__quantite)

    def __str__(self):
        return f"TravailleurCommission: {super().__str__()}, Salaire de base: {self.__salaire}, Commission: {self.__commission}, Quantité: {self.__quantite}"

class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.__retribution = retribution
        self.__heures = heures

    def get_retribution(self):
        return self.__retribution

    def set_retribution(self, retribution):
        self.__retribution = retribution

    def get_heures(self):
        return self.__heures

    def set_heures(self, heures):
        self.__heures = heures

    def gains(self):
        return self.__retribution * self.__heures

    def __str__(self):
        return f"TravailleurHoraire: {super().__str__()}, Rémuneration horaire: {self.__retribution}, Heures travaillées: {self.__heures}"

patron = Patron("Ayman", "Amokrane", 5000)
travailleur_commission = TravailleurCommission("Elon", "Musk", 2000, 10, 100)
travailleur_horaire = TravailleurHoraire("Jeff", "Pezos", 20, 120)

employes = [patron, travailleur_commission, travailleur_horaire]

for employe in employes:
    print(f"{employe} - Salaire: {employe.gains()}")
