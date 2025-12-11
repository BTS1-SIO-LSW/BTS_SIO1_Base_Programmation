ma_liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
print(ma_liste)

# On peut transformer une liste en set pour en retirer tous les doublons
mon_set = set(ma_liste)
print(mon_set)

# On peut également créer un set vierge en se servant de son constructeur
mon_set_2 = set()
print(mon_set_2)

# On peut créer un set remplit via cette syntaxe
mon_set_3 = {1, 4, 6}
print(mon_set_3)

# Pour ajouter un élément à un set, on se sert de la méthode .add()
mon_set_2.add(3)
mon_set_2.add('a')
mon_set_2.add('a')
print(mon_set_2)

# Pour fusionner deux sets ensemble, il existe la fonction  .update()
mon_set.update(mon_set_2)
print(mon_set)

# Pour retirer un élément d'un set
# mon_set_2.remove(25) # Cause une erreur si l'élément n'est pas présent
mon_set_2.discard(25)  # Ne cause pas d'erreur en cas d'absence de l'élément


mon_set_a = {1, 2, 3, 4, 5, 6}
mon_set_b = {5, 6, 7, 8, 9, 10}


# Tester s'il y a présence ou absence d'éléments en commun entre les deux sets
print(mon_set_a.isdisjoint(mon_set_b))
print({25, 50, 99}.isdisjoint(mon_set_b))

# Pour tester si un set fait partie ou non d'un autre set
print({1, 2, 3}.issubset({1, 2, 3, 4, 5, 6}))

# Pour tester si un set comprend un autre set
print({1, 2, 3, 4, 5, 6}.issuperset({1, 2, 3}))

# Diagramme de Venn
print(mon_set_a.union(mon_set_b))  # UNION
print(mon_set_a.intersection(mon_set_b))  # INTERSECTION
print(mon_set_a.difference(mon_set_b))  # DIFFERENCE
print(mon_set_b.difference(mon_set_a))
print(mon_set_a.symmetric_difference(mon_set_b))  # DIFFERENCE SYMETRIQUE
