
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)
    print(f"timeout {timeout}")



funcao(
    "Bruno", 
    1, 
    True, 
    timeout=90, 
    nome="Joao", 
    cidade="Viana", 
    data="hoje")