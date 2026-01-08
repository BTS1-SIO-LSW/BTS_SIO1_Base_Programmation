# Pour créer une classe, il nous faut utiliser le mot-clé 'class'
# Par convention, les classes commencent par des majuscules
class Dog():

    # Pour créer un objet à partir de notre classe, il faudra passer par
    # son constructeur, qui est défini par la méthode __init__(self):
    # En passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, name, breed, age):

        # On crée la propriété d'instance self.nom_prop et on lui donne une valeur
        # par l'affectation des paramètres du constructeur
        self.name = name
        self.breed = breed
        self.age = age
        self.blabla = True

    # Pour créer des Getter (des nom de proprietés personnalisés qui
    # permettent d'avoir un contrôle sur la syntaxe ou le type de nos propriétés
    def __getattr__(self, item):
        if item == "age_str":
            return f"{self.age} ans"
        elif item == "test":
            return "Toutou"
        elif item == "is_adult":
            if self.age >= 1:
                return True
            else:
                return False
        else:
            raise AttributeError(item)

    # Pour les getters, il existe une syntaxe plus moderne d'en créer
    @property
    def color(self):
        return f"{self.name} is Blue"

    @property
    def double_age(self):
        return self.age * 2

    # Pour créer des Setter (des contrôles potentiels sur nos affectations de variables,
    # on se sert de la surcharge de la méthode dunder __setattr__()
    def __setattr__(self, key, value):
        if key == "human_age":
            self.age = int(value / 7)
        else:
            super().__setattr__(key, value)  # Ne pas oublier ceci sous peine de ne plus pouvoir setter de propriétés
        pass

    # Pour les setters, cette syntaxe est disponible
    # (Attention, il nous faut le getter @property pour pouvoir avoir son setter)
    @double_age.setter
    def double_age(self, value):
        self.age = int(value / 2)

    # Pour faire une méthode, il nous faut faire une fonction dans notre classe
    # qui possède comme premier paramètre le mot-clé self (ce qui l'attachera à notre instance)
    #
    # Via ce mot clé, il nous est également possible d'accéder à toutes les propriétés et méthodes de notre instance
    def aboyer(self, text):
        print(f"{self.name} says : {text}")


# Pour créer une instance de notre classe Dog, il nous faut faire appel au constructeur nom_class(params)
# qui va nous renvoyer une variable du type de la classe
mon_chien = Dog("Bernie", "Labrador", 7)

# Afficher l'objet en faisant appel à la méthode __str__()
print(mon_chien)

# Pour accéder aux propriétés de l'objet,
# on se sert de la notation nom_instance.nom_prop
print(mon_chien.age)

mon_chien.age = 21
print(mon_chien.age)
print(mon_chien.age_str)
print(mon_chien.test)
print(mon_chien.is_adult)

mon_chien.human_age = 21
print(mon_chien.age)

print(mon_chien.color)

# mon_chien.double_age = 18
# print(mon_chien.age)







"""
Fichier : exemples_super_attributeerror_valueerror.py
----------------------------------------------------
But : Illustrer clairement QUAND et COMMENT utiliser :
 - super().__setattr__(...)   → éviter la récursion infinie dans __setattr__ et effectuer la vraie affectation
 - raise AttributeError(name) → signaler qu'un attribut n'existe pas (ou n'est pas exposé)
 - raise ValueError(msg)      → signaler qu'une valeur est du bon type mais invalide (règle métier, borne, format)

Contexte : BTS SIO SLAM — POO Python
"""

# ============================================================================
# 1) super().__setattr__  —  Pourquoi c'est indispensable dans __setattr__
# ============================================================================
# Principe : chaque fois qu'on surcharge __setattr__, un "self.x = v" RE-APPELLE __setattr__
# → danger de récursion infinie si on ne délègue pas l'affectation au parent !
#
# Bonne pratique : utiliser super().__setattr__(key, value) pour faire l'affectation réelle
# (i.e., écrire dans self.__dict__).


class Profil:
    """
    Exemple réaliste :
    - On veut accepter un alias 'human_age' mais stocker l'info sous 'age' (en années).
    - On contrôle globalement toutes les affectations via __setattr__.
    - On DOIT appeler super().__setattr__ pour éviter la récursion infinie et réellement écrire la valeur.
    """
    def __init__(self, username: str, age: int):
        # Ici, __init__ passe aussi par __setattr__. C'est OK, car __setattr__ appelle super().
        self.username = username
        self.age = age

    def __setattr__(self, key, value):
        # Exemple de normalisation : si on reçoit 'human_age', on redirige vers 'age'
        if key == "human_age":
            key, value = "age", int(value)

        # Exemple de validation simple
        if key == "age" and int(value) < 0:
            raise ValueError("age >= 0 requis")

        # INDISPENSABLE : déléguer l'affectation réelle au parent
        super().__setattr__(key, value)


