
# Cf Documentation :
#    =============

#     _ Documentation officielle Python   :   https://docs.python.org/3/tutorial/controlflow.html
#     _ W3Schools                         :   https://www.w3schools.com/python/python_conditions.asp


# Les structures conditionnelles
mon_age = int(input("Quel est votre âge ? "))

if mon_age >= 21:  # La condition évaluée à l'entrée du bloc
    print("Vous êtes majeur aux USA, vous pouvez acheter ce produit !")
elif mon_age >= 18:  # La condition évaluée si la condition précédente n'est pas bonne
    print("Vous êtes majeur en France, vous pouvez acheter ce produit !")
else:  # Le chemin par défaut si aucune condition n'est bonne
    print("Vous êtes mineur, vous ne pouvez pas acheter ce produit !")

print("Code à la suite")

# Utilisation de if avec des opéteurs de comparaison mais aussi des opérateurs logiques
identifiant = str(input("Entrez votre identifiant : "))
mot_de_passe = int(input("Entrez votre mot de passe : "))

if identifiant == "admin" and mot_de_passe == 1234:
    print("Connexion réussie en tant qu'administrateur.")
elif identifiant == "user" and mot_de_passe == 6789:
    print("Connexion réussie en tant qu’utilisateur.")
else:
    print("Échec de connexion.")



# ------------------------------------------------------------
# Conditions multiples avec elif
# Exemple : appliquer des remises commerciales selon le CA
# ------------------------------------------------------------

chiffre_affaires = float(input("Entrez le chiffre d'affaires (€) : "))

if chiffre_affaires >= 1_000_000:
    print("Remise exceptionnelle de 15% accordée (CA >= 1M).")
elif chiffre_affaires >= 500_000:
    print("Remise de 10% accordée (CA >= 500k).")
elif chiffre_affaires >= 100_000:
    print("Remise de 5% accordée (CA >= 100k).")
else:
    print("Pas de remise.")

print("Fin du calcul des remises\n")


# ------------------------------------------------------------
# If imbriqués : calcul TVA + type de client
# ------------------------------------------------------------
# Objectif : calculer le montant TTC en fonction du pays et du statut client
# - France : TVA 20%
# - Allemagne : TVA 19%
# - Export hors UE : pas de TVA
# + Entreprise -> TVA récupérable, donc affichage différent

pays = input("Pays du client : ")
montant_ht = float(input("Montant HT (€) : "))
type_client = input("Type de client (entreprise / particulier) : ")

if pays.lower() == "france":
    tva = 0.20
    montant_ttc = montant_ht * (1 + tva)
    if type_client.lower() == "entreprise":
        print(f"Montant TTC = {montant_ttc:.2f} € (TVA récupérable).")
    else:
        print(f"Montant TTC = {montant_ttc:.2f} € (TVA payée).")
elif pays.lower() == "allemagne":
    tva = 0.19
    montant_ttc = montant_ht * (1 + tva)
    print(f"Montant TTC (Allemagne) = {montant_ttc:.2f} €")
else:
    print("Export hors UE : pas de TVA.")

print("Fin du calcul TVA\n")



# ------------------------------------------------------------
# Opérateurs logiques combinés (and, or, not)
# ------------------------------------------------------------
# Exemple : seuil de rentabilité
# Règle : 
# - Si CA > Charges et CA > 200k => Rentable au-dessus du seuil
# - Si CA > Charges mais < 200k => Rentable mais seuil pas atteint
# - Sinon => Déficitaire

charges = float(input("Entrez le total des charges (€) : "))

if chiffre_affaires > charges and chiffre_affaires > 200_000:
    print("Entreprise rentable et au-dessus du seuil.")
elif chiffre_affaires > charges and chiffre_affaires <= 200_000:
    print("Entreprise rentable mais seuil non atteint.")
else:
    print("Entreprise déficitaire.")

print("Fin du calcul de rentabilité\n")

