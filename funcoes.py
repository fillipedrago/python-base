"""Exemplos de funções"""

"""
f(x) = 5 * (x/2)

"""

def f(x): # assinatura
    result = 5 * (x / 2)
    return result 

def double(x):
    return x * 2

def print_in_upper(text):
    "Procedure with no explicit return"
    print(text.upper())
    # impicit return None

def heron(a, b, c):
    "Calcula a área de um triangulo"
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s-a) * (s-b) * (s-c)
    return area ** 0.5 # math.sqrt(area)

# def heron2(params):
#     return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17)
]

# print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")