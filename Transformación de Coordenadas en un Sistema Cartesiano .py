# =====================================
# TRANSFORMACIÓN DE COORDENADAS 2D
# =====================================

# Puntos originales (arreglo bidimensional)
puntos = [
    [1, 1],
    [2, 1],
    [2, 2],
    [1, 2]
]

# Matriz de rotación 90 grados
transformacion = [
    [0, -1],
    [1,  0]
]

# -----------------------------
# Mostrar puntos originales
# -----------------------------
print("Puntos originales:")
for p in puntos:
    print(p)

# -----------------------------
# Aplicar transformación
# -----------------------------
puntos_transformados = []

for p in puntos:
    x = p[0]
    y = p[1]
    
    # multiplicación matriz * vector
    x_nuevo = transformacion[0][0] * x + transformacion[0][1] * y
    y_nuevo = transformacion[1][0] * x + transformacion[1][1] * y
    
    puntos_transformados.append([x_nuevo, y_nuevo])

# -----------------------------
# Mostrar puntos transformados
# -----------------------------
print("\nPuntos después de la rotación:")
for p in puntos_transformados:
    print(p)