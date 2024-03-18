#!/home/gitpod/.pyenv/shims/python
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Exercício feito com dicionários.

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]


salas = {
    "sala1": sala1,
    "sala2": sala2,
}

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

# É possível desempacotar a tupla dentro de um for:

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    
    for sala in salas:
        atividade_sala = set(sala) & set(atividade)
        print(f"{sala}", atividade_sala)
        print("-" * 50)

