import os, json  # Pour manipuler le JSON, il nous faut le module JSON

file_path = './file.json'
mon_dict = {'people': ['Albert', 'Martin', 'Louis'], 'mes Chiens': [1, 2, 4, 5]}


# Pour manipuler les JSON fichiers, il nous faut
# accéder aux deux méthodes ci-dessous
if os.path.exists(file_path):
    file = open(file_path, 'r')
    # Une fois le chargement du JSON,
    # on obtient ici une liste de dictionnaire
    # car le JSON contient plusieurs éléments dans un tableau

    # Pour charger un fichier dans un dictionnaire,
    # il nous faut la méthode .load()
    data = json.load(file)
    file.close()
    print(data)
else:
    file = open(file_path, 'w')

    # Pour sauvegarder un objet dans un JSON, il nous
    # faut la méthode .dump() (indent sert à avoir
    # une présentation plus esthétique)
    json.dump(mon_dict, file, indent=4)
    file.close()

# Pour obtenir la variable string qui va être la représentation textuelle d'un objet,
# on peut se servir de la méthode .dumps() (Avec indent=XXX pour
# l'esthétique ) qui va retourner un string
json_str = json.dumps(mon_dict, indent=4)
print(json_str)
print(type(json_str))

# Pour transformer une chaine de caractère au format JSON en
# un dictionnaire, il existe la méthode .loads() qui
# va retourner un dictionnaire
data = json.loads(json_str)
print(data)
print(type(data))
print(data['people'])