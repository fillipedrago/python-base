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
__version__ = "0.0.1"
__author__ = "Fillipe Drago"
__license__ = "Unlicensed"

import os

# a segunda entrada da variável getenv é o valor retornado seja nulo             
current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg: "Ciao, Mondo!"

print(msg)