# cria e manipula arquivos


def create_archives():
    linhas = ["linha 1\n", "linha 2\n", "linha 3\n", "linha 4\n", "linha 5\n"]
    file = open("teste.txt", "w+")
    file.writelines(linhas)
    file.write("linha 6")
    file.close()


create_archives()
