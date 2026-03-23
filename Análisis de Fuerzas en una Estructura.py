# Matriz 3x3 que representa las fuerzas en los nodos
fuerzas = [
    [10, 5, 0],
    [-3, 8, 2],
    [4, -6, 1]
]

# Mostrar la matriz
print("Matriz de fuerzas:")
for fila in fuerzas:
    print(fila)

# Calcular la suma total de fuerzas
suma_total = 0

for i in range(3):
    for j in range(3):
        suma_total += fuerzas[i][j]

print("\nSuma total de fuerzas:", suma_total)

# Reacción necesaria para equilibrio
reaccion = -suma_total
print("Reacción total en los apoyos:", reaccion)