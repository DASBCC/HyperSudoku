import pygame
from Configuracion import *

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
        
def funcion00(matriz):
    if matriz[0][0][0] == 9:
        matriz[0][0][0] = 1
    else:
        matriz[0][0][0] = matriz[0][0][0] + 1

def funcion01(matriz):
    if matriz[0][0][1] == 9:
        matriz[0][0][1] = 1
    else:
        matriz[0][0][1] = matriz[0][0][1] + 1

def funcion02(matriz):
    if matriz[0][0][2] == 9:
        matriz[0][0][2] = 1
    else:
        matriz[0][0][2] = matriz[0][0][2] + 1

def funcion03(matriz):
    if matriz[0][1][0] == 9:
        matriz[0][1][0] = 1
    else:
        matriz[0][1][0] = matriz[0][1][0] + 1

def funcion04(matriz):
    if matriz[0][1][1] == 9:
        matriz[0][1][1] = 1
    else:
        matriz[0][1][1] = matriz[0][1][1] + 1

def funcion05(matriz):
    if matriz[0][1][2] == 9:
        matriz[0][1][2] = 1
    else:
        matriz[0][1][2] = matriz[0][1][2] + 1        

def funcion06(matriz):
    if matriz[0][2][0] == 9:
        matriz[0][2][0] = 1
    else:
        matriz[0][2][0] = matriz[0][2][0] + 1

def funcion07(matriz):
    if matriz[0][2][1] == 9:
        matriz[0][2][1] = 1
    else:
        matriz[0][2][1] = matriz[0][2][1] + 1

def funcion08(matriz):
    if matriz[0][2][2] == 9:
        matriz[0][2][2] = 1
    else:
        matriz[0][2][2] = matriz[0][2][2] + 1

def funcion09(matriz):
    if matriz[1][0][0] == 9:
        matriz[1][0][0] = 1
    else:
        matriz[1][0][0] = matriz[1][0][0] + 1

def funcion10(matriz):
    if matriz[1][0][1] == 9:
        matriz[1][0][1] = 1
    else:
        matriz[1][0][1] = matriz[1][0][1] + 1

def funcion11(matriz):
    if matriz[1][0][2] == 9:
        matriz[1][0][2] = 1
    else:
        matriz[1][0][2] = matriz[1][0][2] + 1

def funcion12(matriz):
    if matriz[1][1][0] == 9:
        matriz[1][1][0] = 1
    else:
        matriz[1][1][0] = matriz[1][1][0] + 1

def funcion13(matriz):
    if matriz[1][1][1] == 9:
        matriz[1][1][1] = 1
    else:
        matriz[1][1][1] = matriz[1][1][1] + 1

def funcion14(matriz):
    if matriz[1][1][2] == 9:
        matriz[1][1][2] = 1
    else:
        matriz[1][1][2] = matriz[1][1][2] + 1        

def funcion15(matriz):
    if matriz[1][2][0] == 9:
        matriz[1][2][0] = 1
    else:
        matriz[1][2][0] = matriz[1][2][0] + 1

def funcion16(matriz):
    if matriz[1][2][1] == 9:
        matriz[1][2][1] = 1
    else:
        matriz[1][2][1] = matriz[1][2][1] + 1

def funcion17(matriz):
    if matriz[1][2][2] == 9:
        matriz[1][2][2] = 1
    else:
        matriz[1][2][2] = matriz[1][2][2] + 1

def funcion18(matriz):
    if matriz[2][0][0] == 9:
        matriz[2][0][0] = 1
    else:
        matriz[2][0][0] = matriz[2][0][0] + 1

def funcion19(matriz):
    if matriz[2][0][1] == 9:
        matriz[2][0][1] = 1
    else:
        matriz[2][0][1] = matriz[2][0][1] + 1

def funcion20(matriz):
    if matriz[2][0][2] == 9:
        matriz[2][0][2] = 1
    else:
        matriz[2][0][2] = matriz[2][0][2] + 1

