# =====================================
# TABLA DE SENSORES 5x5 SIN LIBRERÍAS
# =====================================

# Datos: filas = tiempo, columnas = sensores
datos = [
    [22, 24, 23, 25, 26],
    [21, 23, 22, 24, 25],
    [20, 22, 21, 23, 24],
    [23, 25, 24, 26, 27],
    [22, 24, 23, 25, 26]
]

# -----------------------------
# Mostrar tabla
# -----------------------------
print("Tabla de temperaturas:")
for fila in datos:
    print(fila)

# -----------------------------
# Promedio por sensor (columnas)
# -----------------------------
print("\nPromedios por sensor:")

for col in range(5):
    suma = 0
    for fila in range(5):
        suma = suma + datos[fila][col]
    
    promedio = suma / 5
    print("Sensor", col + 1, ":", promedio)

# -----------------------------
# Promedio por tiempo (filas)
# -----------------------------
print("\nPromedios por momento en el tiempo:")

for i in range(5):
    suma = 0
    for j in range(5):
        suma = suma + datos[i][j]
    
    promedio = suma / 5
    print("Tiempo", i + 1, ":", promedio)

# -----------------------------
# Desviación estándar por sensor
# -----------------------------
print("\nDesviación estándar por sensor:")

for col in range(5):
    suma = 0
    
    # calcular promedio
    for fila in range(5):
        suma = suma + datos[fila][col]
    promedio = suma / 5
    
    # calcular varianza
    suma_cuadrados = 0
    for fila in range(5):
        diferencia = datos[fila][col] - promedio
        suma_cuadrados = suma_cuadrados + diferencia * diferencia
    
    varianza = suma_cuadrados / 5
    desviacion = varianza ** 0.5
    
    print("Sensor", col + 1, ":", desviacion)