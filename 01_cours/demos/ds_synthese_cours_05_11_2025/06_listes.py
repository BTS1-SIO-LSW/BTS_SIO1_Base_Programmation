# On crée une liste avec la syntaxe des crochets
ma_variable = [1, 2, 3, 'Blabla', True, ['a', True, 25]]

# On peut afficher l'ensemble de la liste en affichant la variable liste
print(ma_variable)

# On peut afficher un élément en particulier
# de la liste en accédant via son index (commence à 0)
print(ma_variable[0])

# Si une liste contient un autre conteneur indexé,
# on peut spécifier l'index de l'index pour accéder au sous-ensemble
print(ma_variable[5][2])

mes_nombres = [1, 4, 5, 2, 3]
print(mes_nombres)

# On peut trier une liste avec la méthode .sort()
mes_nombres.sort(reverse=True)
print(mes_nombres)

# On peut choisir d'afficher une version triée
# (triée uniquement pour l'affichage)
print(sorted(mes_nombres))
print(mes_nombres)

# Pour ajouter à la liste, on utilise .append()
mes_nombres.append(9)
print(mes_nombres)

# Pour ajouter à un index en particulier, on utilise .insert()
mes_nombres.insert(2, 6)
print(mes_nombres)

# Pour ajouter le contenu d'une liste à une autre liste
mes_nombres.extend([8, 7])
print(mes_nombres)

# Pour retirer de la liste à partir de l'index
mes_nombres.pop(2)
print(mes_nombres)

# Pour retirer de la liste à partir du contenu
mes_nombres.remove(4)
print(mes_nombres)

# Pour itérer puis afficher le contenu, on peut passer par une boucle for
for i in mes_nombres:
    print(i)

# List comprehension
liste_a = [x for x in range(1, 11)]  # On obtient une liste de nombres allant de 1 à 10 compris

print(liste_a)

# Il est possible d'altérer l'entrée de l'itérateur
# en modifiant l'expression à gauche de la list comprehension
liste_b = [x ** 2 for x in range(1, 11)]
print(liste_b)

# Grâce à cette syntaxe, on peut avoir l'équivalent d'un map()
liste_c = [x ** 2 for x in liste_a]
print(liste_c)

# Il est également possible de filter les valeurs, équivalent à un filter()
liste_d = [x for x in range(1, 11) if x % 2 == 0]
print(liste_d)

# Il est également possible de conditionner l'affectation de variable
liste_e = ['EVEN' if x % 2 == 0 else 'ODD' for x in liste_a]
print(liste_e)

ma_liste_g = [['a', 25, 1], 'b', 'c', ['a', 14, 5]]
for element in ma_liste_g:
    print(ma_liste_g.index(element), element)

    
