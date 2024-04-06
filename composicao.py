names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian"
]

# TODO: Usar lambda

# Função de composição

def starts_with_b(text):
    return text[0].lower() == "b"

print(*list(filter(starts_with_b, names)))