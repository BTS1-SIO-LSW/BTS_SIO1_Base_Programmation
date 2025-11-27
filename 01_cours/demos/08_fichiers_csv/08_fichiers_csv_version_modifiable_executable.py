"""
Manipulation de fichiers CSV avec Python
----------------------------------------

Ce script illustre :

 - la création de fichiers CSV d'exemple
 - la lecture avec csv.reader et csv.DictReader
 - la vérification d'existence avec os.path.exists
 - l'utilisation de next() pour gérer l'en-tête
 - le stockage des données dans une liste
 - l'écriture avec csv.writer, csv.DictWriter, writerow, writerows
 - extrasaction='ignore' pour ignorer les champs en trop
 - le filtrage, le tri, la conversion de types
 - le nettoyage de chaînes (strip, lower, replace)


IMPORTANT (gestion des chemins) :
=========

- On NE met PAS de lettre de lecteur en dur (F:, C:, etc.).
- On s'appuie sur le RÉPERTOIRE DE TRAVAIL (current working directory).
- Ce répertoire de travail est celui où l'on ouvre le projet / le terminal,
  par exemple : .../BTS_SIO1/BTS_SIO1_Base_Programmation
  et non le répertoire dans lequel se trouve le script pyton 
  ie : BTS_SIO1/BTS_SIO1_Base_Programmation/01_cours/demos/08_fichiers_csv/08_fichiers_csv._version_modifiable_executable.py

Conséquence :

- Tous les fichiers CSV seront créés dans le même répertoire de travail,
  quel que soit le lecteur (F:, C:, D:) de l'élève .
"""

import csv
import os


# ---------------------------------------------------------------------------
# GESTION DU REPERTOIRE DE TRAVAIL
# ---------------------------------------------------------------------------

# current working directory = répertoire depuis lequel Python est lancé
WORKDIR = os.getcwd()

def chemin_fichier(nom_fichier: str) -> str:
    """
    Construit le chemin complet d'un fichier à partir du répertoire de travail.

    Exemple :
    - Si WORKDIR vaut "F:/BTS_SIO1/BTS_SIO1_Base_Programmation"
    - et que nom_fichier vaut "clients.csv"
    - alors le chemin complet sera "F:/BTS_SIO1/BTS_SIO1_Base_Programmation/clients.csv"

    ASTUCE PEDAGOGIQUE :
    - On ne met jamais "F:/..." ou "C:/..." en dur dans le code.
    - On laisse os.getcwd() et os.path.join() faire le travail.
    """
    return os.path.join(WORKDIR, nom_fichier)


# ---------------------------------------------------------------------------
# OUTILS D'AFFICHAGE
# ---------------------------------------------------------------------------

def titre(section: str) -> None:
    """Affiche un titre de section pour rendre le script plus lisible."""
    print("\n" + "=" * 70)
    print(section)
    print("=" * 70)


def sous_titre(texte: str) -> None:
    """Affiche un sous-titre."""
    print("\n" + "-" * 70)
    print(texte)
    print("-" * 70)


# ---------------------------------------------------------------------------
# 1. PRÉPARATION : CRÉATION D'UN FICHIER CSV D'EXEMPLE
# ---------------------------------------------------------------------------

