path = "/mnt/c/c/Udemy/Udemy/Python/Python_base/Fichiers/fichier1.txt"

with open(path, "r") as f:  # r:read the file
    content = f.read().splitlines()  #
    # content becomes a list
    # splitlines enables to have a list of the element of the file
    # as for separator the line break
    print(content)

with open(path, "w") as f:  # r:read the file
    content = f.readlines()
    content[3] = "Désole la ligne a été modifiée "
    f.seek(0)
    f.writelines(content)
