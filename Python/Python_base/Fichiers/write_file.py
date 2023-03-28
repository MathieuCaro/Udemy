path = "/mnt/c/c/Udemy/Udemy/Python/Python_base/Fichiers/write_file.txt"

with open(path,"a") as f: #w:write in the file /a:append to the file
    f.write("\n")
    f.write("Au revoir")