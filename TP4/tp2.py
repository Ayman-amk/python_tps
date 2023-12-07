class Batiment:
    def __init__(self, adresse=""):
        self.__adresse = adresse

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def __str__(self):
        return f"Batiment à l'adresse : {self.__adresse}"


class Maison(Batiment):
    def __init__(self, adresse="", nb_pieces=0):
        super().__init__(adresse)
        self.__nb_pieces = nb_pieces

    def get_nb_pieces(self):
        return self.__nb_pieces

    def set_nb_pieces(self, nb_pieces):
        self.__nb_pieces = nb_pieces

    def __str__(self):
        return f"Maison à l'adresse : {super().get_adresse()}, Nombre de pieces : {self.__nb_pieces}"


class Immeuble(Batiment):
    def __init__(self, adresse="", nb_appart=0):
        super().__init__(adresse)
        self.__nb_appart = nb_appart

    def get_nb_appart(self):
        return self.__nb_appart

    def set_nb_appart(self, nb_appart):
        self.__nb_appart = nb_appart

    def __str__(self):
        return f"Immeuble à l'adresse : {super().get_adresse()}, Nombre d'appartements : {self.__nb_appart}"


batiment1 = Batiment("123 Rue de la Errzchidia")
print(batiment1)

maison1 = Maison("456 Rue du Riad", 3)
print(maison1)

immeuble1 = Immeuble("789 Avenue de la Errachidia", 10)
print(immeuble1)
