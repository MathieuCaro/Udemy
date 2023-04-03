"""
1)Ecrire un programme Python qui permet de créer un fichier sur le bureau nommé monFichier.txt et d'écrire le texte T="Python est un langage de programmation orienté objet".

2)Ecrire un programme Python qui permet lire le fichier  monFichier.txt.

"""

path = (
    "/mnt/c/c/Udemy/Udemy/Python/Python_base/Fichiers/exercices_fichier/exercice1.txt"
)

with open(path, "w+") as f:  # r:read the file
    f.write("Python est un langage de programmation orienté objet")


with open(path, "r") as f:
    content = f.read()  # stockage du contenu du fichier exercice1.txt dans content
    print(content)
