# Concaténation de chaines de caractères
un_nombre = 25
un_texte = "Teste de texte"
un_resultat = un_texte + str(un_nombre)

# Ajout de variables dans les chaines de caractère
mon_genre = 'Garçon'
mon_age = 14

# Chaines formatées classiques
ma_chaine_formatee = "Je suis un {0} et j'ai {1} ans !".format(mon_genre, mon_age)
ma_chaine_formatee2 = f"Je suis un {mon_genre} et j'ai {mon_age} ans !"




"""
  Mini-langue de formatage & Arrondis en Python (exemples compacts et commentés)

Rappels de syntaxe de formatage (utilisable dans f-strings et str.format) :

{valeur: [remplissage][alignement][signe][#][0][largeur][,][.precision][type]}

- alignement : < (gauche), > (droite), ^ (centré)
- remplissage : un seul caractère avant l’alignement (ex: '*' ou '0')
- largeur : nombre mini de caractères réservés (ex: 10)
- .precision : dépend du type (nb décimales pour f/e/g, nb max de caractères pour s)
- type (principaux) : f (flottant), e (scientifique), g (compact), d (entier), s (string), b/x/X (bases), %
"""





# Formatage et modification du nombre de caractère après la virgule (arrondi automatique)
ma_chaine_formatee3 = "Ma moyenne est est de {0:.2f} / 20".format(14.4999)
ma_chaine_formatee4 = f"Ma moyenne est est de {14.5:.2f} / 20"

# Formatage et modification du nombre de caractère que doit prendre horizontalement la variable
ma_chaine_formatee5 = f"{25:6} | {4.99:15.1f}"
ma_chaine_formatee6 = f"{512:6} | {15.37:15.1f}"
ma_chaine_formatee7 = f"{1024:6} | {2.8754:15.1f}"

# Rogner un mot
mon_mot = 'Pierre'
print(f"{mon_mot:.3s}")
print(f"{mon_mot[2:4]}")

print(ma_chaine_formatee)
print(ma_chaine_formatee2)
print(ma_chaine_formatee3)
print(ma_chaine_formatee4)

# Formatage du string et modification de son alignement horizontal avec ajout d'un nombre choisi
# de caractère en fin, sur les côtés ou au début de la chaine de caractère
print(f"{'Somme':6} | {'Valeur en %':<15}")
print(f"{'Somme':6} | {'Valeur en %':^15}")
print(f"{'Somme':6} | {'Valeur en %':>15}")

print(ma_chaine_formatee5)
print(ma_chaine_formatee6)
print(ma_chaine_formatee7)



# =========
# FLOTTANTS
# =========
pi = 3.14159265

# .3f → 3 décimales, type = flottant "fixe"
print(f"pi en 3 décimales (.3f)      : {pi:.3f}")      # 3.142 (arrondi visuel à 3 décimales)
print(f"pi en 0 décimale  (.0f)      : {pi:.0f}")      # 3

# Largeur + décimales : 10.2f = champ min 10, 2 décimales (aligné à droite par défaut)
print(f"pi largeur10, 2 décimales    : |{pi:10.2f}|")  # |      3.14|

# Alignement + remplissage personnalisé pour flottants
print(f"aligné gauche  (<)           : |{pi:<10.2f}|") # |3.14      |
print(f"centré (^) remplissage '*'   : |{pi:*^10.2f}|")# |***3.14***|
print(f"aligné droite (>) zéros '0'  : |{pi:010.2f}|") # |0000003.14|

# Forme scientifique (e) et compacte (g)
grand = 1234567.0
print(f"scientifique (e)             : {grand:.3e}")   # 1.235e+06
print(f"compact (g)                   : {grand:.6g}")   # 1.23457e+06 ou 1234560 selon magnitude

# Séparateur de milliers pour flottants et entiers avec ","
print(f"milliers (,) sur flottant    : {grand:,.2f}")  # 1,234,567.00
print(f"milliers (,) sur entier      : {1234567:,d}")  # 1,234,567


# =========
# CHAÎNES
# =========
mot = "Python"

# .3s → coupe la chaîne à 3 caractères max
print(f"tronquer chaîne (.3s)        : {mot:.3s}")     # "Pyt"

# Largeur + alignements sur chaînes
print(f"gauche  (<) largeur 8        : |{mot:<8s}|")   # |Python  |
print(f"centre  (^) largeur 8        : |{mot:^8s}|")   # | Python |
print(f"droite  (>) largeur 8        : |{mot:>8s}|")   # |  Python|

# Remplissage custom (caractère avant le spécificateur d’alignement)
print(f"remplissage '.' centré       : |{mot:.^10s}|") # |..Python.|

# Largeur = minimum : si le contenu dépasse, Python n’écrase pas → le champ s’élargit
print(f"largeur 4 mais mot plus long : |{'SuperLongMot':4s}|")  # pas tronqué, champ élargi

# =========
# ENTIERS
# =========
n = 42

# 03d → 3 chiffres minimum, complété de zéros à gauche
print(f"entier zéros à gauche (03d)  : {n:03d}")       # 042

# Largeur, alignements et remplissage custom
print(f"entier largeur 6, droite     : |{n:>6d}|")     # |    42|
print(f"entier largeur 6, centré '*' : |{n:*^6d}|")    # |**42**|

# Bases : b (binaire), x/X (hex), o (octal)
print(f"binaire (b)                  : {n:b}")         # 101010
print(f"hex minuscule (x)            : {n:x}")         # 2a
print(f"hex majuscule (X)            : {n:X}")         # 2A
print(f"octal (o)                    : {n:o}")         # 52

# Pourcentage (%) : multiplie par 100 et ajoute '%'
taux = 0.0765
print(f"taux en pourcentage (% .2f)  : {taux:.2%}")    # 7.65%

# ==========================
# ARRONDIS : ceil / floor / round
# ==========================
print("\n=== Arrondis ===")
# ceil : plafond → ENTIER supérieur ou égal (monte toujours, vers +∞)
print(f"ceil(1.1)  = {math.ceil(1.1)}")    # 2
print(f"ceil(-1.1) = {math.ceil(-1.1)}")   # -1 (se rapproche de 0)

# floor : plancher → ENTIER inférieur ou égal (descend toujours, vers -∞)
print(f"floor(1.9)  = {math.floor(1.9)}")  # 1
print(f"floor(-1.1) = {math.floor(-1.1)}") # -2 (s’éloigne de 0)

# round : arrondi "classique" avec règle "ties-to-even" (arrondi du banquier)
# - Si la valeur est pile à .5, on arrondit vers l'entier pair le plus proche.
print("\nround avec ties-to-even (banquier) :")
vals = [1.4, 1.5, 2.5, 3.5, 4.5, 5.5, -1.5, -2.5]
for v in vals:
    print(f"round({v:4}) = {round(v)}")

"""
Résultats clefs à remarquer :
- round(1.5)  -> 2  (pair)
- round(2.5)  -> 2  (pair, pas 3)
- round(3.5)  -> 4  (pair)
- round(4.5)  -> 4  (pair, pas 5)
- round(5.5)  -> 6  (pair)
- round(-1.5) -> -2 (pair le plus proche)
- round(-2.5) -> -2 (pair le plus proche)

Pourquoi ce choix ? Pour éviter un biais statistique quand on arrondit en masse des valeurs .5
(autrement, un arrondi systématiquement vers le haut gonflerait les moyennes).
"""
