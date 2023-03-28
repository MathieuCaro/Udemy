path = "/mnt/c/c/Udemy/Udemy/Python/Python_base/Fichiers/read_file.txt"

with open(path,"r") as f: #r:read the file
    content = f.read().splitlines()
    #splitlines enables to have a list of the element of the file
    # as for separator the line break
    print(content)