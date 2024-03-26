#!/home/gitpod/.pyenv/shims/python

original = [1, 2, 3]

#For loops / Laço for

# Estruturada

dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

dados = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

# Funcional 

# List Comprehesion
dobrada = [n * 2 for n in original]
print (dobrada)

# Dict Comprehesion

dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
