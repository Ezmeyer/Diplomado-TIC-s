# ======================================
# SIMULACIÓN DE FLUIDO EN UNA CUADRÍCULA 3D
# ======================================

TAM = 3

# ------------------------------
# Crear el volumen de fluido
# ------------------------------
def crear_fluido():
    fluido = [[[ [0, 20, 0] for z in range(TAM)]
               for y in range(TAM)]
               for x in range(TAM)]
    
    # Perturbación inicial en el centro
    fluido[1][1][1][0] = 100   # presión alta en el centro
    
    return fluido


# ------------------------------
# Mostrar presión del fluido
# ------------------------------
def mostrar_presion(fluido):
    print("\nDistribución de presión:")
    for z in range(TAM):
        print(f"\nCapa z = {z}")
        for y in range(TAM):
            for x in range(TAM):
                print(f"{fluido[x][y][z][0]:6.1f}", end=" ")
            print()


# ------------------------------
# Obtener vecinos válidos
# ------------------------------
def obtener_vecinos(x, y, z):
    vecinos = []
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                
                nx = x + dx
                ny = y + dy
                nz = z + dz
                
                if 0 <= nx < TAM and 0 <= ny < TAM and 0 <= nz < TAM:
                    vecinos.append((nx, ny, nz))
    
    return vecinos


# ------------------------------
# Simular un paso de tiempo
# ------------------------------
def simular_paso(fluido):
    
    nuevo = [[[fluido[x][y][z][:] for z in range(TAM)]
              for y in range(TAM)]
              for x in range(TAM)]
    
    for x in range(TAM):
        for y in range(TAM):
            for z in range(TAM):
                
                vecinos = obtener_vecinos(x, y, z)
                
                suma_presion = 0
                
                for nx, ny, nz in vecinos:
                    suma_presion += fluido[nx][ny][nz][0]
                
                if len(vecinos) > 0:
                    nueva_presion = suma_presion / len(vecinos)
                    nuevo[x][y][z][0] = nueva_presion
    
    return nuevo


# ======================================
# PROGRAMA PRINCIPAL
# ======================================

fluido = crear_fluido()

print("Estado inicial:")
mostrar_presion(fluido)

# Simular 3 pasos de propagación
for paso in range(1, 4):
    fluido = simular_paso(fluido)
    print(f"\nEstado después del paso {paso}:")
    mostrar_presion(fluido)