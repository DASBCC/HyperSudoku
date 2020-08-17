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


    def jugando_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.jugandoButtons:
            button.update(self.mousePos)

    def jugando_draw(self):
        self.window.fill(BLANCO)

        for button in self.jugandoButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.drawCuad(self.window)
        self.drawSelection(self.window, self.selected)
        pygame.display.update()

##### Funciones auxiliares #####

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, CELESTE, ((pos[0]*CellSize)+CuadPos[0], (pos[1]*CellSize)+CuadPos[1], CellSize, CellSize))
    
    def drawCuad(self, window):
        pygame.draw.rect(window, NEGRO, (CuadPos[0], CuadPos[1], ANCHO-150 , ALTO -150),2)
        for x in range(9):
            if x%3 !=0:
                pygame.draw.line(window, NEGRO, (CuadPos[0]+(x*CellSize), CuadPos[1]), (CuadPos[0] + (x*CellSize), CuadPos[1] + 450))
                pygame.draw.line(window, NEGRO, (CuadPos[0], CuadPos[1] + (x*CellSize)), (CuadPos[0] + 450, CuadPos[1] ++ (x*CellSize)))
            else:
                pygame.draw.line(window, NEGRO, (CuadPos[0]+(x*CellSize), CuadPos[1]), (CuadPos[0] + (x*CellSize), CuadPos[1] + 450), 2)
                pygame.draw.line(window, NEGRO, (CuadPos[0], CuadPos[1] + (x*CellSize)), (CuadPos[0] + 450, CuadPos[1] ++ (x*CellSize)))

    def Boton(self,window): ###PRUEBA ESTE SE MODIFICA Y COLOCAMOS LOS BOTONES
        pygame.draw.rect(window, CELESTE, (100,100,200,200))

    def mouseOnCuad(self):
        if self.mousePos[0] < CuadPos[0] or self.mousePos[1] < CuadPos[1]:
            return False
        if self.mousePos[0] > CuadPos[0] + CuadSize or self.mousePos[1] > CuadPos[1] + CuadSize:
            return False
        return ((self.mousePos[0]-CuadPos[0])//CellSize, (self.mousePos[1] - CuadPos[1])//CellSize)
