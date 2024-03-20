#!/home/gitpod/.pyenv/shims/python
import os
import sys




# LBYL - Look Before You Leap

# if os.path.exists("name.txt"):
#     print("O arquivo existe")
#     input("...") # Race Condition)
#     names = open("names.txt").readlines()
# else:
#     print("[Error] File names.txt not found")
#     sys.exit(1)

# if len(names) >= 3:
#     print(names[2])
# else:
#     print("[Error] Missing name in the list")
#     sys.exit(1)

# print(names[2])

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))


# EAFP - Easier to Ask Forgiveness than Permission
try:
     names = open("names.txt").readlines()
except FileNotFoundError as e: 
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else: 
    print ("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
