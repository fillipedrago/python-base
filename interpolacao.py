# email_tmpl = """
#    ...: Olá, %(nome)s
#    ...: 
#    ...: Tem interesse em comprar %(produto)s?
#    ...: 
#    ...: Este produto é ótimo para resolver
#    ...: %(texto)s
#    ...: 
#    ...: Clique agora em %(link)s
#    ...: 
#    ...: Apenas %(quantidade)d disponíveis!
#    ...: 
#    ...: Preço promocional %(preco).2f
#    ...: """

version = "0.1.1"

import sys
import os 

arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de e-mails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, templatename) #email_tmpl.txt

# Itera cada linha separada do arquivo, carrega cada linha de uma vez separada
# clientes = ["Maria", "Joao", "Bruno"]

for line in open(filepath):
    name, email = line.split(",")

    #TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print ("-" * 50)