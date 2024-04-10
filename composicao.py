""" Imrpime apenas os nomes iniciados com a letra B"""


names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian"
]

print(*list(filter(lambda name: name[0].lower() == "b", names)), sep="\n")