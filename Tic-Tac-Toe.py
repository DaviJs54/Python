p = 0
flag = 0
import os
import random
import time
l = [" "] * 9
def d():
    for x in range(len(z)):
        print(z[x] , end='')
        time.sleep(0.025)
    time.sleep(0.5)
def t():
    print(l[0] + " | " + l[1] + " | " + l[2])
    print('--+---+--')
    print(l[3] + " | " + l[4] + " | " + l[5])
    print('--+---+--')
    print(l[6] + " | " + l[7] + " | " + l[8])
z = "Bem vindo ao jogo da velha com o bot inteligente!\n"
d()
z = "Regras:\n"
d()
z = "Para selecionar a posição, digite um número de 1 a 9, como demonstrado a seguir:"
d()
z = """ 
(1) | (2) | (3)
----+-----+----
(4) | (5) | (6)
----+-----+----
(7) | (8) | (9)\n
    """
d()
z = 'Boa Sorte! Digite qualquer tecla para começar:\n'
d()
input()
while True:    
    l = [" "] * 9
    if p == 1:
        os.system('cls')
        z = "Finalizando Programa..."
        d()
        break
    if flag == 1:
        while True:
            os.system('cls')
            z = ("1-Jogar Novamente\n"
                "2-Ver Regras Novamente\n"
                "3-Sair\n")
            d()
            x = input()
            try:
                x = int(x)
                if x == 1:
                    flag = 0
                    break
                elif x == 2:
                    os.system('cls')
                    z = "Regras:\n"
                    d()
                    z = "Para selecionar a posição, digite um número de 1 a 9, como demonstrado a seguir:"
                    d()
                    z = """ 
                    (1) | (2) | (3)
                    ----+-----+----
                    (4) | (5) | (6)
                    ----+-----+----
                    (7) | (8) | (9)\n
                        """
                    d()
                    z = 'Digite qualquer tecla para retornar:\n'
                    d()
                    input()
                    break
                elif x == 3:
                    p = 1
                    break
                else:
                    z = f"O número {x} não está disponível para opção."
                    d()
            except ValueError:
                z = "Vc não digitou um número."
                d()
    else:
        os.system('cls')
        b = "XO"
        z = "Escolhendo X e O...\n"
        d()
        time.sleep(1)
        bot = random.choice(b)
        p = "X" if bot == "O" else "O"
        z = f"Vc será o {p}.\n"
        d()
        time.sleep(1)
        os.system('cls')
        z = "Escolhendo quem irá iniciar...\n"
        d()
        time.sleep(1)
        start = random.randint(0,1)
        if start == 1:
            z = "O bot iniciará."
            d()
            time.sleep(1)
        else:
            z = "Vc iniciará."
            d()
            time.sleep(1)
        for x in range(1,12):
            flag = 0
            if l[0] == l[1] == l[2] != " " or l[3] == l[4] == l[5] != " " or l[6] == l[7] == l[8] != " " or l[0] == l[3] == l[6] != " " or l[1] == l[4] == l[7] != " " or l[2] == l[5] == l[8] != " " or l[0] == l[4] == l[8] != " " or l[2] == l[4] == l[6] != " ":
                if l[0] == l[1] == l[2] == bot or l[3] == l[4] == [5] == bot or l[6] == l[7] == l[8] == bot or l[0] == l[3] == l[6] == bot or l[1] == l[4] == l[7] == bot or l[2] == l[5] == l[8] == bot or l[0] == l[4] == l[8] == bot or l[2] == l[4] == l[6] == bot:
                    os.system('cls')
                    t()
                    z = "Vc perdeu!"
                    d()
                    flag = 1
                    break    
                else:
                    os.system('cls')
                    t()
                    z = "Vc venceu!"
                    d()
                    flag = 1
                    break
            elif all(item != " " for item in l):
                os.system('cls')
                t()
                z= 'Empate!'
                d()
                flag = 1
                break 
            if x % 2 == start:
                for y in range(1,4):
                    e = bot if y == 1 else p
                    if y == 3:
                        while True:
                            s=random.randint(1,9)
                            if l[s-1] == " ":
                                l[s-1] = bot
                                flag = 1
                                break
                            else:
                                continue
                    if flag == 1:
                        break
                    ll = [
                        l[1,2],l[3,6],l[4,8],
                        l[4,7],l[0,2],l[0,1],
                        l[5,8],l[4,6],l[0,6],
                        l[4,5],l[3,5],l[1,7],
                        l[0,8],l[2,8],l[3,4],
                        l[0,3],l[2,4],l[7,8],
                        l[1,4],l[6,8],l[0,4],
                        l[2,5],l[6,7],l[0,5]
                    ]
                    x=0
                    y=0
                    while(y<9):
                        if ll[x] == e and l[y] == " ":
                            l[y] = bot
                            break
                        x+=1
                        if x % 3 == 0:
                            y+=1                  
                    # for x in range(0,9,3):
                    #     if ll[x] == e and l[x] == " ":
                    #         l[x] = bot
                    #         break
                    
                    # if l[1] == l[2] == e and l[0] == " ":
                    #     l[0] = bot
                    #     break
                    # elif l[3] == l[6] == e and l[0] == " ":
                    #     l[0] = bot
                    #     break
                    # elif l[4] == l[8] == e and l[0] == " ":
                    #     l[0] = bot
                    #     break
                    # elif l[4] == l[7] == e and l[1] == " ":
                    #     l[1] = bot
                    #     break
                    # elif l[0] == l[2] == e and l[1] == " ":
                    #     l[1] = bot
                    #     break
                    # elif l[0] == l[1] == e and l[2] == " ":
                    #     l[2] = bot
                    #     break
                    # elif l[5] == l[8] == e and l[2] == " ":
                    #     l[2] = bot
                    #     break
                    # elif l[4] == l[6] == e and l[2] == " ":
                    #     l[2] = bot
                    #     break
                    # elif l[0] == l[6] == e and l[3] == " ":
                    #     l[3] = bot
                    #     break
                    # elif l[4] == l[5] == e and l[3] == " ":
                    #     l[3] = bot
                    #     break
                    # elif l[3] == l[5] == e and l[4] == " ":
                    #     l[4] = bot
                    #     break
                    # elif l[1] == l[7] == e and l[4] == " ":
                    #     l[4] = bot
                    #     break
                    # elif l[0] == l[8] == e and l[4] == " ":
                    #     l[4] = bot
                    #     break
                    # elif l[2] == l[8] == e and l[5] == " ":
                    #     l[5] = bot
                    #     break
                    # elif l[3] == l[4] == e and l[5] == " ":
                    #     l[5] = bot
                    #     break
                    # elif l[0] == l[3] == e and l[6] == " ":
                    #     l[6] = bot
                    #     break
                    # elif l[2] == l[4] == e and l[6] == " ":
                    #     l[6] = bot
                    #     break
                    # elif l[7] == l[8] == e and l[6] == " ":
                    #     l[6] = bot
                    #     break
                    # elif l[1] == l[4] == e and l[7] == " ":
                    #     l[7] = bot
                    #     break
                    # elif l[6] == l[8] == e and l[7] == " ":
                    #     l[7] = bot
                    #     break
                    # elif l[0] == l[4] == e and l[8] == " ":
                    #     l[8] = bot
                    #     break
                    # elif l[2] == l[5] == e and l[8] == " ":
                    #     l[8] = bot
                    #     break
                    # elif l[6] == l[7] == e and l[8] == " ":
                    #     l[8] = bot
                    #     break 
                    # elif l[0] == l[5] == e and l[8] == " ":
                    #     l[8] = bot
                    #     break
            else:
                while True:
                    os.system('cls')
                    t()
                    j = input('Digite a posição:')
                    try:
                        j = int(j)
                        if j >= 1 and j <= 9:
                            if l[j-1] == " ":
                                l[j-1] = p
                                break
                            else:
                                z = 'Lugar já ocupado, digite um vazio.'
                                d()
                        else:
                            z = 'Lembre-se, digite um número de 1 a 9.'
                            d()
                    except ValueError:
                        z = 'Vc não digitou um número.'
                        d()
                    


                
            