def creer_fichier_clients_csv(nom_fichier: str = "clients.csv") -> None:
    """
    Crée un fichier CSV 'clients.csv' d'exemple dans le répertoire de travail.

    ASTUCE :
    - On utilise newline="" pour éviter les lignes vides sous Windows.
    - Le délimiteur ';' est le plus courant en France (compatibilité Excel).
    - Le fichier sera créé dans WORKDIR, pas à côté du script.
    """
    titre("1. Création d'un fichier CSV d'exemple")
    chemin = chemin_fichier(nom_fichier)

    donnees = [
        ["id", "nom", "email", "ville", "age", "mot_cle", "prix", "actif"],
        [1, "Martin", "martin@example.com", "Paris", 35, " Python course ", 19.99, "true"],
        [2, "Nicole", "nicole@example.com", "Lyon", 22, "csv   tutorial", 9.5, "false"],
        [3, "Dupont", "dupont@example.com", "Paris", 45, "  PYTHON CSV ", 29.0, "true"],
    ]

    with open(chemin, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(donnees)

    print(f"Dossier de travail : {WORKDIR}")
    print(f"Fichier '{chemin}' créé avec {len(donnees) - 1} lignes de données.")


# ---------------------------------------------------------------------------
# 2. VÉRIFICATION DE L'EXISTENCE D'UN FICHIER (os.path.exists)
# ---------------------------------------------------------------------------

def demo_os_path_exists(file_name: str = "clients.csv") -> None:
    """
    Vérifie l'existence du fichier CSV dans le répertoire de travail
    avant de le lire ou de le créer.

    ASTUCE :
    - Toujours vérifier l'existence des fichiers en production pour éviter
      les FileNotFoundError et gérer les cas manquants proprement.
    """
    titre("2. Vérification de l'existence d'un fichier CSV")

    chemin = chemin_fichier(file_name)

    if os.path.exists(chemin):
        print(f"Le fichier '{chemin}' existe, on peut le lire.")
        with open(chemin, "r", encoding="utf-8") as f:
            lecteur = csv.reader(f, delimiter=";")
            for ligne in lecteur:
                print(ligne)
    else:
        print(f"Le fichier '{chemin}' n'existe pas, création nécessaire.")
        with open(chemin, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["id", "nom", "email"])
        print(f"Fichier '{chemin}' créé avec seulement l'en-tête.")


# ---------------------------------------------------------------------------
# 3. LECTURE AVEC csv.reader ET csv.DictReader
# ---------------------------------------------------------------------------

def demo_lecture_reader(nom_fichier: str = "clients.csv") -> None:
    """
    Lecture d'un CSV avec csv.reader (chaque ligne = liste).

    ASTUCE :
    - Méthode simple, mais il faut connaître l'ordre des colonnes.
    """
    titre("3. Lecture avec csv.reader (liste)")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.reader(f, delimiter=";")
        for ligne in lecteur:
            print(ligne)


def demo_lecture_dictreader(nom_fichier: str = "clients.csv") -> None:
    """
    Lecture d'un CSV avec csv.DictReader (chaque ligne = dictionnaire).

    ASTUCE :
    - Accès par nom de colonne : plus lisible et plus robuste.
    """
    titre("4. Lecture avec csv.DictReader (dictionnaire)")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        for ligne in lecteur:
            print(f"Nom : {ligne['nom']} | Email : {ligne['email']} | Ville : {ligne['ville']}")


# ---------------------------------------------------------------------------
# 4. UTILISATION DE next() POUR GÉRER L'EN-TÊTE AVEC csv.reader
# ---------------------------------------------------------------------------

def demo_next_sur_entete(nom_fichier: str = "clients.csv") -> None:
    """
    Utilisation de next() pour lire l'en-tête et éviter qu'il soit traité comme une donnée.

    ASTUCE :
    - next(itérateur) lit la prochaine ligne et avance l'itérateur.
    - Très utile pour "sauter" l'en-tête avant de boucler sur les vraies données.
    """
    titre("5. Utilisation de next() pour gérer l'en-tête avec csv.reader")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.reader(f, delimiter=";")

        # Lire et stocker l'en-tête
        entete = next(lecteur)
        print(f"En-tête : {entete}")

        # Boucle sur les données uniquement
        for ligne in lecteur:
            print(f"Client : {ligne[1]}, Email : {ligne[2]}, Ville : {ligne[3]}")


# ---------------------------------------------------------------------------
# 5. STOCKER LES DONNÉES DANS UNE LISTE POUR TRAITEMENT ULTÉRIEUR
# ---------------------------------------------------------------------------

def demo_stockage_dans_liste(nom_fichier: str = "clients.csv") -> None:
    """
    Stocke toutes les lignes (hors en-tête) dans une liste Python.

    ASTUCE :
    - Idéal pour effectuer plusieurs traitements (tri, filtres) sans relire le fichier.
    """
    titre("6. Stockage des données CSV dans une liste Python")
    chemin = chemin_fichier(nom_fichier)

    mes_donnees = []
    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.reader(f, delimiter=";")
        entete = next(lecteur)
        print(f"Colonnes : {entete}")

        for ligne in lecteur:
            mes_donnees.append(ligne)
            print(f"Ligne ajoutée : {ligne}")

    print(f"\nNombre total de lignes (hors en-tête) : {len(mes_donnees)}")
    if mes_donnees:
        print(f"Première ligne : {mes_donnees[0]}")
        print(f"Dernière ligne : {mes_donnees[-1]}")


# ---------------------------------------------------------------------------
# 6. ÉCRITURE DANS UN FICHIER CSV (writer, DictWriter, writerows)
# ---------------------------------------------------------------------------

def demo_ecriture_writer(nom_fichier: str = "export_writer.csv") -> None:
    """
    Écriture de données dans un CSV avec csv.writer (listes).
    """
    titre("7. Écriture dans un CSV avec csv.writer")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["id", "produit", "prix"])
        writer.writerow([1, "Clavier", 45.99])
        writer.writerow([2, "Souris", 25.50])
        writer.writerow([3, "Écran", 299.00])

    print(f"Fichier '{chemin}' créé (écriture ligne par ligne).")


