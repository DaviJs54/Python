import pygame
import sys
import time
from tkinter import messagebox
pygame.init()
BRANCO = (255, 255, 255)
VERDE = (25, 122, 207)
pb = pygame.image.load("pb.png")
pp = pygame.image.load("pp.png")
tb = pygame.image.load("tb.png")
tp = pygame.image.load("tp.png")
cb = pygame.image.load("cb.png")
cp = pygame.image.load("cp.png")
bb = pygame.image.load("bb.png")
bp = pygame.image.load("bp.png")
rb = pygame.image.load("rb.png")
rp = pygame.image.load("rp.png")
kb = pygame.image.load("kb.png")
kp = pygame.image.load("kp.png")
coordenadas = [[],[],[],[],[],[],[],[]]
peças = [[],[],[],[],[],[],[],[]]
for x in range(8):
    for y in range(8):
        try:
            peças[x].append(" ")
            coordenadas[x].append(" ")
        except IndexError:
            continue
for x in range(8):
    peças[6][x] = pb
    peças[1][x] = pp
peças[0][0] = peças[0][7] = tp
peças[0][1] = peças[0][6] = cp
peças[0][2] = peças[0][5] = bp
peças[0][3] = rp
peças[0][4] = kp
peças[7][0] = peças[7][7] = tb
peças[7][1] = peças[7][6] = cb
peças[7][2] = peças[7][5] = bb
peças[7][3] = rb
peças[7][4] = kb
for x in range(8):
    for y in range(8):
        try:
            coordenadas[y][x] = (60*x,60*y,60,60)
        except IndexError:
            continue
def pt():
    janela = pygame.display.set_mode((480, 480))
    for x in range(8):
        for y in range(8):
            if y in[0,2,4,6]:
                if x in[0,2,4,6]:
                    cor = BRANCO
                else:
                    cor = VERDE
            else:
                if x in[0,2,4,6]:
                    cor = VERDE
                else:
                    cor = BRANCO
            pygame.draw.rect(janela , cor , (x * 60 , y * 60, 60, 60))
