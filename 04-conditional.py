# estrutura de condicional


def sou_maior_de_idade():
    idade = int(input("insira sua idade: "))
    v_padrao = 18
    if idade > 100:
        print("tu devia está morto menor ")
    elif idade >= v_padrao:
        print("você é maior de idade")
    elif idade <= v_padrao:
        print("você é menor de idade")
    else:
        print('nem sei menor')


sou_maior_de_idade()
