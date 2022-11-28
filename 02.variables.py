# variavel inicializada

valor = 15
print(valor)

# concatencação de valores
is_string = "isso é uma strig ?"

print(is_string + " : True")

# o pyrhon não permite concatenar tipos diferentes

# print("isso é uma string mais um numero" +  10)
# a forma correta é transformar o numero em string
print("isso é uma string mais o numero " + str(10))

# o escopo das variaveis são global e local
# Uma variável local (criada dentro de uma função) existe apenas dentro da
# função onde foi declarada.
# Uma variável global é declarada (criada) fora das funções e pode ser
# acessada por todas as funções presentes no módulo onde é definida.


def global_or_local():
    is_string = "aqui sou uma variavel local"
    print(is_string)


global_or_local()

# ao declarar global is_string estou tornando essa variavel q estou utilizando
# na função e, global


def global_or_local2():
    global is_string
    is_string = "aqui sou uma variavel global"
    print(is_string)


global_or_local2()

print(is_string)