# ---------------------------------------------------------------------------------------------
# Version abrégée (ternaire)
# Schéma de construction de ce if :       valeur_si_vrai if condition else valeur_si_faux
# ----------------------------------------------------------------------------------------------
# Exemple : bénéfice ou perte affiché directement

benefice = chiffre_affaires - charges
resultat = "Bénéfice" if benefice >= 0 else "Perte"
print(f"Résultat de l'exercice : {resultat} ({benefice:.2f} €)\n")

# ------------------------------------------------------------
# Contrôle de cohérence d’une facture
# ------------------------------------------------------------
# Hypothèses :
# - Une facture doit être >= 0
# - Si facture > 10 000 € et client particulier => avertissement (rare en pratique)
# - Si remise > 20% => alerte fraude
# - Si TVA < 0 => erreur

facture_ht = float(input("Montant HT de la facture (€) : "))
remise = float(input("Remise en % : ")) / 100
tva = float(input("TVA en % : ")) / 100
client = input("Type de client (particulier / entreprise) : ")

if facture_ht < 0:
    print("ERREUR : Montant négatif impossible.")
else:
    montant_remise = facture_ht * (1 - remise)
    montant_ttc = montant_remise * (1 + tva)

    if client.lower() == "particulier" and facture_ht > 10_000:
        print("Vérifier : Facture très élevée pour un particulier.")

    if remise > 0.20:
        print("Alerte : Remise supérieure à 20%, vérifier l'autorisation.")

    if tva < 0:
        print("ERREUR : TVA négative interdite.")
    else:
        print(f"Montant TTC après remise et TVA : {montant_ttc:.2f} €")

print("Fin du contrôle facture\n")



# ================================================================
# Cours : match / case en Python (≥ 3.10)
# ================================================================
# Objectif : simplifier les longues séries de if / elif / else
# Exemple typique : analyser une variable qui peut prendre
# plusieurs valeurs possibles.
#
#  Différence par rapport à if/elif :
# - if/elif : on compare plusieurs fois la variable avec l'opérateur de comparaison ==
# - match   : on écrit la variable une seule fois, puis on
#             définit les cas possibles (case)
#
# Pas de Fallthrough en Python :
# - Contrairement à certains langages (C, Java),
#   Python NE FAIT PAS de "fallthrough" (Traversée implicite") en français
# - Autrement dit en Python , dès qu’un case correspond, le code de ce case
#   s’exécute et les autres sont ignorés.
# - Donc pas besoin d’écrire "break".
# ================================================================

# Exemple 1 : comparer un choix utilisateur
choix = "facture"  # Essaie avec "devis", "contrat", ou autre

# Version classique avec if/elif/else
if choix == "facture":
    print("Création d'une facture")
elif choix == "devis":
    print("Création d'un devis")
elif choix == "contrat":
    print("Rédaction d'un contrat")
else:
    print("Opération inconnue")

# Version équivalente avec match
match choix:
    case "facture":
        print("Création d'une facture")
    case "devis":
        print("Création d'un devis")
    case "contrat":
        print("Rédaction d'un contrat")
    case _:  # _ = cas par défaut (équivalent de else)
        print("Opération inconnue")

