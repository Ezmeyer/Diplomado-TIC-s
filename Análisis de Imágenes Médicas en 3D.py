# ======================================
# ANÁLISIS DE IMÁGENES MÉDICAS 3D
# FILTRO DE PROMEDIO PARA REDUCIR RUIDO
# ======================================

TAM = 3

# ------------------------------
# Crear volumen de ejemplo con ruido
# ------------------------------
def crear_volumen():
    volumen = [
        [[12, 15, 14],
         [16, 18, 17],
         [15, 14, 13]],

        [[20, 22, 21],
         [23, 100, 24],   # ruido (valor anómalo)
         [21, 20, 19]],

        [[18, 17, 16],
         [19, 18, 17],
         [16, 15, 14]]
    ]
    return volumen


# ------------------------------
# Mostrar el volumen por capas
# ------------------------------
def mostrar_volumen(volumen, titulo):
    print("\n", titulo)
    for z in range(TAM):
        print(f"\nCapa {z}:")
        for y in range(TAM):
            for x in range(TAM):
                print(f"{volumen[z][y][x]:5}", end=" ")
            print()


# ------------------------------
# Obtener vecinos válidos
# ------------------------------
def obtener_vecinos(volumen, z, y, x):
    vecinos = []
    
    for dz in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                
                nz = z + dz
                ny = y + dy
                nx = x + dx
                
                if 0 <= nz < TAM and 0 <= ny < TAM and 0 <= nx < TAM:
                    vecinos.append(volumen[nz][ny][nx])
    
    return vecinos


# ------------------------------
# Filtro de promedio 3D
# ------------------------------
def suavizar_volumen(volumen):
    
    nuevo = [[[0 for x in range(TAM)]
              for y in range(TAM)]
              for z in range(TAM)]
    
    for z in range(TAM):
        for y in range(TAM):
            for x in range(TAM):
                
                vecinos = obtener_vecinos(volumen, z, y, x)
                promedio = sum(vecinos) / len(vecinos)
                nuevo[z][y][x] = round(promedio, 2)
    
    return nuevo


# ======================================
# PROGRAMA PRINCIPAL
# ======================================

volumen = crear_volumen()

mostrar_volumen(volumen, "VOLUMEN ORIGINAL")

volumen_suavizado = suavizar_volumen(volumen)

mostrar_volumen(volumen_suavizado, "VOLUMEN SUAVIZADO")