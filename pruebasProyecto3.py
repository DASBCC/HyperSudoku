import random
resuelto = [[[5,3,4],[6,7,8],[9,1,2]], #resuelto[x]= fila
            [[6,7,2],[1,9,5],[3,4,8]], #resuelto[x][x]= fila, columna
            [[1,9,8],[3,4,2],[5,6,7]], #resuelto[x][x][x]= fila, columna, espacio
            [[8,5,9],[7,6,1],[4,2,3]],
            [[4,2,6],[8,5,3],[7,9,1]],
            [[7,1,3],[9,2,4],[8,5,6]],
            [[9,6,1],[5,3,7],[2,8,4]],
            [[2,8,7],[4,1,9],[6,3,5]],
            [[3,4,5],[2,8,6],[1,7,9]]]

resuelto2 = [[[1,5,6],[2,4,3],[7,8,9]], #resuelto[x]= fila
             [[2,3,4],[7,8,9],[1,5,6]], #resuelto[x][x]= fila, columna
             [[7,8,9],[5,1,6],[2,4,3]], #resuelto[x][x][x]= fila, columna, espacio
             [[9,6,2],[1,5,7],[8,3,4]],
             [[5,4,3],[8,6,2],[9,1,7]],
             [[8,7,1],[3,9,4],[6,2,5]],
             [[4,2,5],[6,7,8],[3,9,1]],
             [[6,9,8],[4,3,1],[5,7,2]],
             [[3,1,7],[9,2,5],[4,6,8]]]

