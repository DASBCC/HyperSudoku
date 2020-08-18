ANCHO = 600
ALTO = 600

BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
<<<<<<< HEAD
LINO = (250,240,230)
CELESTE = (96, 216, 232)
CELDABLOQUEADA = (189,189,189)
COLORINCORRECTO = (195,121,121)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
MORADO = (87,35,100)
AMARILLO = (229,190,1)
CAFE = (128,64,0)
TURQUESA = (93,193,185)
TURQ_OSCURO = (0,32,32)
=======
ROSADO = (255,0,255)
AZUL = (0,0,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
MORADO = (180,26,236)
NARANJA = (255,128,0) 
CAFE = (153, 76, 0)
AMARILLO = (255,255,0)
CELESTE = (96, 216, 232)
CELDABLOQUEADA = (189,189,189)
COLORINCORRECTO = (195,121,121)

COLORES = [AZUL, VERDE, ROJO, MORADO, NARANJA, CAFE, AMARILLO, CELESTE, ROSADO]
>>>>>>> c9d91527c43224e5a9b1808b371382df475e4cb6
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

# Positions and sizes
CuadPos = (75,100)
CellSize = 50
CuadSize = CellSize*9


