import os
import json
from pathlib import Path

# ======================================================================
# CHAPITRE : MANIPULATION DE FICHIERS JSON
# Objectif : montrer 4 cas :
#   1) os      + open() / close()
#   2) os      + with open()
#   3) pathlib + open() / close()
#   4) pathlib + with .open()
#
# Encodage UTF-8 :
# - Gère les accents (é, è, à, ç, œ…)
# - Standard officiel JSON (RFC 8259)
# - Compatible Windows / Linux / Mac
# ======================================================================


# ======================================================================
# CHEMINS RELATIFS : signification
# ======================================================================
# .    = dossier courant
# ..   = dossier parent
# ./   = chemin depuis le dossier courant
# ../  = chemin depuis un dossier au-dessus
# ======================================================================


# ======================================================================
# SIGNIFICATION DE os.path.join ET os.path.abspath
# ======================================================================
# os.path.join(a, b, ...)  -> Assemble proprement un chemin selon l'OS.
# os.path.abspath(chemin)  -> Convertit un chemin relatif en chemin absolu.
# ======================================================================


# ======================================================================
# SIGNIFICATION DE pathlib_dir.resolve()
# ======================================================================
# .resolve() renvoie le chemin ABSOLU complet du fichier ou dossier.
# ======================================================================


# ======================================================================
# SIGNIFICATION DE parents=True et exist_ok=True
# ======================================================================
# parents=True  → crée automatiquement les dossiers parents si nécessaire.
# exist_ok=True → ne génère aucune erreur si le dossier existe déjà.
# ======================================================================


# ======================================================================
# DIFFÉRENCE ENTRE encoding="utf-8" ET ensure_ascii=False
# ======================================================================
# encoding="utf-8" :
#   → s'applique au FICHIER.
#   → garantit que l’écriture utilise l’encodage UTF-8.
#
# ensure_ascii=False :
#   → s'applique au CONTENU JSON.
#   → empêche la conversion des accents en codes Unicode.
#
# Exemple :
#   "é" →  avec ensure_ascii=True  : "\u00e9"
#          avec ensure_ascii=False : "é"
#
# Les deux sont complémentaires :
#   - UTF-8 évite les erreurs d’encodage.
#   - ensure_ascii=False garde les accents visibles dans le fichier JSON.
# ======================================================================


# ======================================================================
# Dictionnaire utilisé dans tous les exemples
# ======================================================================

mon_dict = {
    "people": ["Albert", "Martin", "Louis"],
    "mes_chiens": [1, 2, 4, 5]
}

print("Dictionnaire de départ :", mon_dict)


# ======================================================================
# 1) os + open() / close()
# ======================================================================

print("\n=== 1) os + open() / close() ===")

os_dir = "./data_os"
os_file_open_close = os.path.join(os_dir, "os_open_close.json")

os_dir_abs = os.path.abspath(os_dir)
os_file_open_close_abs = os.path.abspath(os_file_open_close)

print("Dossier (relatif) :", os_dir)
print("Dossier (absolu)  :", os_dir_abs)

os.makedirs(os_dir, exist_ok=True)

# --- ÉCRITURE ---
try:
    f = open(os_file_open_close, "w", encoding="utf-8")
    json.dump(mon_dict, f, indent=4, ensure_ascii=False)
    f.close()
    print("Fichier JSON écrit :", os_file_open_close_abs)
except OSError as e:
    print("[ERREUR écriture os] :", e)

# --- LECTURE ---
try:
    f = open(os_file_open_close, "r", encoding="utf-8")
    data_os_open_close = json.load(f)
    f.close()
    print("Lecture :", data_os_open_close)
except Exception as e:
    print("[ERREUR lecture os] :", e)


# ======================================================================
# 2) os + with open()
# ======================================================================

print("\n=== 2) os + with open() ===")

os_file_with = os.path.join(os_dir, "os_with.json")

# --- ÉCRITURE ---
try:
    with open(os_file_with, "w", encoding="utf-8") as f:
        json.dump(mon_dict, f, indent=4, ensure_ascii=False)
    print("Fichier JSON écrit :", os.path.abspath(os_file_with))
except OSError as e:
    print("[ERREUR écriture with os] :", e)

# --- LECTURE ---
try:
    with open(os_file_with, "r", encoding="utf-8") as f:
        data_os_with = json.load(f)
    print("Lecture :", data_os_with)
except Exception as e:
    print("[ERREUR lecture with os] :", e)


# ======================================================================
# 3) pathlib + open() / close()
# ======================================================================

print("\n=== 3) pathlib + open() / close() ===")

pathlib_dir = Path("data_pathlib")
pathlib_file_open_close = pathlib_dir / "pathlib_open_close.json"

print("Chemin absolu pathlib :", pathlib_dir.resolve())

pathlib_dir.mkdir(parents=True, exist_ok=True)

# --- ÉCRITURE ---
try:
    f = open(pathlib_file_open_close, "w", encoding="utf-8")
    json.dump(mon_dict, f, indent=4, ensure_ascii=False)
    f.close()
    print("Fichier JSON écrit :", pathlib_file_open_close.resolve())
except OSError as e:
    print("[ERREUR écriture pathlib] :", e)

# --- LECTURE ---
try:
    f = open(pathlib_file_open_close, "r", encoding="utf-8")
    data_pathlib_open_close = json.load(f)
    f.close()
    print("Lecture :", data_pathlib_open_close)
except Exception as e:
    print("[ERREUR lecture pathlib] :", e)


# ======================================================================
# 4) pathlib + with .open()
# ======================================================================

print("\n=== 4) pathlib + with .open() ===")

pathlib_file_with = pathlib_dir / "pathlib_with.json"

# --- ÉCRITURE ---
try:
    with pathlib_file_with.open("w", encoding="utf-8") as f:
        json.dump(mon_dict, f, indent=4, ensure_ascii=False)
    print("Fichier JSON écrit :", pathlib_file_with.resolve())
except OSError as e:
    print("[ERREUR écriture pathlib with] :", e)

# --- LECTURE ---
try:
    with pathlib_file_with.open("r", encoding="utf-8") as f:
        data_pathlib_with = json.load(f)
    print("Lecture :", data_pathlib_with)
except Exception as e:
    print("[ERREUR lecture pathlib with] :", e)


# ======================================================================
# BONUS : dumps() + loads()
# ======================================================================

print("\n=== BONUS : dumps() / loads() ===")

json_str = json.dumps(mon_dict, indent=4)
print("Chaîne JSON :", json_str)

data_from_string = json.loads(json_str)
print("Reconversion JSON → dict :", data_from_string)