def revisa(lista): #revisa primera fila
    temp = []
    temp.append(lista[0][0][0])
    temp.append(lista[0][0][1])
    temp.append(lista[0][0][2])
    temp.append(lista[0][1][0])
    temp.append(lista[0][1][1])
    temp.append(lista[0][1][2]) 
    temp.append(lista[0][2][0])
    temp.append(lista[0][2][1])
    temp.append(lista[0][2][2])
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa2(lista): #revisa segunda fila
    temp = []
    temp.append(lista[1][0][0])
    temp.append(lista[1][0][1])
    temp.append(lista[1][0][2])
    temp.append(lista[1][1][0])
    temp.append(lista[1][1][1])
    temp.append(lista[1][1][2]) 
    temp.append(lista[1][2][0])
    temp.append(lista[1][2][1])
    temp.append(lista[1][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa3(lista): #revisa tercera fila
    temp = []
    temp.append(lista[2][0][0])
    temp.append(lista[2][0][1])
    temp.append(lista[2][0][2])
    temp.append(lista[2][1][0])
    temp.append(lista[2][1][1])
    temp.append(lista[2][1][2]) 
    temp.append(lista[2][2][0])
    temp.append(lista[2][2][1])
    temp.append(lista[2][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa4(lista): #revisa cuarta fila
    temp = []
    temp.append(lista[3][0][0])
    temp.append(lista[3][0][1])
    temp.append(lista[3][0][2])
    temp.append(lista[3][1][0])
    temp.append(lista[3][1][1])
    temp.append(lista[3][1][2]) 
    temp.append(lista[3][2][0])
    temp.append(lista[3][2][1])
    temp.append(lista[3][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa5(lista): #revisa quinta fila
    temp = []
    temp.append(lista[4][0][0])
    temp.append(lista[4][0][1])
    temp.append(lista[4][0][2])
    temp.append(lista[4][1][0])
    temp.append(lista[4][1][1])
    temp.append(lista[4][1][2]) 
    temp.append(lista[4][2][0])
    temp.append(lista[4][2][1])
    temp.append(lista[4][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa6(lista): #revisa sexta fila
    temp = []
    temp.append(lista[5][0][0])
    temp.append(lista[5][0][1])
    temp.append(lista[5][0][2])
    temp.append(lista[5][1][0])
    temp.append(lista[5][1][1])
    temp.append(lista[5][1][2]) 
    temp.append(lista[5][2][0])
    temp.append(lista[5][2][1])
    temp.append(lista[5][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa7(lista): #revisa septima fila
    temp = []
    temp.append(lista[6][0][0])
    temp.append(lista[6][0][1])
    temp.append(lista[6][0][2])
    temp.append(lista[6][1][0])
    temp.append(lista[6][1][1])
    temp.append(lista[6][1][2]) 
    temp.append(lista[6][2][0])
    temp.append(lista[6][2][1])
    temp.append(lista[6][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa8(lista): #revisa octava fila
    temp = []
    temp.append(lista[7][0][0])
    temp.append(lista[7][0][1])
    temp.append(lista[7][0][2])
    temp.append(lista[7][1][0])
    temp.append(lista[7][1][1])
    temp.append(lista[7][1][2]) 
    temp.append(lista[7][2][0])
    temp.append(lista[7][2][1])
    temp.append(lista[7][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa9(lista): #revisa novena fila
    temp = []
    temp.append(lista[8][0][0])
    temp.append(lista[8][0][1])
    temp.append(lista[8][0][2])
    temp.append(lista[8][1][0])
    temp.append(lista[8][1][1])
    temp.append(lista[8][1][2]) 
    temp.append(lista[8][2][0])
    temp.append(lista[8][2][1])
    temp.append(lista[8][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa10(lista): #revisa primera columna
    temp = []
    temp.append(lista[0][0][0])
    temp.append(lista[1][0][0])
    temp.append(lista[2][0][0])
    temp.append(lista[3][0][0])
    temp.append(lista[4][0][0])
    temp.append(lista[5][0][0])
    temp.append(lista[6][0][0])
    temp.append(lista[7][0][0])
    temp.append(lista[8][0][0])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa11(lista): #revisa segunda columna
    temp = []
    temp.append(lista[0][0][1])
    temp.append(lista[1][0][1])
    temp.append(lista[2][0][1])
    temp.append(lista[3][0][1])
    temp.append(lista[4][0][1])
    temp.append(lista[5][0][1])
    temp.append(lista[6][0][1])
    temp.append(lista[7][0][1])
    temp.append(lista[8][0][1])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa12(lista): #revisa tercera columna
    temp = []
    temp.append(lista[0][0][2])
    temp.append(lista[1][0][2])
    temp.append(lista[2][0][2])
    temp.append(lista[3][0][2])
    temp.append(lista[4][0][2])
    temp.append(lista[5][0][2])
    temp.append(lista[6][0][2])
    temp.append(lista[7][0][2])
    temp.append(lista[8][0][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa13(lista): #revisa cuarta columna
    temp = []
    temp.append(lista[0][1][0])
    temp.append(lista[1][1][0])
    temp.append(lista[2][1][0])
    temp.append(lista[3][1][0])
    temp.append(lista[4][1][0])
    temp.append(lista[5][1][0])
    temp.append(lista[6][1][0])
    temp.append(lista[7][1][0])
    temp.append(lista[8][1][0])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa14(lista): #revisa quinta columna
    temp = []
    temp.append(lista[0][1][1])
    temp.append(lista[1][1][1])
    temp.append(lista[2][1][1])
    temp.append(lista[3][1][1])
    temp.append(lista[4][1][1])
    temp.append(lista[5][1][1])
    temp.append(lista[6][1][1])
    temp.append(lista[7][1][1])
    temp.append(lista[8][1][1])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa15(lista): #revisa sexta columna
    temp = []
    temp.append(lista[0][1][2])
    temp.append(lista[1][1][2])
    temp.append(lista[2][1][2])
    temp.append(lista[3][1][2])
    temp.append(lista[4][1][2])
    temp.append(lista[5][1][2])
    temp.append(lista[6][1][2])
    temp.append(lista[7][1][2])
    temp.append(lista[8][1][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa16(lista): #revisa septima columna
    temp = []
    temp.append(lista[0][2][0])
    temp.append(lista[1][2][0])
    temp.append(lista[2][2][0])
    temp.append(lista[3][2][0])
    temp.append(lista[4][2][0])
    temp.append(lista[5][2][0])
    temp.append(lista[6][2][0])
    temp.append(lista[7][2][0])
    temp.append(lista[8][2][0])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa17(lista): #revisa octava columna
    temp = []
    temp.append(lista[0][2][1])
    temp.append(lista[1][2][1])
    temp.append(lista[2][2][1])
    temp.append(lista[3][2][1])
    temp.append(lista[4][2][1])
    temp.append(lista[5][2][1])
    temp.append(lista[6][2][1])
    temp.append(lista[7][2][1])
    temp.append(lista[8][2][1])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa18(lista): #revisa novena columna
    temp = []
    temp.append(lista[0][2][2])
    temp.append(lista[1][2][2])
    temp.append(lista[2][2][2])
    temp.append(lista[3][2][2])
    temp.append(lista[4][2][2])
    temp.append(lista[5][2][2])
    temp.append(lista[6][2][2])
    temp.append(lista[7][2][2])
    temp.append(lista[8][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa19(lista): #revisa primer area
    temp = []
    temp.append(lista[0][0][0])
    temp.append(lista[0][0][1])
    temp.append(lista[0][0][2])
    temp.append(lista[1][0][0])
    temp.append(lista[1][0][1])
    temp.append(lista[1][0][2])
    temp.append(lista[2][0][0])
    temp.append(lista[2][0][1])
    temp.append(lista[2][0][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa20(lista): #revisa segundo area
    temp = []
    temp.append(lista[0][1][0])
    temp.append(lista[0][1][1])
    temp.append(lista[0][1][2])
    temp.append(lista[1][1][0])
    temp.append(lista[1][1][1])
    temp.append(lista[1][1][2])
    temp.append(lista[2][1][0])
    temp.append(lista[2][1][1])
    temp.append(lista[2][1][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa21(lista): #revisa tercer area
    temp = []
    temp.append(lista[0][2][0])
    temp.append(lista[0][2][1])
    temp.append(lista[0][2][2])
    temp.append(lista[1][2][0])
    temp.append(lista[1][2][1])
    temp.append(lista[1][2][2])
    temp.append(lista[2][2][0])
    temp.append(lista[2][2][1])
    temp.append(lista[2][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa22(lista): #revisa cuarta area
    temp = []
    temp.append(lista[3][0][0])
    temp.append(lista[3][0][1])
    temp.append(lista[3][0][2])
    temp.append(lista[4][0][0])
    temp.append(lista[4][0][1])
    temp.append(lista[4][0][2])
    temp.append(lista[5][0][0])
    temp.append(lista[5][0][1])
    temp.append(lista[5][0][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa23(lista): #revisa quinta area
    temp = []
    temp.append(lista[3][1][0])
    temp.append(lista[3][1][1])
    temp.append(lista[3][1][2])
    temp.append(lista[4][1][0])
    temp.append(lista[4][1][1])
    temp.append(lista[4][1][2])
    temp.append(lista[5][1][0])
    temp.append(lista[5][1][1])
    temp.append(lista[5][1][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa24(lista): #revisa sexta area
    temp = []
    temp.append(lista[3][2][0])
    temp.append(lista[3][2][1])
    temp.append(lista[3][2][2])
    temp.append(lista[4][2][0])
    temp.append(lista[4][2][1])
    temp.append(lista[4][2][2])
    temp.append(lista[5][2][0])
    temp.append(lista[5][2][1])
    temp.append(lista[5][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa25(lista): #revisa septima area
    temp = []
    temp.append(lista[6][0][0])
    temp.append(lista[6][0][1])
    temp.append(lista[6][0][2])
    temp.append(lista[7][0][0])
    temp.append(lista[7][0][1])
    temp.append(lista[7][0][2])
    temp.append(lista[8][0][0])
    temp.append(lista[8][0][1])
    temp.append(lista[8][0][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa26(lista): #revisa octava area
    temp = []
    temp.append(lista[6][1][0])
    temp.append(lista[6][1][1])
    temp.append(lista[6][1][2])
    temp.append(lista[7][1][0])
    temp.append(lista[7][1][1])
    temp.append(lista[7][1][2])
    temp.append(lista[8][1][0])
    temp.append(lista[8][1][1])
    temp.append(lista[8][1][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa27(lista): #revisa novena area
    temp = []
    temp.append(lista[6][2][0])
    temp.append(lista[6][2][1])
    temp.append(lista[6][2][2])
    temp.append(lista[7][2][0])
    temp.append(lista[7][2][1])
    temp.append(lista[7][2][2])
    temp.append(lista[8][2][0])
    temp.append(lista[8][2][1])
    temp.append(lista[8][2][2])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa28(lista): #revisa primer area especial
    temp = []
    temp.append(lista[1][0][1])
    temp.append(lista[1][0][2])
    temp.append(lista[1][1][0])
    temp.append(lista[2][0][1])
    temp.append(lista[2][0][2])
    temp.append(lista[2][1][0])
    temp.append(lista[3][0][1])
    temp.append(lista[3][0][2])
    temp.append(lista[3][1][0])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa29(lista): #revisa segunda area especial
    temp = []
    temp.append(lista[1][1][2])
    temp.append(lista[1][2][0])
    temp.append(lista[1][2][1])
    temp.append(lista[2][1][2])
    temp.append(lista[2][2][0])
    temp.append(lista[2][2][1])
    temp.append(lista[3][1][2])
    temp.append(lista[3][2][0])
    temp.append(lista[3][2][1])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa30(lista): #revisa tercer area especial
    temp = []
    temp.append(lista[5][0][1])
    temp.append(lista[5][0][2])
    temp.append(lista[5][1][0])
    temp.append(lista[6][0][1])
    temp.append(lista[6][0][2])
    temp.append(lista[6][1][0])
    temp.append(lista[7][0][1])
    temp.append(lista[7][0][2])
    temp.append(lista[7][1][0])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False

def revisa31(lista): #revisa cuarta area especialp
    temp = []
    temp.append(lista[5][1][2])
    temp.append(lista[5][2][0])
    temp.append(lista[5][2][1])
    temp.append(lista[6][1][2])
    temp.append(lista[6][2][0])
    temp.append(lista[6][2][1])
    temp.append(lista[7][1][2])
    temp.append(lista[7][2][0])
    temp.append(lista[7][2][1])
    #print(temp)
    if temp.count(1)<=1 and temp.count(2)<=1 and temp.count(3)<=1 and temp.count(4)<=1 and temp.count(5)<=1 and temp.count(6)<=1 and temp.count(7)<=1 and temp.count(8)<=1 and temp.count(9)<=1:
        return True
    else:
        return False
        
def revisarFilas(lista):
    if revisa(lista) == True and revisa2(lista) == True and revisa3(lista) == True and revisa4(lista) == True and revisa5(lista) == True and revisa6(lista) == True and revisa7(lista) == True and revisa8(lista) == True and revisa9(lista) == True:
        return True
    else:
        return False

def revisarColumnas(lista):
    if revisa10(lista) == True and revisa11(lista) == True and revisa12(lista) == True and revisa13(lista) == True and revisa14(lista) == True and revisa15(lista) == True and revisa16(lista) == True and revisa17(lista) == True and revisa18(lista) == True:
        return True
    else:
        return False

def revisarAreas(lista):
    if revisa19(lista) == True and revisa20(lista) == True and revisa21(lista) == True and revisa22(lista) == True and revisa23(lista) == True and revisa24(lista) == True and revisa25(lista) == True and revisa26(lista) == True and revisa27(lista) == True:
        return True
    else:
        return False

def revisarEspeciales(lista):
    if revisa28(lista) == True and revisa29(lista) == True and revisa30(lista) == True and revisa31(lista) == True:
        return True
    else:
        return False

def revisarFinal(lista):
    if revisarAreas(lista) == True and revisarFilas(lista) == True and revisarColumnas(lista) == True and revisarEspeciales(lista) == True:
        return True
    else:
        return False
print(revisarFinal(resuelto2))
cantidad = random.randint(8, 20) 
def generador(cantidad):
    matriz =[[[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]], 
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]],
             [[0,0,0],[0,0,0],[0,0,0]]]
    while cantidad > 0:
        a = random.randint(0, 8)
        b = random.randint(0, 2)
        c = random.randint(0,2)
        num = random.randint(1, 9)
        matriz[a][b][c] = num
        cantidad = cantidad - 1
    if revisarFinal(matriz) == True:
        return matriz
    else:
        cantidad = random.randint(8, 20)
        return generador(cantidad)

#print (generador(cantidad))