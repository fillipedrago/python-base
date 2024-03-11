#!/home/gitpod/.pyenv/shims/python
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Lista com 3 tuplas
atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
    ]

# Listar alunos em cada atividade por sala

# É possível desempacotar a tupla dentro de um for:

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    
    # sala 1 que tem intersecção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    
    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)
    print("-" * 50)

