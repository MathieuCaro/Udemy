"""
1) Ecrire un programme en langage Python qui permet de créer un fichier nommé 'monFichier.txt' qui contient le texte 
T='Python est un langage de programmation orienté objet. Python est un langage de haut niveau. En outre Python est très populaire'.

2) Créer un autre programme Python permettant de remplacer le mot 'Python' par le mot 'Java' au sein du fichier  'monFichier.txt'

"""

path = (
    "/mnt/c/c/Udemy/Udemy/Python/Python_base/Fichiers/exercices_fichier/exercice2.txt"
)


# 1er programme
with open(path, "w+") as f:
    f.write(
        "Python est un langage de programmation orienté objet. \
        Python est un langage de haut niveau. En outre Python est très populaire"
    )

# 2eme programme
with open(path, "r") as f:
    content = f.read()
    modif = content.replace("Python", "Java")

with open(path, "w") as f:
    f.write(modif)