# ==================================================================
# Introduction au pattern matching en Python
# ===================================================================
# Depuis Python 3.10, un nouveau mécanisme est apparu : le pattern matching (littéralement « correspondance de motifs »).
# Il est accessible avec la nouvelle structure match/case.
#
# Qu’est-ce qu’un pattern ?
#
# Un pattern est une forme de correspondance que Python va essayer d’associer à une valeur.
# En français, on pourrait traduire pattern par motif.
# Dans l'exemple ci-dessous "facture" , "devis" , "contrat" sont des patterns .
# Si la valeur testée correspond à un de ces motifs (patterns), alors le bloc associé à ce motif s’exécute :
#
# match choix:
#     case "facture":
#         print("Création d'une facture")
#     case "devis":
#         print("Création d'un devis")
#     case "contrat":
#         print("Rédaction d'un contrat")
#     case _:  # _ = cas par défaut (équivalent de else)
#         print("Opération inconnue")
#
# ==================================================================
# Pattern matching vs conditions classiques
# ==================================================================
# Avant Python 3.10, on utilisait if/elif/else pour comparer une variable à plusieurs valeurs.
# Avec match/case, on exprime la même logique mais de manière plus claire et plus lisible, surtout quand il y a beaucoup de cas.
#
# Parallèle avec les expressions régulières (regex) :
# ===================================================
# Vous avez peut-être déjà entendu parler des expressions régulières (regular expressions en anglais).
# Ce sont aussi des patterns, mais dans un autre contexte : elles servent à rechercher des motifs dans des chaînes de caractères (par exemple, vérifier si un email est valide).
#
# Exemple rapide :
#
import re
texte = "client@example.com"
if re.match(r"^[^@]+@[^@]+\.[^@]+$", texte):
    print("Email valide")
#
# Ici, ^[^@]+@[^@]+\.[^@]+$ est un pattern beaucoup plus complexe qu’un simple "facture" , "devis" ou "contrat". 
# La différence est que dans match/case, les patterns servent surtout à choisir quel bloc de code exécuter  , 
# selon la valeur d’une variable, tandis que dans les regex, ils servent à décrire une forme de texte dans une chaîne .

# À retenir :
#  ========
# Un pattern est une règle de correspondance .
# Traduction française : "motif" mais on utilisera plutôt le mot anglais "pattern".
# En Python, l'instruction match/case permet d’écrire des tests basés sur des patterns .
# Ce n’est pas la même chose que les expressions régulières, même si les deux notions partagent l’idée de « motif de correspondance ».




# ================================================================
# Exemple 2 : plusieurs valeurs possibles avec un seul case
statut = "en attente"  # Essaie aussi avec "payé", "annulé"

match statut:
    case "payé" | "validé":  # | signifie OU
        print("Paiement validé !")
    case "en attente" | "en cours":
        print("Paiement en cours !")
    case "refusé" | "annulé":
        print("Paiement refusé !")
    case _:
        print("Statut inconnu")

# ================================================================
# Exemple 3 : match est plus lisible que if/elif
note = 12

# Avec if/elif :
if note >= 16:
    print("Très bien")
elif note >= 10:
    print("Admis")
else:
    print("Refusé")

# Avec match + conditions de garde (if) :
# "Conditions de garde" se traduit par "Guard clauses" , en anglais .
# Ici x est un nom de variable réceptrice (on dit aussi qu’elle reçoit ou capture la valeur de note).
# Concrètement :
# Python affecte d’abord note à x.
# Ensuite, il vérifie la condition de garde if x >= 16.
# Si la condition est vraie, le bloc associé s’exécute :

match note:
    case x if x >= 16:
        print("Très bien")
    case x if x >= 10:
        print("Admis")
    case _:
        print("Refusé")


# Autre exemple : plusieurs valeurs avec OU + garde
jour = "samedi"
heure = 22

match jour:
    case "lundi" | "mardi" | "mercredi" if heure < 18:
        print("C'est un jour de semaine avant 18h : travail en cours ")
    case "samedi" | "dimanche" if heure >= 20:
        print("C'est le week-end tard le soir ")
    case "samedi" | "dimanche":
        print("C'est le week-end ")
    case _:
        print("Autre cas")

# ================================================================
# Bilan :
# - if/elif/else : universel, mais vite répétitif si beaucoup de cas
# - match/case   : plus lisible, surtout quand on compare UNE seule
#   variable à plusieurs valeurs possibles
# - pas de fallthrough en Python : un seul case s’exécute
# ================================================================



# ------------------------------------------------------------
# Conclusion
# ------------------------------------------------------------
# - Les conditions permettent d'appliquer des règles de gestion complexes.
# - On peut combiner if/elif/else, if imbriqués et opérateurs logiques.
# - Lisibilité et ordre des tests sont essentiels (toujours traiter les cas particuliers avant les cas généraux).