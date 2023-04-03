"""
1) Écrire un programme Python qui permet de créer un fichier nommé myFile.txt et d'y écrire le texte suivant: 
"Python est un langage de programmation souple et flexible."

2) Écrire un programme en Python qui permet d'ajouter à la fin du fichier myFile.txt le contenu suivant:
''Ce contenu a été ajouté via un code Python ! ''.

"""

path = "Python_base/Fichiers/exercices_fichier/exercice3.txt"

with open(path, "w+") as f:
    f.write("Python est un langage de programmation souple et flexible.")

with open(path, "a") as f:
    f.write("Ce contenu a été ajouté via un code Python ! ")