def funcion21(matriz):
    if matriz[2][1][0] == 9:
        matriz[2][1][0] = 1
    else:
        matriz[2][1][0] = matriz[2][1][0] + 1

def funcion22(matriz):
    if matriz[2][1][1] == 9:
        matriz[2][1][1] = 1
    else:
        matriz[2][1][1] = matriz[2][1][1] + 1

def funcion23(matriz):
    if matriz[2][1][2] == 9:
        matriz[2][1][2] = 1
    else:
        matriz[2][1][2] = matriz[2][1][2] + 1        

def funcion24(matriz):
    if matriz[2][2][0] == 9:
        matriz[2][2][0] = 1
    else:
        matriz[2][2][0] = matriz[2][2][0] + 1

def funcion25(matriz):
    if matriz[2][2][1] == 9:
        matriz[2][2][1] = 1
    else:
        matriz[2][2][1] = matriz[2][2][1] + 1

def funcion26(matriz):
    if matriz[2][2][2] == 9:
        matriz[2][2][2] = 1
    else:
        matriz[2][2][2] = matriz[2][2][2] + 1

def funcion27(matriz):
    if matriz[3][0][0] == 9:
        matriz[3][0][0] = 1
    else:
        matriz[3][0][0] = matriz[3][0][0] + 1

def funcion28(matriz):
    if matriz[3][0][1] == 9:
        matriz[3][0][1] = 1
    else:
        matriz[3][0][1] = matriz[3][0][1] + 1

def funcion29(matriz):
    if matriz[3][0][2] == 9:
        matriz[3][0][2] = 1
    else:
        matriz[3][0][2] = matriz[3][0][2] + 1

def funcion30(matriz):
    if matriz[3][1][0] == 9:
        matriz[3][1][0] = 1
    else:
        matriz[3][1][0] = matriz[3][1][0] + 1

def funcion31(matriz):
    if matriz[3][1][1] == 9:
        matriz[3][1][1] = 1
    else:
        matriz[3][1][1] = matriz[3][1][1] + 1

def funcion32(matriz):
    if matriz[3][1][2] == 9:
        matriz[3][1][2] = 1
    else:
        matriz[3][1][2] = matriz[3][1][2] + 1        

def funcion33(matriz):
    if matriz[3][2][0] == 9:
        matriz[3][2][0] = 1
    else:
        matriz[3][2][0] = matriz[3][2][0] + 1

def funcion34(matriz):
    if matriz[3][2][1] == 9:
        matriz[3][2][1] = 1
    else:
        matriz[3][2][1] = matriz[3][2][1] + 1

def funcion35(matriz):
    if matriz[3][2][2] == 9:
        matriz[3][2][2] = 1
    else:
        matriz[3][2][2] = matriz[3][2][2] + 1

def funcion36(matriz):
    if matriz[4][0][0] == 9:
        matriz[4][0][0] = 1
    else:
        matriz[4][0][0] = matriz[4][0][0] + 1

def funcion37(matriz):
    if matriz[4][0][1] == 9:
        matriz[4][0][1] = 1
    else:
        matriz[4][0][1] = matriz[4][0][1] + 1

def funcion38(matriz):
    if matriz[4][0][2] == 9:
        matriz[4][0][2] = 1
    else:
        matriz[4][0][2] = matriz[4][0][2] + 1

def funcion39(matriz):
    if matriz[4][1][0] == 9:
        matriz[4][1][0] = 1
    else:
        matriz[4][1][0] = matriz[4][1][0] + 1

def funcion40(matriz):
    if matriz[4][1][1] == 9:
        matriz[4][1][1] = 1
    else:
        matriz[4][1][1] = matriz[4][1][1] + 1

def funcion41(matriz):
    if matriz[4][1][2] == 9:
        matriz[4][1][2] = 1
    else:
        matriz[4][1][2] = matriz[4][1][2] + 1        

