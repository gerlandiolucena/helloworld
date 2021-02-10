def create_file(name):
    fileName = "%s_file.txt" % (name)
    with open(fileName,"w") as file:
        file.write("Arquivo criado utilizando python.\n")
        file.write("Autor: %s" % (name))

create_file("Gerlandio")