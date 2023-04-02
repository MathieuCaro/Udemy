"""
1) - Écrire un programme en Python qui permet de créer un fichier nommé myFile.txt et d'ajouter les lignes suivantes:
Python Programming
Java Programming
C++ Programming
2) - Écrire un programme en Python qui permet d'échanger la troisième ligne avec la deuxième ligne du fichier myFile.txt.

"""

path = "Python_base/Fichiers/exercices_fichier/exercice4.txt"

with open(path, "w+") as f:
    f.writelines("Python Programming\nJava Programming\nC++ Programming\n")

with open(path, "r") as f:
    content = f.readlines()  # on met les lignes sous formes de listes
    ligne_2 = content[1]
    ligne_3 = content[2]
    content[1] = ligne_3
    content[2] = ligne_2

with open(path, "w") as f:
    f.writelines(content)