def demo_ecriture_writerows(nom_fichier: str = "export_writerows.csv") -> None:
    """
    Écriture de plusieurs lignes avec writerows().

    ASTUCE :
    - Plus performant et plus lisible quand on a beaucoup de lignes.
    """
    titre("8. Écriture multiple avec writerows()")
    chemin = chemin_fichier(nom_fichier)

    donnees = [
        ["id", "produit", "prix"],
        [1, "Clavier", 45.99],
        [2, "Souris", 25.50],
        [3, "Écran", 299.00],
    ]

    with open(chemin, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(donnees)

    print(f"Fichier '{chemin}' créé (writerows).")


def demo_ecriture_dictwriter() -> None:
    """
    Écriture dans un CSV avec csv.DictWriter, gestion de fieldnames et extrasaction.
    """
    titre("9. Écriture dans un CSV avec csv.DictWriter et extrasaction='ignore'")

    champs = ["id", "mot_cle", "volume"]

    # Exemple sans extrasaction (tous les champs doivent être dans fieldnames)
    sous_titre("9.1 DictWriter simple (champs stricts)")
    chemin_simple = chemin_fichier("export_dict.csv")
    with open(chemin_simple, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=champs, delimiter=";")
        writer.writeheader()
        writer.writerow({"id": 1, "mot_cle": "python cours", "volume": 1200})
    print(f"Fichier '{chemin_simple}' créé.")

    # Exemple avec extrasaction='ignore' : les champs en trop sont ignorés
    sous_titre("9.2 DictWriter avec extrasaction='ignore'")

    donnees = {
        "id": 1,
        "mot_cle": "python cours",
        "volume": 1200,
        "auteur": "Jean",        # champ en trop
        "date": "2024-01-15",    # champ en trop
    }

    chemin_ignore = chemin_fichier("export_dict_ignore.csv")
    with open(chemin_ignore, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=champs,
            delimiter=";",
            extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerow(donnees)

    print(f"Fichier '{chemin_ignore}' créé (champs 'auteur' et 'date' ignorés).")


# ---------------------------------------------------------------------------
# 7. MANIPULATIONS AVANCÉES : FILTRAGE, TRI, CONVERSIONS
# ---------------------------------------------------------------------------

def demo_filtrer_ville_paris(nom_fichier: str = "clients.csv") -> None:
    """
    Filtrer les clients qui habitent à Paris avec DictReader.
    """
    titre("10. Filtrer les données (ville == 'Paris')")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        print("Clients habitant à Paris :")
        for ligne in lecteur:
            if ligne["ville"] == "Paris":
                print(f"- {ligne['nom']} ({ligne['email']})")


def demo_tri_clients(nom_fichier: str = "clients.csv") -> None:
    """
    Trier les clients par nom (alphabétique) puis par âge (numérique).
    """
    titre("11. Tri des données (nom puis âge)")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        clients = list(lecteur)

    sous_titre("11.1 Tri alphabétique par nom")
    clients_tries_nom = sorted(clients, key=lambda c: c["nom"])
    for c in clients_tries_nom:
        print(f"{c['nom']} ({c['ville']})")

    sous_titre("11.2 Tri numérique par âge (croissant)")
    clients_tries_age = sorted(clients, key=lambda c: int(c["age"]))
    for c in clients_tries_age:
        print(f"{c['nom']} - {c['age']} ans")

    # ASTUCE : tri décroissant -> reverse=True
    sous_titre("11.3 Tri par âge (décroissant)")
    clients_tries_age_desc = sorted(clients, key=lambda c: int(c["age"]), reverse=True)
    for c in clients_tries_age_desc:
        print(f"{c['nom']} - {c['age']} ans")


def demo_conversions_et_nettoyage(nom_fichier: str = "clients.csv") -> None:
    """
    Illustration des conversions de types et du nettoyage de chaînes.
    """
    titre("12. Conversion de types et nettoyage des données")
    chemin = chemin_fichier(nom_fichier)

    with open(chemin, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        for ligne in lecteur:
            # Conversion str -> int / float / bool
            age_str = ligne["age"]
            age = int(ligne["age"])

            prix_str = ligne["prix"]
            prix = float(ligne["prix"])

            actif_str = ligne["actif"]
            actif = actif_str == "true"   # True si "true", False sinon

            # Nettoyage des mots-clés : strip + lower
            mot_cle_brut = ligne["mot_cle"]
            mot_cle_propre = mot_cle_brut.strip().lower()

            # Nettoyage "téléphone" (exemple fictif)
            tel_brut = "01 23 45-67-89"
            tel_propre = tel_brut.replace(" ", "").replace("-", "")

            print(f"--- Client {ligne['nom']} ---")
            print(f"Age (str -> int) : {age_str} -> {age}")
            print(f"Prix (str -> float) : {prix_str} -> {prix}")
            print(f"Actif (str -> bool) : {actif_str} -> {actif}")
            print(f"Mot clé brut      : '{mot_cle_brut}'")
            print(f"Mot clé nettoyé   : '{mot_cle_propre}'")
            print(f"Téléphone brut    : '{tel_brut}'")
            print(f"Téléphone nettoyé : '{tel_propre}'")
            print()


# ---------------------------------------------------------------------------
# POINT D'ENTRÉE PRINCIPAL
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Lancement séquentiel de toutes les démonstrations.
    Les étudiants peuvent commenter/décommenter des appels pour tester chaque partie.

    ASTUCE :
    - Affiche le répertoire de travail au début pour bien montrer où
      seront créés les fichiers CSV.
    """
    titre("0. Informations sur le répertoire de travail")
    print(f"Répertoire de travail (os.getcwd()) : {WORKDIR}")

    creer_fichier_clients_csv()        # 1. Création du fichier de base
    demo_os_path_exists()              # 2. Vérification d'existence et lecture brute

    demo_lecture_reader()              # 3. Lecture avec csv.reader
    demo_lecture_dictreader()          # 4. Lecture avec DictReader
    demo_next_sur_entete()             # 5. Utilisation de next() sur l'en-tête

    demo_stockage_dans_liste()         # 6. Stockage dans une liste

    demo_ecriture_writer()             # 7. Écriture avec writer
    demo_ecriture_writerows()          # 8. Écriture avec writerows
    demo_ecriture_dictwriter()         # 9. Écriture avec DictWriter

    demo_filtrer_ville_paris()         # 10. Filtrer les données
    demo_tri_clients()                 # 11. Tri
    demo_conversions_et_nettoyage()    # 12. Conversions et nettoyage


if __name__ == "__main__":
    main()
