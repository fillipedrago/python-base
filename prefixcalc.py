#!/usr/bin/env python3                                                                             #!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

operations = ["sum", "sub", "mul", "div"]

if sys.argv[1] not in operations:
    print("Error, select valid operation.")
    sys.exit()

if len(sys.argv) == 1:
    operation = input("operação:")
    n1 = int(input("n1:"))
    n2= int(input("n2:"))
else:
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    operation = sys.argv[1]


if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(result)