def funcion42(matriz):
    if matriz[4][2][0] == 9:
        matriz[4][2][0] = 1
    else:
        matriz[4][2][0] = matriz[4][2][0] + 1

def funcion43(matriz):
    if matriz[4][2][1] == 9:
        matriz[4][2][1] = 1
    else:
        matriz[4][2][1] = matriz[4][2][1] + 1

def funcion44(matriz):
    if matriz[4][2][2] == 9:
        matriz[4][2][2] = 1
    else:
        matriz[4][2][2] = matriz[4][2][2] + 1

def funcion45(matriz):
    if matriz[5][0][0] == 9:
        matriz[5][0][0] = 1
    else:
        matriz[5][0][0] = matriz[5][0][0] + 1

def funcion46(matriz):
    if matriz[5][0][1] == 9:
        matriz[5][0][1] = 1
    else:
        matriz[5][0][1] = matriz[5][0][1] + 1

def funcion47(matriz):
    if matriz[5][0][2] == 9:
        matriz[5][0][2] = 1
    else:
        matriz[5][0][2] = matriz[5][0][2] + 1

def funcion48(matriz):
    if matriz[5][1][0] == 9:
        matriz[5][1][0] = 1
    else:
        matriz[5][1][0] = matriz[5][1][0] + 1

def funcion49(matriz):
    if matriz[5][1][1] == 9:
        matriz[5][1][1] = 1
    else:
        matriz[5][1][1] = matriz[5][1][1] + 1

def funcion50(matriz):
    if matriz[5][1][2] == 9:
        matriz[5][1][2] = 1
    else:
        matriz[5][1][2] = matriz[5][1][2] + 1        

def funcion51(matriz):
    if matriz[5][2][0] == 9:
        matriz[5][2][0] = 1
    else:
        matriz[5][2][0] = matriz[5][2][0] + 1

def funcion52(matriz):
    if matriz[5][2][1] == 9:
        matriz[5][2][1] = 1
    else:
        matriz[5][2][1] = matriz[5][2][1] + 1

def funcion53(matriz):
    if matriz[5][2][2] == 9:
        matriz[5][2][2] = 1
    else:
        matriz[5][2][2] = matriz[5][2][2] + 1

def funcion54(matriz):
    if matriz[6][0][0] == 9:
        matriz[6][0][0] = 1
    else:
        matriz[6][0][0] = matriz[6][0][0] + 1

def funcion55(matriz):
    if matriz[6][0][1] == 9:
        matriz[6][0][1] = 1
    else:
        matriz[6][0][1] = matriz[6][0][1] + 1

def funcion56(matriz):
    if matriz[6][0][2] == 9:
        matriz[6][0][2] = 1
    else:
        matriz[6][0][2] = matriz[6][0][2] + 1

def funcion57(matriz):
    if matriz[6][1][0] == 9:
        matriz[6][1][0] = 1
    else:
        matriz[6][1][0] = matriz[6][1][0] + 1

def funcion58(matriz):
    if matriz[6][1][1] == 9:
        matriz[6][1][1] = 1
    else:
        matriz[6][1][1] = matriz[6][1][1] + 1

def funcion59(matriz):
    if matriz[6][1][2] == 9:
        matriz[6][1][2] = 1
    else:
        matriz[6][1][2] = matriz[6][1][2] + 1        

def funcion60(matriz):
    if matriz[6][2][0] == 9:
        matriz[6][2][0] = 1
    else:
        matriz[6][2][0] = matriz[6][2][0] + 1

def funcion61(matriz):
    if matriz[6][2][1] == 9:
        matriz[6][2][1] = 1
    else:
        matriz[6][2][1] = matriz[6][2][1] + 1

def funcion62(matriz):
    if matriz[6][2][2] == 9:
        matriz[6][2][2] = 1
    else:
        matriz[6][2][2] = matriz[6][2][2] + 1

def funcion63(matriz):
    if matriz[7][0][0] == 9:
        matriz[7][0][0] = 1
    else:
        matriz[7][0][0] = matriz[7][0][0] + 1

