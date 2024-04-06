"""\
Este modulo serve apenas de anotação.
"""

# definição ou atribuição
# assinatura
# documentacao / docstring

def nome_da_funcao(a: int, b: int, c: int) -> int:
    """Esta função faz alco com a, b e c.

    Use esta função quando quiser a + b + c

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

print(nome_da_funcao(1, 2, 3))

def outra_funcao(a, b, c):
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2


####################################

# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de 2 numeros."""
    return n1 + n2

# normal
print(soma(10, 20))

# argumentos em sequencia /posicional
args = (20, 30) # tuple, list, str

# print(soma(args[0], args[1]))
print(soma(*args)) # desempacotando

# argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100} # dict, hashmap

#print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))


#############################

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650}
]

for item in lista_de_valores_para_somar:
    print(soma(**item))