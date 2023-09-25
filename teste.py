matriz = [[],[],[],[]]

for l in range(4):
    for c in range(4):
        matriz[l].append(f'-')

matriz[2][2] = "K"

for l in range(4):
    linha = " "
    for c in range(4):
        linha += matriz[l][c]+" "
    print(f"{linha}")