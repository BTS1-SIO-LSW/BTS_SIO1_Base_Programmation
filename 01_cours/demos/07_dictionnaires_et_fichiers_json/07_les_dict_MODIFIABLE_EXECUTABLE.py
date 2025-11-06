# ============================================================
# CHAPITRE : DICTIONNAIRES (dict) — propriétés & manipulations
# ============================================================
# Propriétés clés des dictionnaires en Python :
# 1) MUTABLE   : on peut modifier le contenu après création (ajout, modif., suppression).
# 2) ORDONNÉ   : depuis Python 3.7+, l'ordre d'insertion des clés est préservé.
# 3) ITÉRABLE  : on peut les parcourir en boucle for (par défaut sur les clés).
#
# Ce script est exécutable : lancez-le pour voir les démonstrations imprimées.
# ------------------------------------------------------------

print("=== 0) Création et règles de base ===")
# Création d'un dictionnaire vide
mon_dict = {}
print("Dico vide :", mon_dict)

# Démonstration : pas de doublons de clé possibles → la dernière valeur écrase la précédente
# Remarque : dans la déclaration ci-dessous, la clé 'test' est déclarée deux fois.
mon_dict_a = {'test': 'Texte de test', 1: 25, 'test': True}
print("Dico avec doublon de clé 'test' :", mon_dict_a)
# → Seule la dernière affectation pour la clé 'test' subsiste (True).

# Accéder à une valeur par sa clé
print("Valeur pour la clé 1   :", mon_dict_a[1])
print("Valeur pour la clé 'test' :", mon_dict_a['test'])

print("\n=== 1) MUTABILITÉ : ajout / modification / suppression ===")
# Ajout : créer une nouvelle clé et lui affecter une valeur
mon_dict_a['blabla'] = 'Texte lié à blabla'
print("Après ajout de 'blabla' :", mon_dict_a)

# Modification : réaffecter une valeur à une clé existante
mon_dict_a['blabla'] = 247
print("Après modification de 'blabla' :", mon_dict_a)

# Suppression avec del (⚠️ lève une exception si la clé n'existe pas)
del mon_dict_a['test']
print("Après suppression de 'test' (avec del) :", mon_dict_a)

# Suppression avec pop (retourne la valeur supprimée ; peut fournir une valeur par défaut)
valeur_supprimee = mon_dict_a.pop(1)            # supprime la clé 1
print("Valeur supprimée avec pop(1) :", valeur_supprimee)
print("État après pop(1) :", mon_dict_a)
valeur_defaut = mon_dict_a.pop('inconnue', None)  # ne lève pas d'erreur si la clé n'existe pas
print("pop('inconnue', None) →", valeur_defaut)

# Fusion de dictionnaires : update
mon_dict_a.update({2: "Valeur de clé 2"})
print("Après update({2: 'Valeur de clé 2'}) :", mon_dict_a)

print("\n=== 2) ORDRE : l'ordre d'insertion est conservé (Python 3.7+) ===")
# On montre que l'itération suit l'ordre d'insertion
mon_dict_ordonne = {}
mon_dict_ordonne['a'] = 1
mon_dict_ordonne['b'] = 2
mon_dict_ordonne['c'] = 3
print("Dico ordonné initial :", mon_dict_ordonne)

print("Itération (clés → valeurs) selon l'ordre d'insertion :")
for k, v in mon_dict_ordonne.items():
    print(f"  {k} → {v}")

# On insère une nouvelle clé ; elle apparaîtra en fin d'itération
mon_dict_ordonne['z'] = 26
print("Après insertion de 'z' :", mon_dict_ordonne)

print("Nouvelle itération (ordre conservé, 'z' en dernier) :")
for k, v in mon_dict_ordonne.items():
    print(f"  {k} → {v}")

print("\n=== 3) ITÉRABILITÉ : parcourir clés, valeurs, paires ===")
mon_dict_iter = {'x': 10, 'y': 20, 'z': 30}

# a) Par défaut, la boucle for parcourt les clés
print("Contenu de mon_dict_iter.keys() : ", mon_dict_iter.keys())
print("Itération sur les clés :")
for cle in mon_dict_iter:
    print("  clé :", cle)

# b) Iteration sur les valeurs
print("Contenu de mon_dict_iter.values() : ", mon_dict_iter.values())
print("Itération sur les valeurs :")
for valeur in mon_dict_iter.values():
    print("  valeur :", valeur)

# c) Itération sur les paires (clé, valeur)
print("Contenu de mon_dict_iter.items() : ", mon_dict_iter.items())
print("Itération sur les items (clé, valeur) :")
for cle, valeur in mon_dict_iter.items():
    print(f"  {cle} = {valeur}")

print("\n=== 4) APIs utiles : .keys(), .values(), .items() ===")
print("mon_dict_iter.keys()   →", list(mon_dict_iter.keys()))
print("mon_dict_iter.values() →", list(mon_dict_iter.values()))
print("mon_dict_iter.items()  →", list(mon_dict_iter.items()))

print("\n=== 5) RÉCAPITULATIF ===")
print("- Mutable  : oui → on peut ajouter/modifier/supprimer des entrées.")
print("- Ordonné  : oui (depuis Python 3.7+) → l'ordre d'insertion est conservé.")
print("- Itérable : oui → on peut parcourir clés/valeurs/paires.")





print("\n=== 6) FOCUS : dict.pop(clé, valeur_par_défaut) et le rôle de None ===")
# Objectif : montrer la différence entre pop('clé') (qui peut lever un KeyError)
# et pop('clé', None) (qui renvoie None si la clé n'existe pas, sans lever d'erreur).

demo_pop = {'a': 1, 'b': 2}
print("Dictionnaire de démo :", demo_pop)

# 6.1) Cas avec clé existante : pop('a')
val_a = demo_pop.pop('a')
print("pop('a') renvoie :", val_a)         # → 1
print("État après pop('a') :", demo_pop)   # → {'b': 2}

# 6.2) Cas avec clé absente : pop('z') → lève KeyError si aucune valeur par défaut n'est fournie
try:
    demo_pop.pop('z')                      # pas d'argument par défaut → KeyError
except KeyError as e:
    print("pop('z') sans valeur par défaut → KeyError capturée :", e)

# 6.3) Cas avec clé absente ET valeur par défaut None : pas d'erreur, retourne None
retour_none = demo_pop.pop('z', None)
print("pop('z', None) renvoie :", retour_none)  # → None
print("État final du dico de démo :", demo_pop)

# Remarque : 'None' signifie « absence de valeur ». On l'utilise souvent comme sentinelle pour indiquer
# qu'aucune valeur n'a été trouvée / fournie, sans interrompre l'exécution par une exception.
