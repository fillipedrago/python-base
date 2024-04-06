names = ["Bruno", "Joao", "Bernardo", "Cintia", "Marcia"]

print(sorted(names, key=lambda name: name.count("a")))

print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

# Calculadora

operacao = input("operacao: [sum, mul, div, sub]:")
n1 = input("n1:").strip()
n2 = input("n2:").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")