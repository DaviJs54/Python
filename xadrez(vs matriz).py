l = [[],[],[],[],[],[],[],[]]
for c in range(8):
    for x in range(8):
        l[c].append(" ")
for x in range(0,8):
    l[1][x] = "♙"
    l[6][x] = "♟"
l[0][0] , l[0][7] = "♖" , "♖"
l[7][0] , l[7][7] = "♜" , "♜"
l[0][1] , l[0],[6] = ""

def t():
    print("┌───┬───┬───┬───┬───┬───┬───┬───┐")
    for x in range(8):
        linha = "│"
        for c in range(8):
            linha += " " + l[x][c]+" │"
        print(linha)
        if x != 7:
            print("├───┼───┼───┼───┼───┼───┼───┼───┤")
    print("└───┴───┴───┴───┴───┴───┴───┴───┘")
t()
    



        
        
