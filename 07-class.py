# classes, aqui no pyhton this é igual a self, e __init__ é o construtor

class cachorro:
    def __init__(self):
        self.nome = "dog"

    def mudar_nome(self, params):
        self.nome = str(params)


tipo = cachorro()

print(tipo.nome)
tipo.mudar_nome("flaco")
print(tipo.nome)
