import pygame

class Button:
    def __init__(self, x, y, ANCHO, ALTO,texto=None, color=(255,0,0), colorclaro=(234,137,154), funcion=None, parametros=None):
        self.image = pygame.Surface((ANCHO, ALTO))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.texto = texto
        self.color = color
        self.colorclaro = colorclaro
        self.funcion =  funcion
        self.parametros = parametros
        self.claro = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.claro = True
        else:
            self.claro = False
    
    def draw(self, window):
        if self.claro:
            self.image.fill(self.colorclaro)
        else:
            self.image.fill(self.color)
        window.blit(self.image, self.pos)