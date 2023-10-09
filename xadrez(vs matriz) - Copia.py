import os
import time
l = [[],[],[],[],[],[],[],[]]
for c in range(8):
    for x in range(8):
        l[c].append(" ")
p = []
for x in range(8,0,-1):
    p.extend([[f"a{x}",f"b{x}",f"c{x}",f"d{x}",f"e{x}",f"f{x}",f"g{x}",f"h{x}"]])
for x in range(8):
    l[1][x] = "♙"
    l[6][x] = "♟" 
l[0][0] = l[0][7] = "♖" 
l[7][0] = l[7][7] = "♜" 
l[0][1] = l[0][6] = "♘" 
l[7][1] = l[7][6] = "♞"
l[0][2] = l[0][5] = "♗"
l[7][2] = l[7][5] = "♝"
l[7][3] , l[7][4] = "♛" , "♚"
l[0][3] , l[0][4] = "♕" , "♔"
def t():
    print("    a   b   c   d   e   f   g   h")
    print("  ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    for x in range(8):
        print(8 if x == 0 else int(8-x),end='')
        linha = " │"
        for c in range(8):
            linha += " " + l[x][c]+" │"
        print(linha)
        if x != 7:
            print("  ├───┼───┼───┼───┼───┼───┼───┼───┤")
    print("  └───┴───┴───┴───┴───┴───┴───┴───┘")
n = len(l)
k = 0
l1 = []

while True:
    x1 = [0,1,2,3]
    y1 = [7,6,5,4]
    for ç in range(2):
        os.system('cls')
        if ç == 0:
            if k == 1:
                l.reverse()
        else:
            k = 1
            l.reverse()
        flag = 0
        ll = []
        pp = []
        for x in range(8):
            for y in range(8):
                ll.append(l[x][y])
                pp.append(p[x][y])   
        os.system('cls')
        t()
        if "♚" not in ll:
            print("Pretas vencem!")
            break
        if "♔" not in ll:
            print("Brancas Vencem!")
            break
        while True:
            os.system('cls')
            t()
            j = input("Digite a peça que deseja mover:\n")
            if len(j) != 2 or j not in pp or ll[pp.index(j)] == " ":
                print('Digitação inválida')
                time.sleep(1)
            else:
                break
        while True:
            os.system('cls')
            t()
            jg = input(f'peça selecionada "{ll[pp.index(j)]} ", escolha o local que deseja move-la:\n')
            if len(jg) != 2 or j not in pp:
                print('Digitação inválida')
                time.sleep(1)
            else:
                break
        if ç == 0:
            if ll[pp.index(j)] == "♟":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for c in range(8):
                                for z in range(8):
                                    if p[z][c] == jg and l[z][c] != " ": 
                                        print("Não é possivel colocar a peça nessa posição.")
                                        time.sleep(1)
                                        flag = 1
                                        break
                            if flag == 1:
                                break
                            if x == 6:
                                for i in range(1,3):
                                    if p[x-i][y] == jg:
                                        a = l[x-i][y]
                                        l[x-i][y] = "♟"
                                        l[x][y] = " "
                                        flag = 1
                                        for u in range(i):
                                            if l[x-u][y] != " ":
                                                print("Não é possivel colocar a peça nessa posição.")
                                                l[x-i][y] = a
                                                l[x][y] = "♟" 
                                                flag = 0
                                                break
                            for i in[1,-1]:
                                try:
                                    if p[x-1][y+i] == jg and l[x-1][y+i] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙"]:
                                        l[x-1][y+i] = "♟"
                                        l[x][y] = " "
                                        flag = 1
                                        break
                                except IndexError:
                                    continue
                            if flag == 1:
                                break
                            elif p[x-1][y] == jg and l[x-1][y] == " ":
                                l[x-1][y] = "♟"
                                l[x][y] = " "
                            else:
                                print("Não é possivel colocar a peça nessa posição.")
                                time.sleep(1)
            elif ll[pp.index(j)] == "♞":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in[2 , -2]:
                                for u in[1 , -1]:
                                    try:
                                        if p[x+u][y+i] == jg and l[x+u][y+i] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+u][y+i] = "♞"
                                            l[x][y] = " "
                                        elif p[x+i][y+u] == jg and l[x+i][y+u] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+i][y+u] = "♞"
                                            l[x][y] = " "
                                        elif p[x-2][y+1] == jg and l[x-2][y+1] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x-2][y+1] = "♞"
                                            l[x][y] = " "
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♜":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for o in[1 , -1]:
                                    try:
                                        if p[x-(i*o)][y] == jg and l[x-(i*o)][y] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            a = l[x-(i*o)][y]
                                            l[x-(i*o)][y] = "♜"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x-(u*o)][y] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x-(i*o)][y] = a
                                                    l[x][y] = "♜"
                                                    time.sleep(1)
                                                    break
                                        elif p[x][y-(i*o)] == jg and l[x][y-(i*o)] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            a = l[x][y-(i*o)]
                                            l[x][y-(i*o)] = "♜"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x][y-(u*o)] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x][y-(i*o)] = a
                                                    l[x][y] = "♜"
                                                    time.sleep(1)
                                                    break
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♚":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in[1,-1]:
                                for u in[1,-1]:
                                    try:
                                        if p[x+i][y+u] == jg and l[x+i][y+u] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+i][y+u] = "♚"
                                            l[x][y] = " "
                                        elif p[x][y+u] == jg and l[x][y+u] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x][y+u] = "♚"
                                            l[x][y] = " "
                                        elif p[x+i][y] == jg and l[x+i][y] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+i][y] = "♚"
                                            l[x][y] = " "
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♝":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for u in[1 , -1]:
                                    for z in[1 , -1]:
                                        try:
                                            if p[x+(i*u)][y+(i*z)] == jg and l[x+(i*u)][y+(i*z)] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                                a = l[x+(i*u)][y+(i*z)]
                                                l[x+(i*u)][y+(i*z)] = "♝"
                                                l[x][y] = " "
                                                for r in range(i):
                                                    if l[x+(r*u)][y+(r*z)] != " ":
                                                        print("Não é possivel colocar a peça nessa posição.")
                                                        l[x+(i*u)][y+(i*z)] = a
                                                        l[x][y] = "♝"
                                                        time.sleep(1)
                                                        break
                                        except IndexError:
                                            continue
            elif ll[pp.index(j)] == "♛":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for u in[1 , -1]:
                                    for z in[1 , -1]:
                                        try:
                                            if p[x+(i*u)][y+(i*z)] == jg and l[x+(i*u)][y+(i*z)] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                                a = l[x+(i*u)][y+(i*z)]
                                                l[x+(i*u)][y+(i*z)] = "♛"
                                                l[x][y] = " "
                                                for r in range(i):
                                                    if l[x+(r*u)][y+(r*z)] != " ":
                                                        print("Não é possivel colocar a peça nessa posição.")
                                                        l[x+(i*u)][y+(i*z)] = a
                                                        l[x][y] = "♛"
                                                        time.sleep(1)
                                                        break
                                        except IndexError:
                                            continue
                                for o in[1 , -1]:
                                    try:
                                        if p[x-(i*o)][y] == jg and l[x-(i*o)][y] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            a = l[x-(i*o)][y]
                                            l[x-(i*o)][y] = "♛"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x-(u*o)][y] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x-(i*o)][y] = a
                                                    l[x][y] = "♛"
                                                    time.sleep(1)
                                                    break
                                        elif p[x][y-(i*o)] == jg and l[x][y-(i*o)] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            a = l[x][y-(i*o)]
                                            l[x][y-(i*o)] = "♛"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x][y-(u*o)] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x][y-(i*o)] = a
                                                    l[x][y] = "♛"
                                                    time.sleep(1)
                                                    break
                                    except IndexError:
                                        continue
        elif ç == 1:
            if ll[pp.index(j)] == "♙":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for c in range(8):
                                for z in range(8):
                                    if p[z][c] == jg and l[z][c] != " ": 
                                        print("Não é possivel colocar a peça nessa posição.")
                                        time.sleep(1)
                                        flag = 1
                                        break
                            if flag == 1:
                                break
                            if x == 6:
                                for i in range(1,3):
                                    if p[x-i][y] == jg:
                                        a = l[x-i][y]
                                        l[x-i][y] = "♙"
                                        l[x][y] = " "
                                        flag = 1
                                        for u in range(i):
                                            if l[x-u][y] != " ":
                                                print("Não é possivel colocar a peça nessa posição.")
                                                l[x-i][y] = a
                                                l[x][y] = "♙" 
                                                flag = 0
                                                break
                            for i in[1,-1]:
                                if p[x-1][y+i] == jg and l[x-1][y+i] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟"]:
                                    l[x-1][y+i] = "♙"
                                    l[x][y] = " "
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                            elif p[x-1][y] == jg and l[x-1][y] == " ":
                                l[x-1][y] = "♙"
                                l[x][y] = " "
                            else:
                                print("Não é possivel colocar a peça nessa posição.")
                                time.sleep(1)
            elif ll[pp.index(j)] == "♘":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in[2 , -2]:
                                for u in[1 , -1]:
                                    try:
                                        if p[x+u][y+i] == jg and l[x+u][y+i] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+u][y+i] = "♘"
                                            l[x][y] = " "
                                        elif p[x+i][y+u] == jg and l[x+i][y+u] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x+i][y+u] = "♘"
                                            l[x][y] = " "
                                        elif p[x-2][y+1] == jg and l[x-2][y+1] in["♕" , "♔" , "♖" , "♘" , "♗" , "♙" , " "]:
                                            l[x-2][y+1] = "♘"
                                            l[x][y] = " "
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♖":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for o in[1 , -1]:
                                    try:
                                        if p[x-(i*o)][y] == jg and l[x-(i*o)][y] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            a = l[x-(i*o)][y]
                                            l[x-(i*o)][y] = "♖"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x-(u*o)][y] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x-(i*o)][y] = a
                                                    l[x][y] = "♖"
                                                    time.sleep(1)
                                                    break
                                        elif p[x][y-(i*o)] == jg and l[x][y-(i*o)] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟" , " "]:
                                            a = l[x][y-(i*o)]
                                            l[x][y-(i*o)] = "♖"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x][y-(u*o)] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x][y-(i*o)] = a
                                                    l[x][y] = "♖"
                                                    time.sleep(1)
                                                    break
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♔":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in[1,-1]:
                                for u in[1,-1]:
                                    try:
                                        if p[x+i][y+u] == jg and l[x+i][y+u] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            l[x+i][y+u] = "♔"
                                            l[x][y] = " "
                                        elif p[x][y+u] == jg and l[x][y+u] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            l[x][y+u] = "♔"
                                            l[x][y] = " "
                                        elif p[x+i][y] == jg and l[x+i][y] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            l[x+i][y] = "♔"
                                            l[x][y] = " "
                                    except IndexError:
                                        continue
            elif ll[pp.index(j)] == "♗":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for u in[1 , -1]:
                                    for z in[1 , -1]:
                                        try:
                                            if p[x+(i*u)][y+(i*z)] == jg and l[x+(i*u)][y+(i*z)] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                                a = l[x+(i*u)][y+(i*z)]
                                                l[x+(i*u)][y+(i*z)] = "♗"
                                                l[x][y] = " "
                                                for r in range(i):
                                                    if l[x+(r*u)][y+(r*z)] != " ":
                                                        print("Não é possivel colocar a peça nessa posição.")
                                                        l[x+(i*u)][y+(i*z)] = a
                                                        l[x][y] = "♗"
                                                        time.sleep(1)
                                                        break
                                        except IndexError:
                                            continue
            elif ll[pp.index(j)] == "♕":
                for x in range(8):
                    for y in range(8):
                        if p[x][y] == j:
                            for i in range(8):
                                for u in[1 , -1]:
                                    for z in[1 , -1]:
                                        try:
                                            if p[x+(i*u)][y+(i*z)] == jg and l[x+(i*u)][y+(i*z)] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                                a = l[x+(i*u)][y+(i*z)]
                                                l[x+(i*u)][y+(i*z)] = "♕"
                                                l[x][y] = " "
                                                for r in range(i):
                                                    if l[x+(r*u)][y+(r*z)] != " ":
                                                        print("Não é possivel colocar a peça nessa posição.")
                                                        l[x+(i*u)][y+(i*z)] = a
                                                        l[x][y] = "♕"
                                                        time.sleep(1)
                                                        break
                                        except IndexError:
                                            continue
                                for o in[1 , -1]:
                                    try:
                                        if p[x-(i*o)][y] == jg and l[x-(i*o)][y] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            a = l[x-(i*o)][y]
                                            l[x-(i*o)][y] = "♕"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x-(u*o)][y] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x-(i*o)][y] = a
                                                    l[x][y] = "♕"
                                                    time.sleep(1)
                                                    break
                                        elif p[x][y-(i*o)] == jg and l[x][y-(i*o)] in["♛" , "♚" , "♜" , "♞" , "♝" , "♟", " "]:
                                            a = l[x][y-(i*o)]
                                            l[x][y-(i*o)] = "♕"
                                            l[x][y] = " "
                                            for u in range(i):
                                                if l[x][y-(u*o)] != " ":
                                                    print("Não é possivel colocar a peça nessa posição.")
                                                    l[x][y-(i*o)] = a
                                                    l[x][y] = "♕"
                                                    time.sleep(1)
                                                    break
                                    except IndexError:
                                        continue








    

                                    

                

        



                        
                    
                
        

    



        
        
