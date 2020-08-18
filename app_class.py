import pygame, sys
from Configuracion import *
from Botones import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((ANCHO, ALTO))
        self.running = True
        self.selected = None
        self.mousePos = None
        self.state = "Jugando"
        self.jugandoButtons = []
        self.colores = [ROJO, VERDE, AZUL, MORADO, AMARILLO, CAFE, TURQUESA, TURQ_OSCURO, CELESTE]

    def run(self):
        while self.running:
            if self.state == "Jugando":
                self.jugando_events()
                self.jugando_update()
                self.jugando_draw()
        pygame.quit()
        sys.exit()
########### Funciones que se ejecutan mientras se esta jugando ##########
    def jugando_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnCuad()
                if selected:
                    print(selected)
                else:
                    print ("no está en la tabla")
                    self.selected = None 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 and Cuad00.isOver(pos):
                    Cuad00 = button(NEGRO, CuadPos[0]+2,CuadPos[1]+2,CellSize-2,CellSize-2, '')




    def jugando_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.jugandoButtons:
            button.update(self.mousePos)

    def jugando_draw(self):
        self.window.fill(LINO)

        for button in self.jugandoButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.drawCuad(self.window)
        self.Cuadrados(self.window)
        self.menu_Botones(self.window)
        pygame.display.update()



##### Funciones auxiliares #####

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, CELESTE, ((pos[0]*CellSize)+CuadPos[0], (pos[1]*CellSize)+CuadPos[1], CellSize, CellSize))
    
    def drawCuad(self, window):
        pygame.draw.rect(window, NEGRO, (CuadPos[0], CuadPos[1], ANCHO-150 , ALTO -150),2)
        for x in range(9):
            if x%3 !=0:
                pygame.draw.line(window, NEGRO, (CuadPos[0]+(x*CellSize), CuadPos[1]), (CuadPos[0] + (x*CellSize), CuadPos[1] + 450))
                pygame.draw.line(window, NEGRO, (CuadPos[0], CuadPos[1] + (x*CellSize)), (CuadPos[0] + 450, CuadPos[1] + (x*CellSize)))
            else:
                pygame.draw.line(window, NEGRO, (CuadPos[0]+(x*CellSize), CuadPos[1]), (CuadPos[0] + (x*CellSize), CuadPos[1] + 450), 2)
                pygame.draw.line(window, NEGRO, (CuadPos[0], CuadPos[1] + (x*CellSize)), (CuadPos[0] + 450, CuadPos[1] + (x*CellSize)))

    def menu_Botones(self, window):
        Check.draw(window)

    def Cuadrados(self,window): 
        Cuad00.draw(window)
        Cuad01.draw(window)
        Cuad02.draw(window)
        Cuad03.draw(window)
        Cuad04.draw(window)
        Cuad05.draw(window)
        Cuad06.draw(window)
        Cuad07.draw(window)
        Cuad08.draw(window)
        Cuad10.draw(window)
        Cuad11.draw(window)
        Cuad12.draw(window)
        Cuad13.draw(window)
        Cuad14.draw(window)
        Cuad15.draw(window)
        Cuad16.draw(window)
        Cuad17.draw(window)
        Cuad18.draw(window)
        Cuad20.draw(window)
        Cuad21.draw(window)
        Cuad22.draw(window)
        Cuad23.draw(window)
        Cuad24.draw(window)
        Cuad25.draw(window)
        Cuad26.draw(window)
        Cuad27.draw(window)
        Cuad28.draw(window)
        Cuad30.draw(window)
        Cuad31.draw(window)
        Cuad32.draw(window)
        Cuad33.draw(window)
        Cuad34.draw(window)
        Cuad35.draw(window)
        Cuad36.draw(window)
        Cuad37.draw(window)
        Cuad38.draw(window)
        Cuad40.draw(window)
        Cuad41.draw(window)
        Cuad42.draw(window)
        Cuad43.draw(window)
        Cuad44.draw(window)
        Cuad45.draw(window)
        Cuad46.draw(window)
        Cuad47.draw(window)
        Cuad48.draw(window)
        Cuad50.draw(window)
        Cuad51.draw(window)
        Cuad52.draw(window)
        Cuad53.draw(window)
        Cuad54.draw(window)
        Cuad55.draw(window)
        Cuad56.draw(window)
        Cuad57.draw(window)
        Cuad58.draw(window)
        Cuad60.draw(window)
        Cuad61.draw(window)
        Cuad62.draw(window)
        Cuad63.draw(window)
        Cuad64.draw(window)
        Cuad65.draw(window)
        Cuad66.draw(window)
        Cuad67.draw(window)
        Cuad68.draw(window)
        Cuad70.draw(window)
        Cuad71.draw(window)
        Cuad72.draw(window)
        Cuad73.draw(window)
        Cuad74.draw(window)
        Cuad75.draw(window)
        Cuad76.draw(window)
        Cuad77.draw(window)
        Cuad78.draw(window)
        Cuad80.draw(window)
        Cuad81.draw(window)
        Cuad82.draw(window)
        Cuad83.draw(window)
        Cuad84.draw(window)
        Cuad85.draw(window)
        Cuad86.draw(window)
        Cuad87.draw(window)
        Cuad88.draw(window)


    def mouseOnCuad(self):
        if self.mousePos[0] < CuadPos[0] or self.mousePos[1] < CuadPos[1]:
            return False
        if self.mousePos[0] > CuadPos[0] + CuadSize or self.mousePos[1] > CuadPos[1] + CuadSize:
            return False
        return ((self.mousePos[0]-CuadPos[0])//CellSize, (self.mousePos[1] - CuadPos[1])//CellSize)
