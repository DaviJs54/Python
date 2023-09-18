import time
import os
l = [" "] * 64
k = 0
p = []
for x in range(8,0,-1):
    p.extend([f"a{x}",f"b{x}",f"c{x}",f"d{x}",f"e{x}",f"f{x}",f"g{x}",f"h{x}"])
for x in range(8,16):
    l[x] = "♙"
for x in range(48,56):
    l[x] = "♟"
l[0] = l[7] = "♖"
l[1] = l[6] = "♘"
l[2] = l[5] = "♗"
l[3] , l[4] = "♕" , "♔"

l[56] = l[63] = "♜"
l[57] = l[62] = "♞"
l[58] = l[61] = "♝"
l[59] , l[60] = "♛" , "♚"
#lb = ["♛" , "♚" , "♜" , "♞" , "♝" , "♟"]
#lp = ["♕" , "♔" , "♖" , "♘" , "♗" , "♙"]
def t():
    print("    a   b   c   d   e   f   g   h")
    i = 0.125
    for x in range(0,64,8):
        if x == 0:
            print("   _______________________________")
        print(8 if x == 0 else int(8-x/8) , "| " + l[x] + " | " + l[x+1] + " | " + l[x+2] + " | " + l[x+3] + " | " + l[x+4] + " | " + l[x+5] + " | " + l[x+6] + " | " + l[x+7] + " |" , 8 if x == 0 else int(8-x/8))
        if x < 56:
            print("  |---+---+---+---+---+---+---+---|")
        if x == 56:
            print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("    a   b   c   d   e   f   g   h")
while True:
    flag = 0
    if "♚" not in l and "♔" not in l:
        break
    for x in range(1,3):    
        if x == 1:    
            os.system('cls')
            t()
            j = input("Digite a peça que deseja mover:\n")
            while len(j) != 2 or j not in p:
                print('Digitação inválida')
                time.sleep(1)
                break
            if j in p:
                if l[p.index(j)] == "♟":
                    while True:
                        os.system('cls')
                        t()
                        jg = input(f'peça selecionada "♟ ", escolha o local que deseja move-la:\n')
                        if len(jg) != 2 or jg not in p:
                            print('Digitação inválida')
                            time.sleep(1)
                            continue
                        if p.index(j) - 7 == p.index(jg) or p.index(j) - 9 == p.index(jg):
                            if l[p.index(jg)] in ["♕" , "♔" , "♖" , "♘" , "♗" , "♙"]:
                                l[p.index(jg)] = "♟"
                                l[p.index(j)] = " "
                                break
                            else:
                                print("Não é possivel colocar a peça nessa posição.")
                        while l[p.index(jg)] != " ":
                            print("Não é possivel colocar a peça nessa posição.")
                            break
                        else: 
                            if p.index(j) in[47,48,49,50,51,52,53,54,55]:
                                if p.index(j) - 8 == p.index(jg) or p.index(j) - 16 == p.index(jg):
                                    l[p.index(jg)] = "♟"
                                    l[p.index(j)] = " "
                                    break
                                else:
                                    print("Não é possivel colocar a peça nessa posição.")
                            else:
                                if p.index(j) - 8 == p.index(jg):
                                    l[p.index(jg)] = "♟"
                                    l[p.index(j)] = " "
                                    break
                                else:
                                    print("Não é possivel colocar a peça nessa posição.")
                elif l[p.index(j)] == "♞":
                    while True:
                        jg = input(f'peça selecionada "♞ ", escolha o local que deseja move-la:\n')
                        if abs(p.index(j) - p.index(jg)) in (15, 17, -15, -17 , 10 , 6 , -10 , -6):
                            if l[p.index(jg)] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                l[p.index(jg)] = "♞"
                                l[p.index(j)] = " "
                                break
                            else:
                                print("Não é possivel colocar a peça nessa posição.")
                        else:
                            print("Não é possivel colocar a peça nessa posição.")
                elif l[p.index(j)] == "♝":
                    bp = []
                    for x in range(64):
                        if x < 8 or x > 15 and x < 24 or x > 31 and x < 40 or x > 47 and x < 56:
                            if x % 2 == 0:
                                bp.append(x)
                        else:
                            if x % 2 == 1:
                                bp.append(x)
                    while True:
                        jg = input(f'peça selecionada "♝ ", escolha o local que deseja move-la:\n')
                        if flag == 1:
                            break
                        
                        for x in range(1,8):
                            try:    
                                if l[p.index(j)+8*x+1] == l[p.index(jg)]:
                                    for y in range(1,x):
                                        if l[p.index(j)+8*y+1] != " ":
                                            print("Não é possivel colocar a peça nessa posição.")
                                            break
                                        else:
                                            l[p.index(jg)] = "♝"
                                            l[p.index(j)] = " "
                                            flag = 1
                                            break
                                elif l[p.index(j)+8*x-1] == l[p.index(jg)]:
                                    for y in range(1,x):
                                        if l[p.index(j)+8*y-1] != " ":
                                            print("Não é possivel colocar a peça nessa posição.")
                                            break
                                    else:
                                        l[p.index(jg)] = "♝"
                                        l[p.index(j)] = " "
                                        flag = 1
                                        break
                                elif l[p.index(j)-8*x-1] == l[p.index(jg)]:
                                    for y in range(1,x):
                                        if l[p.index(j)-8*y-1] != " ":
                                            print("Não é possivel colocar a peça nessa posição.")
                                            break
                                    else:
                                        l[p.index(jg)] = "♝"
                                        l[p.index(j)] = " "
                                        flag = 1
                                        break
                                elif l[p.index(j)-8*x+1] == l[p.index(jg)]:
                                    for y in range(1,x):
                                        if l[p.index(j)-8*y+1] != " ":
                                            print("Não é possivel colocar a peça nessa posição.")
                                            break
                                    else:
                                        l[p.index(jg)] = "♝"
                                        l[p.index(j)] = " "
                                        flag = 1
                                        break
                            except IndexError:
                                continue
                                
                                    
                            

