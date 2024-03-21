#!/home/gitpod/.pyenv/shims/python

"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Fillipe Drago"
__license__ = "Unlicensed"

import os
import sys


arguments = {"lang": None,"count": 1,}
# pega os argumentos da lsita do sys.argv do indice 1 pra frente 
# (não pega o nome do programa)

# as entradas na execucao apos o nome do programa entram na sys.argv
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("try with --key=value")
        sys.exit(1)

    key = key.lstrip("-").strip() # tirando traços do inicio e espaços
    value = value.strip() # tirando espaços

    if key not in arguments:
        print(f"Invalid Option ´{key}´")
        sys.exit() # programa para de executar
    
    arguments[key] = value

            
current_language = arguments["lang"]

# a segunda entrada da variável getenv é o valor retornado seja nulo 
if current_language is None:    
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]


# sets (Hash Table) - O(1) - constante
# dicts (Hash Table) - O(1) - constante

msg = {
    "en_US":"Hello World!",
    "pt_BR": "Olá, mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "it_IT": "Ciao, Mondo!",
}

# Ordem Complexidade O(n):

# if current_language == "pt_BR":
#     msg = "Olá, mundo!"
# elif current_language == "it_IT":
#     msg: "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg: "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"

# O(1) - constante

try:
    message = msg[current_language] # dicionario[chave]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * 
    int(arguments["count"])) #por padrao o input vem em texto