# Démo rapide
p = Profil("alice", 20)
p.human_age = 21   # redirigé vers 'age'
print("[Profil] username=", p.username, "age=", p.age)

# ⚠️ Anti-pattern (à ne PAS faire) : provoquerait une récursion infinie
# class Bad:
#     def __setattr__(self, k, v):
#         self.__setattr__(k, v)  # ❌ s'appelle lui-même pour toujours → RecursionError


# ============================================================================
# 2) AttributeError  —  Quand un attribut n'existe pas (ou n'est pas exposé)
# ============================================================================
# - __getattr__(self, name) n'est appelé QUE si l'attribut 'name' n'a pas été trouvé classiquement.
# - Lever AttributeError(name) indique à Python que l'attribut n'existe pas.
#   Cela garde un comportement standard avec hasattr(), getattr(..., default), etc.


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x, self.y = float(x), float(y)

    def __getattr__(self, name):
        # Attributs calculés "virtuels"
        if name == "magnitude":
            return (self.x**2 + self.y**2) ** 0.5
        if name == "is_null":
            return (self.x == 0.0 and self.y == 0.0)

        # Très important : si on ne connaît pas l'attribut, on signale explicitement son absence
        raise AttributeError(name)


v = Vector2D(3, 4)
print("[Vector2D] magnitude=", v.magnitude)  # 5.0
print("[Vector2D] is_null =", v.is_null)     # False
try:
    print(v.angle)  # ❌ n'existe pas
except AttributeError as e:
    print("[Vector2D] AttributeError détectée :", e)


# ============================================================================
# 3) ValueError  —  Valeur de bon type mais invalide (contrainte métier)
# ============================================================================
# - On lève ValueError quand la "forme" est correcte (types OK) mais que le "fond" ne respecte pas les règles.


class Rectangle:
    def __init__(self, width: float, height: float):
        # Types OK (float acceptés), mais on impose des bornes
        if width <= 0:
            raise ValueError("Largeur > 0 requise")
        if height <= 0:
            raise ValueError("Hauteur > 0 requise")
        self._w = float(width)
        self._h = float(height)

    @property
    def width(self) -> float:
        return self._w

    @width.setter
    def width(self, val: float):
        if val <= 0:
            raise ValueError("Largeur > 0 requise")
        self._w = float(val)

    @property
    def height(self) -> float:
        return self._h

    @height.setter
    def height(self, val: float):
        if val <= 0:
            raise ValueError("Hauteur > 0 requise")
        self._h = float(val)

    @property
    def area(self) -> float:
        return self._w * self._h


r = Rectangle(10, 5)
print("[Rectangle] area=", r.area)
try:
    r.width = -3  # ❌ valeur invalide → ValueError
except ValueError as e:
    print("[Rectangle] ValueError détectée :", e)


# ============================================================================
# 4) Exemple combiné (AttributeError + ValueError + super().__setattr__)
# ============================================================================
# Cas d'un modèle simple d'inventaire :
# - __setattr__ contrôle les affectations et délègue avec super()
# - Valeurs invalides → ValueError
# - Attributs calculés via __getattr__ (sinon AttributeError)


class ArticleStock:
    def __init__(self, sku: str, quantity: int, price: float):
        self.sku = sku
        self.quantity = quantity
        self.price = price

    def __setattr__(self, key, value):
        # Règles métiers simples
        if key == "sku" and (not value or not str(value).strip()):
            raise ValueError("SKU non vide requis")
        if key == "quantity" and int(value) < 0:
            raise ValueError("Quantité >= 0 requise")
        if key == "price" and float(value) < 0:
            raise ValueError("Prix >= 0 requis")

        # Toujours déléguer l'écriture effective à l'implémentation de base
        super().__setattr__(key, value)

    def __getattr__(self, name):
        # Attributs virtuels
        if name == "is_in_stock":
            return self.quantity > 0
        if name == "total_value":
            return round(self.quantity * self.price, 2)
        # Sinon : comportement standard → cet attribut n'existe pas
        raise AttributeError(name)


a = ArticleStock("ABC-001", 10, 3.5)
print("[ArticleStock] in_stock=", a.is_in_stock, " total_value=", a.total_value)

try:
    a.quantity = -1  # ❌ ValueError (contrainte métier)
except ValueError as e:
    print("[ArticleStock] ValueError détectée :", e)

try:
    print(a.unknown_attr)  # ❌ AttributeError
except AttributeError as e:
    print("[ArticleStock] AttributeError détectée :", e)

