"""
Faça um script que pergunta ao usuário qual a temperatura atual 
e o indice de umidade do ar sendo que caso será exibida 
uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

    "ALERTA!!! 🥵♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo.

Ex:
python3 temp.py 
temperatura: 30
umidade: 90
... 
"ALERTA!!! 🥵♒ Perigo de calor úmido"

"""
import sys
import logging

info = {
    "temperatura": None,
    "umidade": None
    }


log = logging.Logger("alerta")

while True:
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break
    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f"Qual a {key}?: ").strip())    
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

temp, umidade = info.values() #unpachking

if temp > 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp >30 and temp * 3 >= umidade: #pemdas.info
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")