def funcion64(matriz):
    if matriz[7][0][1] == 9:
        matriz[7][0][1] = 1
    else:
        matriz[7][0][1] = matriz[7][0][1] + 1

def funcion65(matriz):
    if matriz[7][0][2] == 9:
        matriz[7][0][2] = 1
    else:
        matriz[7][0][2] = matriz[7][0][2] + 1

def funcion66(matriz):
    if matriz[7][1][0] == 9:
        matriz[7][1][0] = 1
    else:
        matriz[7][1][0] = matriz[7][1][0] + 1

def funcion67(matriz):
    if matriz[7][1][1] == 9:
        matriz[7][1][1] = 1
    else:
        matriz[7][1][1] = matriz[7][1][1] + 1

def funcion68(matriz):
    if matriz[7][1][2] == 9:
        matriz[7][1][2] = 1
    else:
        matriz[7][1][2] = matriz[7][1][2] + 1        

def funcion69(matriz):
    if matriz[7][2][0] == 9:
        matriz[7][2][0] = 1
    else:
        matriz[7][2][0] = matriz[7][2][0] + 1

def funcion70(matriz):
    if matriz[7][2][1] == 9:
        matriz[7][2][1] = 1
    else:
        matriz[7][2][1] = matriz[7][2][1] + 1

def funcion71(matriz):
    if matriz[7][2][2] == 9:
        matriz[7][2][2] = 1
    else:
        matriz[7][2][2] = matriz[7][2][2] + 1

def funcion72(matriz):
    if matriz[8][0][0] == 9:
        matriz[8][0][0] = 1
    else:
        matriz[8][0][0] = matriz[8][0][0] + 1

def funcion73(matriz):
    if matriz[8][0][1] == 9:
        matriz[8][0][1] = 1
    else:
        matriz[8][0][1] = matriz[8][0][1] + 1

def funcion74(matriz):
    if matriz[8][0][2] == 9:
        matriz[8][0][2] = 1
    else:
        matriz[8][0][2] = matriz[8][0][2] + 1

def funcion75(matriz):
    if matriz[8][1][0] == 9:
        matriz[8][1][0] = 1
    else:
        matriz[8][1][0] = matriz[8][1][0] + 1

def funcion76(matriz):
    if matriz[8][1][1] == 9:
        matriz[8][1][1] = 1
    else:
        matriz[8][1][1] = matriz[8][1][1] + 1

def funcion77(matriz):
    if matriz[8][1][2] == 9:
        matriz[8][1][2] = 1
    else:
        matriz[8][1][2] = matriz[8][1][2] + 1        

def funcion78(matriz):
    if matriz[8][2][0] == 9:
        matriz[8][2][0] = 1
    else:
        matriz[8][2][0] = matriz[8][2][0] + 1

def funcion79(matriz):
    if matriz[8][2][1] == 9:
        matriz[8][2][1] = 1
    else:
        matriz[8][2][1] = matriz[8][2][1] + 1

def funcion80(matriz):
    if matriz[8][2][2] == 9:
        matriz[8][2][2] = 1
    else:
        matriz[8][2][2] = matriz[8][2][2] + 1
        