pt()
largura, altura = 480, 480
janela = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Chess")
p = 0
a = u = 0
k = 0
d = 0
i = 0
pt()
while True:
    try:
        flag = 0
        for evento in pygame.event.get():
            peças_verificação = []
            for x in range(8):
                for y in range(8):
                    peças_verificação.append(peças[y][x])
            if kb not in peças_verificação:
                pygame.quit()
                messagebox.showinfo("Fim do Jogo" , "Vitória das pretas")
                sys.exit()
            elif kp not in peças_verificação:
                pygame.quit()
                messagebox.showinfo("Fim do Jogo" , "Vitória das brancas")
                sys.exit()
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN or i == 1:
                i = 0
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if evento.button == 1:
                    if p == 0:
                        for u in range(8):
                            if flag == 1:
                                break
                            for a in range(8):
                                quadrado = pygame.Rect(a * 60, u * 60, 60, 60)
                                if quadrado.collidepoint(mouse_x, mouse_y):
                                    pt()
                                    pygame.draw.rect(janela , (255,255,0) , (a * 60 , u * 60 , 60 , 60))
                                    p = 1
                                    coordenada1 = (a * 60 , u * 60 , 60 , 60)
                                    if peças[u][a] == " ":
                                        pt()
                                        p = 0
                                    if d == 0:
                                        if peças[u][a] in [pp,bp,cp,kp,rp,tp]:
                                            pt()
                                            p = 0
                                    else:
                                        if peças[u][a] in [pb,bb,cb,kb,rb,tb]:
                                            pt()
                                            p = 0                     
                                    if d == 0:
                                        if peças[u][a] == pb:
                                            try:
                                                if peças[u-1][a] == " ":
                                                    pygame.draw.rect(janela , (128,128,128) , ((a * 60) + 20 , ((u-1) * 60)+20 , 20 , 20))
                                                if u == 6:    
                                                    if peças[u-2][a] == " " and peças[u-1][a] == " ":
                                                        pygame.draw.rect(janela , (128,128,128) , ((a * 60) + 20 , ((u-2) * 60)+20 , 20 , 20))
                                                if peças[u-1][a-1] in [pp,bp,cp,kp,rp,tp]:
                                                    pygame.draw.rect(janela , (255,0,0) , (((a - 1) * 60), ((u-1) * 60) , 60 , 60))
                                                if peças[u-1][a+1] in [pp,bp,cp,kp,rp,tp]:
                                                    pygame.draw.rect(janela , (255,0,0) , (((a + 1) * 60), ((u-1) * 60) , 60 , 60))
                                            except IndexError:
                                                continue
                                        elif peças[u][a] == cb:
                                            for w in[-2,2]:
                                                for t in[-1,1]:
                                                    try:
                                                        if peças[u+w][a+t] in [pp,bp,cp,kp,rp,tp]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + t) * 60), ((u+w) * 60) , 60 , 60))
                                                        elif peças[u+w][a+t] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + t) * 60) + 20, ((u+w) * 60) + 20 , 20 , 20))
                                                        if peças[u+t][a+w] in [pp,bp,cp,kp,rp,tp]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + w) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + w) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                    except IndexError:
                                                        continue
                                        elif peças[u][a] == kb:
                                            for w in [1,-1]:
                                                for t in [1,-1]:
                                                    try:
                                                        if peças[u+t][a+w] in[pp,rp,kp,tp,bp,cp]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + w) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + w) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                        if peças[u+t][a] in[pp,rp,kp,tp,bp,cp]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                        if peças[u][a+w] in[pp,rp,kp,tp,bp,cp]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a+w) * 60), ((u) * 60) , 60 , 60))
                                                        elif peças[u][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a+w) * 60) + 20, ((u) * 60) + 20 , 20 , 20))
                                                    except IndexError:
                                                        continue
                                        elif peças[u][a] == tb:
                                            v = h = 0 
                                            for o in[1,-1]:
                                                v = h = 0 
                                                for i in range(1,8):
                                                    try:
                                                        if v == 0:    
                                                            if peças[u-i*o][a] in[pp,rp,kp,tp,bp,cp]:
                                                                pygame.draw.rect(janela , (255,0,0) , (((a) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                v = 1
                                                            elif peças[u-i*o][a] == " ":
                                                                pygame.draw.rect(janela , (128,128,128) , (((a) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                            else:
                                                                v = 1
                                                        if h == 0:
                                                            if peças[u][a+i*o] in[pp,rp,kp,tp,bp,cp]:
                                                                pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u) * 60) , 60 , 60))
                                                                h = 1
                                                            elif peças[u][a+i*o] == " ":
                                                                pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u) * 60) + 20 , 20 , 20))
                                                            else:
                                                                h = 1 
                                                    except IndexError:
                                                        continue
                                        elif peças[u][a] == bb:
                                            v = h = 0 
                                            for o in[1,-1]:
                                                for n in[1,-1]:
                                                    v = h = 0 
                                                    for i in range(1,8):
                                                        try:
                                                            if v == 0:    
                                                                if peças[u-i*o][a-i*n] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a - i*n) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                    v = 1
                                                                elif peças[u-i*o][a-i*n] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a - i*n) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    v = 1
                                                            if h == 0:
                                                                if peças[u-i*n][a+i*o] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u-i*n) * 60) , 60 , 60))
                                                                    h = 1
                                                                elif peças[u-i*n][a+i*o] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u-i*n) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    h = 1 
                                                        except IndexError:
                                                            continue
                                        elif peças[u][a] == rb:
                                            v = h = 0 
                                            v2 = h2 = 0
                                            for o in[1,-1]:
                                                v2 = h2 = 0
                                                for n in[1,-1]:
                                                    v = h = 0 
                                                    for i in range(1,8):
                                                        try:
                                                            if v == 0:    
                                                                if peças[u-i*o][a-i*n] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a - i*n) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                    v = 1
                                                                elif peças[u-i*o][a-i*n] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a - i*n) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    v = 1
                                                            if h == 0:
                                                                if peças[u-i*n][a+i*o] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u-i*n) * 60) , 60 , 60))
                                                                    h = 1
                                                                elif peças[u-i*n][a+i*o] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u-i*n) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    h = 1 
                                                            if v2 == 0:    
                                                                if peças[u-i*o][a] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                    v2 = 1
                                                                elif peças[u-i*o][a] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    v2 = 1
                                                            if h2 == 0:
                                                                if peças[u][a+i*o] in[pp,rp,kp,tp,bp,cp]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u) * 60) , 60 , 60))
                                                                    h2 = 1
                                                                elif peças[u][a+i*o] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    h2 = 1
                                                        except IndexError:
                                                            continue
                                    else:
                                        if peças[u][a] == pp:
                                            try:
                                                if peças[u-1][a] == " ":
                                                    pygame.draw.rect(janela , (128,128,128) , ((a * 60) + 20 , ((u-1) * 60)+20 , 20 , 20))
                                                if u == 6:    
                                                    if peças[u-2][a] == " " and peças[u-1][a] == " ":
                                                        pygame.draw.rect(janela , (128,128,128) , ((a * 60) + 20 , ((u-2) * 60)+20 , 20 , 20))
                                                if peças[u-1][a-1] in [pb,bb,cb,kb,rb,tb]:
                                                    pygame.draw.rect(janela , (255,0,0) , (((a - 1) * 60), ((u-1) * 60) , 60 , 60))
                                                if peças[u-1][a+1] in [pb,bb,cb,kb,rb,tb]:
                                                    pygame.draw.rect(janela , (255,0,0) , (((a + 1) * 60), ((u-1) * 60) , 60 , 60))
                                            except IndexError:
                                                continue
                                        elif peças[u][a] == cp:
                                            for w in[-2,2]:
                                                for t in[-1,1]:
                                                    try:
                                                        if peças[u+w][a+t] in [pb,bb,cb,kb,rb,tb]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + t) * 60), ((u+w) * 60) , 60 , 60))
                                                        elif peças[u+w][a+t] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + t) * 60) + 20, ((u+w) * 60) + 20 , 20 , 20))
                                                        if peças[u+t][a+w] in [pb,bb,cb,kb,rb,tb]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + w) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + w) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                    except IndexError:
                                                        continue
                                        elif peças[u][a] == kp:
                                            for w in [1,-1]:
                                                for t in [1,-1]:
                                                    try:
                                                        if peças[u+t][a+w] in[pb,bb,cb,kb,rb,tb]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a + w) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a + w) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                        if peças[u+t][a] in[pb,bb,cb,kb,rb,tb]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a) * 60), ((u+t) * 60) , 60 , 60))
                                                        elif peças[u+t][a] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a) * 60) + 20, ((u+t) * 60) + 20 , 20 , 20))
                                                        if peças[u][a+w] in[pb,bb,cb,kb,rb,tb]:
                                                            pygame.draw.rect(janela , (255,0,0) , (((a+w) * 60), ((u) * 60) , 60 , 60))
                                                        elif peças[u][a+w] == " ":
                                                            pygame.draw.rect(janela , (128,128,128) , (((a+w) * 60) + 20, ((u) * 60) + 20 , 20 , 20))
                                                    except IndexError:
                                                        continue
                                        elif peças[u][a] == tp:
                                            v = h = 0 
                                            for o in[1,-1]:
                                                v = h = 0 
                                                for i in range(1,8):
                                                    try:
                                                        if v == 0:    
                                                            if peças[u-i*o][a] in[pb,rb,kb,tb,bb,cb]:
                                                                pygame.draw.rect(janela , (255,0,0) , (((a) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                v = 1
                                                            elif peças[u-i*o][a] == " ":
                                                                pygame.draw.rect(janela , (128,128,128) , (((a) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                            else:
                                                                v = 1
                                                        if h == 0:
                                                            if peças[u][a+i*o] in[pb,rb,kb,tb,bb,cb]:
                                                                pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u) * 60) , 60 , 60))
                                                                h = 1
                                                            elif peças[u][a+i*o] == " ":
                                                                pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u) * 60) + 20 , 20 , 20))
                                                            else:
                                                                h = 1 
                                                    except IndexError:
                                                        continue  
                                        elif peças[u][a] == bp:
                                            v = h = 0 
                                            for o in[1,-1]:
                                                for n in[1,-1]:
                                                    v = h = 0 
                                                    for i in range(1,8):
                                                        try:
                                                            if v == 0:    
                                                                if peças[u-i*o][a-i*n] in[pb,rb,kb,tb,bb,cb]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a - i*n) * 60), ((u - i*o) * 60) , 60 , 60))
                                                                    v = 1
                                                                elif peças[u-i*o][a-i*n] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a - i*n) * 60) + 20, ((u - i*o) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    v = 1
                                                            if h == 0:
                                                                if peças[u-i*n][a+i*o] in[pb,rb,kb,tb,bb,cb]:
                                                                    pygame.draw.rect(janela , (255,0,0) , (((a + i*o) * 60), ((u-i*n) * 60) , 60 , 60))
                                                                    h = 1
                                                                elif peças[u-i*n][a+i*o] == " ":
                                                                    pygame.draw.rect(janela , (128,128,128) , (((a+i*o) * 60) + 20, ((u-i*n) * 60) + 20 , 20 , 20))
                                                                else:
                                                                    h = 1 
                                                        except IndexError:
                                                            continue    

                    else:
                        for x in range(8):
                            for y in range(8):
                                if flag == 1:
                                    break
                                quadrado1 = pygame.Rect(x * 60, y * 60, 60, 60)
                                if quadrado1.collidepoint(mouse_x, mouse_y):
                                    coordenada2 = (x * 60, y * 60, 60, 60)
                                    if flag == 1:
                                        break
                                    if coordenada1 == coordenada2:
                                        pt()
                                        coordenada2 = None
                                        coordenada1 = None
                                        p = 0
                                        break
                                    if d == 0:
                                        if peças[y][x] in [pb,rb,kb,tb,bb,cb]:
                                            pt()
                                            coordenada1 = coordenada2
                                            i = 1
                                            #pygame.draw.rect(janela , (255,255,0) , coordenada1)
                                            p = 0
                                            break
                                    else:
                                        if peças[y][x] in [pp,rp,kp,tp,bp,cp]:
                                            pt()
                                            coordenada1 = coordenada2
                                            i = 1
                                            p = 0
                                            break
                                    for x in range(8):
                                        for y in range(8):
                                            if coordenadas[y][x] == coordenada1:    
                                                if d == 0:
                                                    if peças[y][x] == pb:
                                                        if y == 6:
                                                            if (x * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " ":
                                                                peças[y-1][x] = pb
                                                                peças[y][x] = " "
                                                                k = 1
                                                            if (x * 60 , (y-2) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " " and peças[y-2][x] == " ":
                                                                peças[y-2][x] = pb
                                                                peças[y][x] = " "
                                                                k = 1
                                                            elif ((x-1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x-1] in[pp,rp,kp,tp,bp,cp]:
                                                                peças[y-1][x-1] = pb
                                                                peças[y][x] = " "
                                                                k = 1
                                                            elif ((x+1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x+1] in[pp,rp,kp,tp,bp,cp]:
                                                                peças[y-1][x+1] = pb
                                                                peças[y][x] = " "
                                                                k = 1
                                                        elif (x * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " ":
                                                            peças[y-1][x] = pb
                                                            peças[y][x] = " "
                                                            k = 1
                                                        elif ((x-1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x-1] in[pp,rp,kp,tp,bp,cp]:
                                                            peças[y-1][x-1] = pb
                                                            peças[y][x] = " "
                                                            k = 1
                                                        elif ((x+1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x+1] in[pp,rp,kp,tp,bp,cp]:
                                                            peças[y-1][x+1] = pb
                                                            peças[y][x] = " "
                                                            k = 1
                                                    elif peças[y][x] == cb:
                                                        for c in [1 , -1]:
                                                            for z in [2 , -2]:
                                                                if ((x+z) * 60 , (y+c) * 60 , 60 , 60) == coordenada2 and peças[y+c][x+z] in[pp,rp,kp,tp,bp,cp," "]:
                                                                    peças[y+c][x+z] = cb
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif ((x+c) * 60 , (y+z) * 60 , 60 , 60) == coordenada2 and peças[y+z][x+c] in[pp,rp,kp,tp,bp,cp," "]:                                             
                                                                    peças[y+z][x+c] = cb
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                    elif peças[y][x] == tb:
                                                        for i in range(8):
                                                            for o in[1 , -1]:
                                                                try:
                                                                    if ((x-(i*o)) * 60,y * 60,60,60)  == coordenada2 and peças[y][x-(i*o)] in[pp,rp,kp,tp,bp,cp," "]:
                                                                        a = peças[y][x-(i*o)]
                                                                        peças[y][x-(i*o)] = tb
                                                                        peças[y][x] = " "
                                                                        k = 1
                                                                        for u in range(i):
                                                                            if peças[y][x-(u*o)] != " ":
                                                                                peças[y][x-(i*o)] = a
                                                                                peças[y][x] = tb
                                                                                k = 0
                                                                    elif (x * 60,(y-(i*o)) * 60,60,60)  == coordenada2 and peças[y-(i*o)][x] in[pp,rp,kp,tp,bp,cp," "]:
                                                                        a = peças[y-(i*o)][x]
                                                                        peças[y-(i*o)][x] = tb
                                                                        peças[y][x] = " "
                                                                        k = 1
                                                                        for u in range(i):
                                                                            if peças[y-(u*o)][x] != " ":
                                                                                peças[y-(i*o)][x] = a
                                                                                peças[y][x] = tb
                                                                                k = 0
                                                                except IndexError:
                                                                    continue
                                                    elif peças[y][x] == kb:
                                                        for w in [1,-1]:
                                                            for t in [-1,1]:
                                                                if coordenada2 == ((x+w) * 60 , (y+t) * 60 , 60 , 60) and peças[y+t][x+w] in[pp,rp,kp,tp,bp,cp," "]:
                                                                    peças[y+t][x+w] = kb
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif coordenada2 == ((x) * 60 , (y+t) * 60 , 60 , 60) and peças[y+t][x] in[pp,rp,kp,tp,bp,cp," "]:
                                                                    peças[y+t][x] = kb
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif coordenada2 == ((x+w) * 60 , (y) * 60 , 60 , 60) and peças[y][x+w] in[pp,rp,kp,tp,bp,cp," "]:
                                                                    peças[y][x+w] = kb
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                    elif peças[y][x] == bb:
                                                        for i in range(8):
                                                            for u in[1 , -1]:
                                                                for z in[1 , -1]:
                                                                    try:
                                                                        if ((x+(i*u)) * 60, (y+(i*z)) * 60 , 60 , 60) == coordenada2 and peças[y+(i*z)][x+(i*u)] in[pp,rp,kp,tp,bp,cp, " "]:
                                                                            a = peças[y+(i*z)][x+(i*u)]
                                                                            peças[y+(i*z)][x+(i*u)] = bb
                                                                            peças[y][x] = " "
                                                                            k = 1
                                                                            for r in range(i):
                                                                                if peças[y+(r*z)][x+(r*u)] != " ":
                                                                                    peças[y+(i*z)][x+(i*u)] = a
                                                                                    peças[y][x] = bb
                                                                                    k = 0
                                                                    except IndexError:
                                                                        continue
                                                    elif peças[y][x] == rb:
                                                        for i in range(8):
                                                            for o in[1 , -1]:
                                                                for u in[1 , -1]:
                                                                    for z in[1 , -1]:
                                                                        try:
                                                                            if ((x-(i*o)) * 60,y * 60,60,60)  == coordenada2 and peças[y][x-(i*o)] in[pp,rp,kp,tp,bp,cp," "]:
                                                                                a = peças[y][x-(i*o)]
                                                                                peças[y][x-(i*o)] = rb
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for u in range(i):
                                                                                    if peças[y][x-(u*o)] != " ":
                                                                                        peças[y][x-(i*o)] = a
                                                                                        peças[y][x] = rb
                                                                                        k = 0
                                                                            elif (x * 60,(y-(i*o)) * 60,60,60)  == coordenada2 and peças[y-(i*o)][x] in[pp,rp,kp,tp,bp,cp," "]:
                                                                                a = peças[y-(i*o)][x]
                                                                                peças[y-(i*o)][x] = rb
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for u in range(i):
                                                                                    if peças[y-(u*o)][x] != " ":
                                                                                        peças[y-(i*o)][x] = a
                                                                                        peças[y][x] = rb
                                                                                        k = 0
                                                                            if ((x+(i*u)) * 60, (y+(i*z)) * 60 , 60 , 60) == coordenada2 and peças[y+(i*z)][x+(i*u)] in[pp,rp,kp,tp,bp,cp, " "]:
                                                                                a = peças[y+(i*z)][x+(i*u)]
                                                                                peças[y+(i*z)][x+(i*u)] = rb
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for r in range(i):
                                                                                    if peças[y+(r*z)][x+(r*u)] != " ":
                                                                                        peças[y+(i*z)][x+(i*u)] = a
                                                                                        peças[y][x] = rb
                                                                                        k = 0
                                                                        except IndexError:
                                                                            continue

                                                else:
                                                    if peças[y][x] == pp:
                                                        if y == 6:
                                                            if (x * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " ":
                                                                peças[y-1][x] = pp
                                                                peças[y][x] = " "
                                                                k = 1
                                                            if (x * 60 , (y-2) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " " and peças[y-2][x] == " ":
                                                                peças[y-2][x] = pp
                                                                peças[y][x] = " "
                                                                k = 1
                                                            elif ((x-1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x-1] in[pb,rb,kb,tb,bb,cb]:
                                                                peças[y-1][x-1] = pp
                                                                peças[y][x] = " "
                                                                k = 1
                                                            elif ((x+1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x+1] in[pb,rb,kb,tb,bb,cb]:
                                                                peças[y-1][x+1] = pp
                                                                peças[y][x] = " "
                                                                k = 1
                                                        elif (x * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x] == " ":
                                                            peças[y-1][x] = pp
                                                            peças[y][x] = " "
                                                            k = 1
                                                        elif ((x-1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x-1] in[pb,rb,kb,tb,bb,cb]:
                                                            peças[y-1][x-1] = pp
                                                            peças[y][x] = " "
                                                            k = 1
                                                        elif ((x+1) * 60 , (y-1) * 60 , 60 , 60) == coordenada2 and peças[y-1][x+1] in[pb,rb,kb,tb,bb,cb]:
                                                            peças[y-1][x+1] = pp
                                                            peças[y][x] = " "
                                                            k = 1
                                                    elif peças[y][x] == cp:
                                                        for c in [1 , -1]:
                                                            for z in [2 , -2]:
                                                                if ((x+z) * 60 , (y+c) * 60 , 60 , 60) == coordenada2 and peças[y+c][x+z] in[pb,rb,kb,tb,bb,cb," "]:
                                                                    peças[y+c][x+z] = cp
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif ((x+c) * 60 , (y+z) * 60 , 60 , 60) == coordenada2 and peças[y+z][x+c] in[pb,rb,kb,tb,bb,cb," "]:                                             
                                                                    peças[y+z][x+c] = cp
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                    elif peças[y][x] == tp:
                                                        for i in range(8):
                                                            for o in[1 , -1]:
                                                                try:
                                                                    if ((x-(i*o)) * 60,y * 60,60,60)  == coordenada2 and peças[y][x-(i*o)] in[pb,rb,kb,tb,bb,cb," "]:
                                                                        a = peças[y][x-(i*o)]
                                                                        peças[y][x-(i*o)] = tp
                                                                        peças[y][x] = " "
                                                                        k = 1
                                                                        for u in range(i):
                                                                            if peças[y][x-(u*o)] != " ":
                                                                                peças[y][x-(i*o)] = a
                                                                                peças[y][x] = tp
                                                                                k = 0
                                                                    elif (x * 60,(y-(i*o)) * 60,60,60)  == coordenada2 and peças[y-(i*o)][x] in[pb,rb,kb,tb,bb,cb," "]:
                                                                        a = peças[y-(i*o)][x]
                                                                        peças[y-(i*o)][x] = tp
                                                                        peças[y][x] = " "
                                                                        k = 1
                                                                        for u in range(i):
                                                                            if peças[y-(u*o)][x] != " ":
                                                                                peças[y-(i*o)][x] = a
                                                                                peças[y][x] = tp
                                                                                k = 0
                                                                except IndexError:
                                                                    continue
                                                    elif peças[y][x] == kp:
                                                        for w in [1,-1]:
                                                            for t in [-1,1]:
                                                                if coordenada2 == ((x+w) * 60 , (y+t) * 60 , 60 , 60) and peças[y+t][x+w] in[pb,rb,kb,tb,bb,cb," "]:
                                                                    peças[y+t][x+w] = kp
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif coordenada2 == ((x) * 60 , (y+t) * 60 , 60 , 60) and peças[y+t][x] in[pb,rb,kb,tb,bb,cb," "]:
                                                                    peças[y+t][x] = kp
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                                elif coordenada2 == ((x+w) * 60 , (y) * 60 , 60 , 60) and peças[y][x+w] in[pb,rb,kb,tb,bb,cb," "]:
                                                                    peças[y][x+w] = kp
                                                                    peças[y][x] = " "
                                                                    k = 1
                                                    elif peças[y][x] == bp:
                                                        for i in range(8):
                                                            for u in[1 , -1]:
                                                                for z in[1 , -1]:
                                                                    try:
                                                                        if ((x+(i*u)) * 60, (y+(i*z)) * 60 , 60 , 60) == coordenada2 and peças[y+(i*z)][x+(i*u)] in[pb,rb,kb,tb,bb,cb, " "]:
                                                                            a = peças[y+(i*z)][x+(i*u)]
                                                                            peças[y+(i*z)][x+(i*u)] = bp
                                                                            peças[y][x] = " "
                                                                            k = 1
                                                                            for r in range(i):
                                                                                if peças[y+(r*z)][x+(r*u)] != " ":
                                                                                    peças[y+(i*z)][x+(i*u)] = a
                                                                                    peças[y][x] = bp
                                                                                    k = 0
                                                                    except IndexError:
                                                                        continue
                                                    elif peças[y][x] == rp:
                                                        for i in range(8):
                                                            for o in[1 , -1]:
                                                                for u in[1 , -1]:
                                                                    for z in[1 , -1]:
                                                                        try:
                                                                            if ((x-(i*o)) * 60,y * 60,60,60)  == coordenada2 and peças[y][x-(i*o)] in[pb,rb,kb,tb,bb,cb," "]:
                                                                                a = peças[y][x-(i*o)]
                                                                                peças[y][x-(i*o)] = rp
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for u in range(i):
                                                                                    if peças[y][x-(u*o)] != " ":
                                                                                        peças[y][x-(i*o)] = a
                                                                                        peças[y][x] = rp
                                                                                        k = 0
                                                                            elif (x * 60,(y-(i*o)) * 60,60,60)  == coordenada2 and peças[y-(i*o)][x] in[pb,rb,kb,tb,bb,cb," "]:
                                                                                a = peças[y-(i*o)][x]
                                                                                peças[y-(i*o)][x] = rp
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for u in range(i):
                                                                                    if peças[y-(u*o)][x] != " ":
                                                                                        peças[y-(i*o)][x] = a
                                                                                        peças[y][x] = rp
                                                                                        k = 0
                                                                            if ((x+(i*u)) * 60, (y+(i*z)) * 60 , 60 , 60) == coordenada2 and peças[y+(i*z)][x+(i*u)] in[pb,rb,kb,tb,bb,cb, " "]:
                                                                                a = peças[y+(i*z)][x+(i*u)]
                                                                                peças[y+(i*z)][x+(i*u)] = rp
                                                                                peças[y][x] = " "
                                                                                k = 1
                                                                                for r in range(i):
                                                                                    if peças[y+(r*z)][x+(r*u)] != " ":
                                                                                        peças[y+(i*z)][x+(i*u)] = a
                                                                                        peças[y][x] = rp
                                                                                        k = 0
                                                                        except IndexError:
                                                                            continue
                                    p = 0
                                    pygame.time.delay(700)
                                    pt()                                                        
        if k == 1:
            k = 0
            d = 1 if d == 0 else 0
            for x in range(8):
                for y in range(4):
                    peças[y][x], peças[7-y][x] = peças[7-y][x], peças[y][x]
            
        for x in range(8):
            for y in range(8):
                try:
                    if peças[y][x] != " ":
                        janela.blit(peças[y][x], coordenadas[y][x])
                except IndexError:
                    continue
        pygame.display.update()
    except AttributeError:
        continue