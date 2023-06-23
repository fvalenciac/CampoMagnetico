import numpy as np
import matplotlib.pyplot as plt

def calcular_campo_magnetico(corriente, x):
    mu0 = 4 * np.pi * 1e-7  # Permeabilidad del vacío
    r = np.sqrt(x**2)  # Distancia desde el conductor
    B = (mu0 * corriente) / (2 * np.pi * r)  # Campo magnético
    return B

# Solicitar al usuario los datos de entrada
corriente = float(input("Ingresa la corriente en amperios: "))
posicion_inicial = float(input("Ingresa la posición inicial en metros: "))
posicion_final = float(input("Ingresa la posición final en metros: "))
num_puntos = int(input("Ingresa el número de puntos a calcular: "))

# Generar los valores de x
x = np.linspace(posicion_inicial, posicion_final, num_puntos)

# Calcular el campo magnético en cada posición
B = calcular_campo_magnetico(corriente, x)

# Graficar los resultados
plt.plot(x, B)
plt.xlabel('Posición (m)')
plt.ylabel('Campo magnético (T)')
plt.title('Distribución del campo magnético')
plt.grid(True)
plt.show()