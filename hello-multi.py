#!/home/gitpod/.pyenv/shims/python

"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Fillipe Drago"
__license__ = "Unlicensed"

import os

# a segunda entrada da variável getenv é o valor retornado seja nulo             
current_language = os.getenv("LANG", "en_US")[:5]


# sets (Hash Table) - O(1) - constante
# dicts (Hash Table) - O(1) - constante

msg = {
    "en_US":"Hello World!",
    "pt_BR": "Olá, mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde",
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
print(msg[current_language]) #dicionario[chave]