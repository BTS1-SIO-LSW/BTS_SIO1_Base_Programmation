#  Les bases
print("Hello World")
print('Hello World')

# Affectation de variables
mon_texte = "Bla bla"            # Ceci est un texte String entouré de guillemets
mon_texte2 = 'Bla bla2'          # Ceci est un texte String entouré d'apostrophes

# Pour mettre en commentaire une ligne d'instructions , utiliser #
# mon_texte = "Blabla"

# Pour mettre en commentaire un bloc d'instructions , mettez le bloc d'instructions en surbrillance , puis faites CTRL + /
# mon_texte = "Bla bla"
# mon_texte2 = "Bla bla"

# Quand la variable est de type str (chaîne de caractères) , on peut mettre sa valeur sur plusieurs lignes  ,
# en triplant les guillemets ou les apostrophes :
mon_texte3 = """Bonjour        
Je m'appelle
David"""
mon_texte4 = '''Bonjour
Je m'appelle
DONISA'''
mon_nombre = 25                 # Ceci est un nombre de type int ( pour Integer , en Anglais)
mon_nombre_virgule = 3.14       # Ceci est un nombre à virgule ou encore "Flottant" Float

ma_variable = None              # Valeur None équivaut à une variable 'vide'

# Affichage de variables
print("La variable mon_texte vaut :", mon_texte)
print("La variable mon_texte2 vaut :", mon_texte2)
print("La variable mon_texte3 vaut :", mon_texte3)
print(mon_nombre)
print(mon_nombre_virgule)
print(mon_texte, mon_nombre, mon_nombre_virgule)

# Récupération entrées utilisateur
input_user = input("Veuilliez entrer un nombre : ")
print(input_user)
print(type(input_user))

# Casting des variables en un autre type
input_en_nombre = int(input_user)
print(input_en_nombre)
print(type(input_en_nombre))

# Casting à la volée de notre récupération utilisateur
input_user_2 = int(input("Veuilliez entrer un vrai nombre : "))
print(input_user_2)
print(type(input_user_2))
