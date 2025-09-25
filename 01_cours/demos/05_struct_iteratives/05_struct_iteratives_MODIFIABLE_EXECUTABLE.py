# ----------------------------------------------------------------
# 1) Pourquoi utiliser une structure itérative ?
# ----------------------------------------------------------------
# ➤ Quand on veut RÉPÉTER plusieurs fois une action :
#    - compter, afficher, calculer, valider N fois, etc.
# ➤ Deux grandes familles :
#    - for    : nombre d’itérations connu/contrôlé via range()
#    - while  : répéter "tant que" la condition est vraie (arrêt conditionnel)
#
# ⚠ Dans ce cours on ne manipule PAS de types "complexes" (pas de liste, dict…),
#    on se limite aux variables simples, conditions, chaînes et range().

# ----------------------------------------------------------------
# 2) La boucle for avec range()
# ----------------------------------------------------------------
# range(début, fin, pas) génère une suite d'entiers commençant à 'début',
# s'arrêtant AVANT 'fin', et augmentant de 'pas' à chaque itération.
# On l’emploie quand on sait combien de tours on veut faire.

# Exemple : afficher 0, 2, 4, 6, 8, 10
for nom_variable in range(0, 11, 2):  # début=0, fin exclusive=11, pas=2
    print("La variable vaut", nom_variable)

# ----------------------------------------------------------------
# 2.1) range() en version abrégée
# ----------------------------------------------------------------
# range(n) équivaut à range(0, n, 1) : de 0 à n-1, pas de 1.
# Exemple : afficher 5 fois "OK" (pour i = 0,1,2,3,4)
for i in range(5):
    print("OK (itération n°", i, ")")

# ----------------------------------------------------------------
# 2.2) Boucles for imbriquées (nested loops)
# ----------------------------------------------------------------
# Une boucle à l’intérieur d’une autre. Utile pour répéter un motif de répétitions.
# Exemple : afficher un petit "tableau" de 3 lignes × 4 colonnes d’étoiles, SANS liste.
for ligne in range(1, 4):      # 1, 2, 3
    texte = ""                 # on construit une chaîne (pas de liste)
    for colonne in range(1, 5):# 1, 2, 3, 4
        texte = texte + "*"    # concaténation simple
    print("Ligne", ligne, ":", texte)

# ----------------------------------------------------------------
# 3) Mots-clés de contrôle : pass, break, continue
# ----------------------------------------------------------------
# - pass     : instruction "ne rien faire". Sert de placeholder (bouchon) ; le code est valide.
# - continue : saute DIRECTEMENT à l’itération SUIVANTE (ignore le reste du bloc courant).
# - break    : STOPPE immédiatement la boucle courante (sortie de la boucle).
#
# ➤ Différence clé pass vs continue :
#   * pass ne change pas le flux : la suite du bloc s’exécute normalement (mais ici, pass lui-même
#     ne fait rien).
#   * continue interrompt le reste du bloc et relance une prochaine itération.

# Démo simple (for) :
for n in range(1, 7):
    if n == 2:
        pass  # on ne fait rien de particulier ici, mais on peut laisser du code "à venir"
    if n == 3:
        continue  # on saute l'affichage pour n == 3
    if n == 5:
        break  # on arrête complètement la boucle quand n == 5
    print("n vaut", n)
# Sortie prévue : n=1, n=2, (3 est sauté), n=4 puis break à 5 => on n'affiche pas 5 ni 6.

# ----------------------------------------------------------------
# 4) La boucle while
# ----------------------------------------------------------------
# Syntaxe : while <condition>:
#           (bloc d'instructions)
#
# La boucle s'exécute TANT QUE la condition est vraie. On l’emploie quand :
# - On NE connaît PAS à l’avance le nombre d’itérations
# - On veut s’arrêter dès qu’une condition (calculée/mesurée) devient fausse
#
# ⚠ Risque de BOUCLE INFINIE si la condition ne devient jamais fausse.
#   Toujours prévoir : une variable d’itération qui évolue OU une condition qui peut changer.

mon_compteur = 0

# Phase comparaison et entrée dans la boucle
while mon_compteur < 10:
    # Phase de modification de la variable d'itération (pour éviter l'infini)
    mon_compteur += 1

    # Phase d'instructions (exemples de continue/break)
    if mon_compteur == 3:
        continue  # on saute l'affichage quand mon_compteur == 3 (puis passe à l’itération suivante)

    if (mon_compteur % 5) == 0:
        break  # on stoppe la boucle dès qu'on atteint un multiple de 5 (ici 5)

    if (mon_compteur % 2) == 0:
        print("Bonjour (compteur pair)", mon_compteur)

    pass  # rien à faire de plus ici ; placeholder propre

print("Valeur finale du compteur :", mon_compteur)

# ----------------------------------------------------------------
# 4.1) Éviter explicitement la boucle infinie (exemple type)
# ----------------------------------------------------------------
# Mauvais exemple (à NE PAS faire) :
# x = 0
# while x < 3:
#     print("Je boucle…")   # ⚠ x n'est jamais modifié => boucle infinie !
#
# Bon réflexe :
# - Modifier la variable liée à la condition à CHAQUE tour (ou à une fréquence maîtrisée)
# - OU inclure un break conditionnel clair.

# Exemple correct :
x = 0
while x < 3:
    print("Tour de while n°", x)
    x = x + 1  # la condition finira par devenir fausse (x=3), donc la boucle s’arrête.

# ----------------------------------------------------------------
# 5) Choisir entre for et while : repères simples
# ----------------------------------------------------------------
# - Utiliserr for + range() quand vous savez COMBIEN de fois vous voulez boucler
#   (par ex. "10 fois", "de 0 à 100 par pas de 10", etc.).
# - Utilise while si la répétition dépend d’un ÉTAT qui évolue (lecture d’entrée,
#   compteur inconnu à l’avance, attente d’une condition vraie/fausse).
#
# NB : Dans les deux cas, break permet une sortie anticipée ; continue saute un tour.