Cuad00 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+2,CellSize-2,CellSize-2, '') #(0,0)
Cuad01 = button(BLANCO, CuadPos[0]+51,CuadPos[1]+2,CellSize-1,CellSize-2,'') #(0,1)
Cuad02 = button(BLANCO, CuadPos[0]+101,CuadPos[1]+2,CellSize-1,CellSize-2,'') #(0,2)
Cuad03 = button(BLANCO, CuadPos[0]+152,CuadPos[1]+2,CellSize-2,CellSize-2,'') #(0,3)
Cuad04 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+2,CellSize-1,CellSize-2,'') #(0,4)
Cuad05 = button(BLANCO, CuadPos[0]+251,CuadPos[1]+2,CellSize-1,CellSize-2,'') #(0,5)
Cuad06 = button(BLANCO, CuadPos[0]+302,CuadPos[1]+2,CellSize-2,CellSize-2,'') #(0,6)
Cuad07 = button(BLANCO, CuadPos[0]+351,CuadPos[1]+2,CellSize-1,CellSize-2,'') #(0,7)
Cuad08 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+2,CellSize-2,CellSize-2,'') #(0,8)
Cuad10 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+51,CellSize-2,CellSize-1,'') #(1,0)
Cuad11 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+51,CellSize-1,CellSize-1,'') #(1,1)
Cuad12 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+51,CellSize-1,CellSize-1,'') #(1,2)
Cuad13 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+51,CellSize-2,CellSize-1,'') #(1,3)
Cuad14 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+51,CellSize-1,CellSize-1,'') #(1,4)
Cuad15 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+51,CellSize-1,CellSize-1,'') #(1,5)
Cuad16 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+51,CellSize-2,CellSize-1,'') #(1,6)
Cuad17 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+51,CellSize-1,CellSize-1,'') #(1,7)
Cuad18 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+51,CellSize-2,CellSize-1,'') #(1,8)
Cuad20 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+101,CellSize-2,CellSize-1,'') #(2,0)
Cuad21 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+101,CellSize-1,CellSize-1,'') #(2,1)
Cuad22 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+101,CellSize-1,CellSize-1,'') #(2,2)
Cuad23 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+101,CellSize-2,CellSize-1,'') #(2,3)
Cuad24 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+101,CellSize-1,CellSize-1,'') #(2,4)
Cuad25 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+101,CellSize-1,CellSize-1,'') #(2,5)
Cuad26 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+101,CellSize-2,CellSize-1,'') #(2,6)
Cuad27 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+101,CellSize-1,CellSize-1,'') #(2,7)
Cuad28 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+101,CellSize-2,CellSize-1,'') #(2,8)
Cuad30 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+151,CellSize-2,CellSize-1,'') #(3,0)
Cuad31 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+151,CellSize-1,CellSize-1,'') #(3,1)
Cuad32 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+151,CellSize-1,CellSize-1,'') #(3,2)
Cuad33 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+151,CellSize-2,CellSize-1,'') #(3,3)
Cuad34 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+151,CellSize-1,CellSize-1,'') #(3,4)
Cuad35 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+151,CellSize-1,CellSize-1,'') #(3,5)
Cuad36 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+151,CellSize-2,CellSize-1,'') #(3,6)
Cuad37 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+151,CellSize-1,CellSize-1,'') #(3,7)
Cuad38 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+151,CellSize-2,CellSize-1,'') #(3,8)
Cuad40 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+201,CellSize-2,CellSize-1,'') #(4,0)
Cuad41 = button(BLANCO, CuadPos[0]+51,CuadPos[1]+201,CellSize-1,CellSize-1,'') #(4,1)
Cuad42 = button(BLANCO, CuadPos[0]+101,CuadPos[1]+201,CellSize-1,CellSize-1,'') #(4,2)
Cuad43 = button(BLANCO, CuadPos[0]+152,CuadPos[1]+201,CellSize-2,CellSize-1,'') #(4,3)
Cuad44 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+201,CellSize-1,CellSize-1,'') #(4,4)
Cuad45 = button(BLANCO, CuadPos[0]+251,CuadPos[1]+201,CellSize-1,CellSize-1,'') #(4,5)
Cuad46 = button(BLANCO, CuadPos[0]+302,CuadPos[1]+201,CellSize-2,CellSize-1,'') #(4,6)
Cuad47 = button(BLANCO, CuadPos[0]+351,CuadPos[1]+201,CellSize-1,CellSize-1,'') #(4,7)
Cuad48 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+201,CellSize-2,CellSize-1,'') #(4,8)
Cuad50 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+251,CellSize-2,CellSize-1,'') #(5,0)
Cuad51 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+251,CellSize-1,CellSize-1,'') #(5,1)
Cuad52 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+251,CellSize-1,CellSize-1,'') #(5,2)
Cuad53 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+251,CellSize-2,CellSize-1,'') #(5,3)
Cuad54 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+251,CellSize-1,CellSize-1,'') #(5,4)
Cuad55 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+251,CellSize-1,CellSize-1,'') #(5,5)
Cuad56 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+251,CellSize-2,CellSize-1,'') #(5,6)
Cuad57 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+251,CellSize-1,CellSize-1,'') #(5,7)
Cuad58 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+251,CellSize-2,CellSize-1,'') #(5,8)
Cuad60 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+301,CellSize-2,CellSize-1,'') #(6,0)
Cuad61 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+301,CellSize-1,CellSize-1,'') #(6,1)
Cuad62 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+301,CellSize-1,CellSize-1,'') #(6,2)
Cuad63 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+301,CellSize-2,CellSize-1,'') #(6,3)
Cuad64 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+301,CellSize-1,CellSize-1,'') #(6,4)
Cuad65 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+301,CellSize-1,CellSize-1,'') #(6,5)
Cuad66 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+301,CellSize-2,CellSize-1,'') #(6,6)
Cuad67 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+301,CellSize-1,CellSize-1,'') #(6,7)
Cuad68 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+301,CellSize-2,CellSize-1,'') #(6,8)
Cuad70 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+351,CellSize-2,CellSize-1,'') #(7,0)
Cuad71 = button(CELDABLOQUEADA, CuadPos[0]+51,CuadPos[1]+351,CellSize-1,CellSize-1,'') #(7,1)
Cuad72 = button(CELDABLOQUEADA, CuadPos[0]+101,CuadPos[1]+351,CellSize-1,CellSize-1,'') #(7,2)
Cuad73 = button(CELDABLOQUEADA, CuadPos[0]+152,CuadPos[1]+351,CellSize-2,CellSize-1,'') #(7,3)
Cuad74 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+351,CellSize-1,CellSize-1,'') #(7,4)
Cuad75 = button(CELDABLOQUEADA, CuadPos[0]+251,CuadPos[1]+351,CellSize-1,CellSize-1,'') #(7,5)
Cuad76 = button(CELDABLOQUEADA, CuadPos[0]+302,CuadPos[1]+351,CellSize-2,CellSize-1,'') #(7,6)
Cuad77 = button(CELDABLOQUEADA, CuadPos[0]+351,CuadPos[1]+351,CellSize-1,CellSize-1,'') #(7,7)
Cuad78 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+351,CellSize-2,CellSize-1,'') #(7,8)
Cuad80 = button(BLANCO, CuadPos[0]+2,CuadPos[1]+401,CellSize-2,CellSize-2,'') #(8,0)
Cuad81 = button(BLANCO, CuadPos[0]+51,CuadPos[1]+401,CellSize-1,CellSize-2,'') #(8,1)
Cuad82 = button(BLANCO, CuadPos[0]+101,CuadPos[1]+401,CellSize-1,CellSize-2,'') #(8,2)
Cuad83 = button(BLANCO, CuadPos[0]+152,CuadPos[1]+401,CellSize-2,CellSize-2,'') #(8,3)
Cuad84 = button(BLANCO, CuadPos[0]+201,CuadPos[1]+401,CellSize-1,CellSize-2,'') #(8,4)
Cuad85 = button(BLANCO, CuadPos[0]+251,CuadPos[1]+401,CellSize-1,CellSize-2,'') #(8,5)
Cuad86 = button(BLANCO, CuadPos[0]+302,CuadPos[1]+401,CellSize-2,CellSize-2,'') #(8,6)
Cuad87 = button(BLANCO, CuadPos[0]+351,CuadPos[1]+401,CellSize-1,CellSize-2,'') #(8,7)
Cuad88 = button(BLANCO, CuadPos[0]+401,CuadPos[1]+401,CellSize-2,CellSize-2,'') #(8,8)

Check = button(TURQUESA, 25, 25, 100,50,"CHECKING")