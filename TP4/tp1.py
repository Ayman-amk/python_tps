class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"


class Rectangle(Point):
    def __init__(self, x=0, y=0, longueur=0, largeur=0):
        super().__init__(x, y)
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        return self.__longueur * self.__largeur

    def __str__(self):
        return f"Rectangle({super().get_x()}, {super().get_y()}, {self.__longueur}, {self.__largeur})"


class Parallelepipede(Rectangle):
    def __init__(self, x=0, y=0, longueur=0, largeur=0, hauteur=0):
        super().__init__(x, y, longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def aire(self):
        return 2 * (self.__longueur * self.__largeur + self.__longueur * self.__hauteur + self.__largeur * self.__hauteur)

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur

    def __str__(self):
        return f"Parallelepipede({super().get_x()}, {super().get_y()}, {self.__longueur}, {self.__largeur}, {self.__hauteur})"


point1 = Point(1, 2)
print(point1)

rectangle1 = Rectangle(1, 2, 3, 4)
print(rectangle1)
print("Aire du rectangle :", rectangle1.aire())

parallelepiped1 = Parallelepipede(1, 2, 3, 4, 5)
print(parallelepiped1)
print("Aire du parallelepiped :", parallelepiped1.aire())
print("Volume du parallelepiped :", parallelepiped1.volume())
