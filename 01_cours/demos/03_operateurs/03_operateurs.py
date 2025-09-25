import math as mon_math  # Ajout d'un import du module 'math'

# Les opérateurs arithmétiques
mon_resultat_a = 12 + 8  # Addition
print(mon_resultat_a)

mon_resultat_b = 12 - 8  # Soustraction
print(mon_resultat_b)

mon_resultat_c = 12 / 8  # Division avec virgule
print(mon_resultat_c)

mon_resultat_d = 12 * 8  # Multiplication
print(mon_resultat_d)

mon_resultat_cb = 12 // 8  # Division sans virgule
print(mon_resultat_cb)

mon_resultat_e = 12 % 8  # Reste d'une division / Modulo
print(mon_resultat_e)

mon_resultat_f = 12 ** 8  # Puissance
print(mon_resultat_f)

mon_resultat_g = "Fifi" + " " + "Nono"  # Concaténation
print(mon_resultat_g)

# Utilisation des fonctions du module math
print("L'arrondi au supérieur de 1.9 vaut", mon_math.ceil(1.9))
print("L'arrondi de 1.9 vaut", round(1.9))
print("L'arrondi à l'inférieur de 1.9 vaut", mon_math.floor(1.9))

# Obtenir des constantes mathématiques
print("La valeur de PI est :", mon_math.pi)

# Modification d'une variable en la passant dans une opération arithmétique
ma_variable = 25
ma_variable = ma_variable * 2
ma_variable *= 2

# Les opérateurs logiques
# Il vous permettent de créer des conditions booléennes  que vous pouvez par la suite utiliser
# dans des structures de contrôles il elif else , des structures itératives (boucle for , boucle while)
mon_resultat_l_a = 21 > 5  # Supériorité
print(mon_resultat_l_a)
mon_resultat_l_b = 21 >= 5  # Supériorité ou égalité
print(mon_resultat_l_b)
mon_resultat_l_c = 2 < 50  # Infériorité
print(mon_resultat_l_c)
mon_resultat_l_d = 21 <= 50  # Infériorité ou égalité
print(mon_resultat_l_d)
mon_resultat_l_e = 21 == 5  # Egalité ( Et non =)
print(mon_resultat_l_e)
mon_resultat_l_f = 21 != 5  # Différence
print(mon_resultat_l_f)

# Opérateurs logiques pour tables de vérités 
print((25 > 5) and (125 != 2))  # ET
print((25 > 50) or (125 != 2))  # OU
print((25 < 50) ^ (125 != 2))  # OU EXCLUSIF
print(not True)  # Inversion
