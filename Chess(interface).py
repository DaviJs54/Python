import pygame
import sys
import time
from tkinter import messagebox
pygame.init()
BRANCO = (255, 255, 255)
VERDE = (0, 128, 0)
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
pc = []
cd = []
def pt():
    i = []
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
            pygame.draw.rect(janela , cor , (x * 60 , y * 60 , 60 , 60))
pt()
largura, altura = 480, 480
janela = pygame.display.set_mode((480, 480))
pygame.display.set_caption("Chess")
i = []
i = [""] * 64
p = 0
pc.append(rb)
cd.append((60*3 , 60 * 7 , 60 , 60))
pc.append(rp)
cd.append((60*3 , 0 , 60 , 60))
for z in range(8):
    pc.append(pb)
    cd.append((z * 60, 6 * 60 , 60 , 60))
    pc.append(pp)
    cd.append((z * 60, 60 , 60 , 60))
for z in[0,7]:
    pc.append(tb)
    cd.append((z * 60, 60 * 7, 60 , 60))
    pc.append(tp)
    cd.append((z * 60, 0 , 60 , 60))
for z in[1,6]:
    pc.append(cb)
    cd.append((z * 60, 60 * 7, 60 , 60))
    pc.append(cp)
    cd.append((z * 60, 0 , 60 , 60))
for z in[2,5]:
    pc.append(bb)
    cd.append((z * 60, 60 * 7, 60 , 60))
    pc.append(bp)
    cd.append((z * 60, 0 , 60 , 60))
pc.append(kb)
cd.append((60*4 , 60 * 7 , 60 , 60))
pc.append(kp)
cd.append((60*4 , 0 , 60 , 60))
a = u = 0
k = 0
d = 0
pt()
while True:
    flag = 0
    for evento in pygame.event.get():
        if kb not in pc:
            pygame.quit()
            messagebox.showinfo("Fim do Jogo" , "Vitória das pretas")
            sys.exit()
        elif kp not in pc:
            pygame.quit()
            messagebox.showinfo("Fim do Jogo" , "Vitória das brancas")
            sys.exit()
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
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
                                if coordenada1 not in cd:
                                    pt()
                                    p = 0
                else:
                    for x in range(8):
                        for y in range(8):
                            quadrado1 = pygame.Rect(x * 60, y * 60, 60, 60)
                            if quadrado1.collidepoint(mouse_x, mouse_y):
                                coordenada2 = (x * 60, y * 60, 60, 60)
                                for z in range(64):
                                    try:
                                        if coordenada1 == coordenada2:
                                            for x in range(8):
                                                for y in range(8):
                                                    if coordenada2 == (x * 60, y * 60, 60, 60):
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
                                                        pygame.draw.rect(janela , cor , (x * 60 , y * 60 , 60 , 60))
                                            coordenada2 = None
                                            coordenada1 = None
                                            p = 0
                                        if coordenada2 == cd[z]:
                                            pc.pop(z)
                                            cd.pop(z)
                                        if coordenada1 == cd[z]:
                                            cd[z] = coordenada2
                                            k = 1
                                            p = 0
                                            time.sleep(0.7)
                                            pt()
                                    except IndexError:
                                        continue
    

    if k == 1:
        k = 0
        d = 1 if d == 0 else 0
        for z in range(len(pc)):
            flag = 0
            for x in range(8):
                if flag == 1:
                    break
                for y in range(8):
                    if (60 * x,60 * y, 60 , 60) == cd[z]:
                        cd[z] = (60 * (7-x),60 * (7-y), 60 , 60)
                        flag = 1

    for x in range(len(pc)):
        janela.blit(pc[x] , cd[x])
    pygame.display.update()


