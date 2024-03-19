#!/home/gitpod/.pyenv/shims/python
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de teconologia

$ notes.py read --tag=tech
...
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")

if arguments[0] not in cmds:
    print(f"Invalid command {argument[0]}")
    sys.exit(1)

if arguments[0] == "read":
    # leitura das notas
    key, value = arguments[1].split("=")
    tag = value.strip().lstrip("-")
    

if arguments[0] == "new":
    # criacao da nota
    title = arguments[1]
    tag = input("Tag:").strip()
    text = input("Text:\n")
    
    with open(filepath, "a") as arquivo:
        arquivo.write(f"Tag = {tag}\n")
        arquivo.write(f"{title}\n")
        print()
        arquivo.write(f"{text}\n")
        
