laberinto = [
    ['F', 1,  0, 3, 1, 0, 1, 1, 1],
    [ 1,  3,  0, 4, 1, 1, 1, 0, 1],
    [ 1,  0,  3, 1, 0, 3, 4, 1, 1],
    [ 1,  4,  1, 1, 1, 0, 1, 3, 0],
    [ 0,  1,  0, 3, 4, 1, 1, 0, 1],
    [ 1,  1,  1, 0, 1, 3, 0, 1, 1],
    [ 3,  0, 4, 1, 1, 4, 1, 1, 0],
    [ 1,  1,  1, 0, 3, 1, 0, 4, 1],
    ['I', 3,  4, 1, 1, 1, 1, 1, 1]
]

camino_encontrado = []
puntos_totales = 0

def imprimir_laberinto(mat):
    for fila in mat:
        print(fila)
    print()

def backtracking(x, y, puntos_actuales, visitados, camino):
    global camino_encontrado, puntos_totales
    
    if laberinto[x][y] == 'F':
        if puntos_actuales >= 23:  
            camino_encontrado = list(camino)
            puntos_totales = puntos_actuales
            return True
        return False
        
    visitados[x][y] = True
    
    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for m in movimientos:
        nx = x + m[0]
        ny = y + m[1]
        
        if nx >= 0 and nx < 9 and ny >= 0 and ny < 9:
            if laberinto[nx][ny] != 0 and not visitados[nx][ny]:
                
                extra = 0
                valor_celda = laberinto[nx][ny]
                if valor_celda == 3 or valor_celda == 4:
                    extra = valor_celda
                
                camino.append((nx, ny))
                
                if backtracking(nx, ny, puntos_actuales + extra, visitados, camino):
                    return True
                
                camino.pop()
                
    visitados[x][y] = False
    return False

visitados = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append(False)
    visitados.append(fila)

inicio_x = 8
inicio_y = 0
camino_inicial = [(inicio_x, inicio_y)]

print("=== LABERINTO ORIGINAL ===")
imprimir_laberinto(laberinto)

exito = backtracking(inicio_x, inicio_y, 0, visitados, camino_inicial)

if exito:
    print("Se encontro un camino valido.")
    print("Puntos totales sumados:", puntos_totales)
    print()
    
    matriz_resultado = []
    for fila in laberinto:
        matriz_resultado.append(list(fila))
        
    for coord in camino_encontrado:
        rx = coord[0]
        ry = coord[1]
        if laberinto[rx][ry] != 'I' and laberinto[rx][ry] != 'F':
            matriz_resultado[rx][ry] = '*'
            
    print("=== MATRIZ INDICANDO CÓMO SALIR ===")
    imprimir_laberinto(matriz_resultado)
else:
    print("Ningun camino alcanzo los 23 puntos minimos.")