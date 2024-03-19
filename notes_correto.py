"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de teconologia

$ notes.py read tech
...
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag == arguments[1].lower():
            print(f"titulo: {title}")
            print(f"text: {text}")
            print("-" * 30)
    

if arguments[0] == "new":
    # criacao da nota
    title = arguments[1] # TODO: Tratar excepction
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv -> tab separated values
    # o with open itera cada um dos elementos da lista e vai appendando com tab:
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
   
    