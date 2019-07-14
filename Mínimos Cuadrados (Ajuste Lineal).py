# Librería numpy
import numpy as np
from matplotlib import pyplot as plt

# Datos experimentales
x = np.array([ 176, 168, 202, 138, 213, 159, 193, 122, 185, 153])
y = np.array([ 448, 556, 844, 427, 811, 398, 447, 154, 534, 313])

# Ajuste a una recta (polinomio de grado 1)
p = np.polyfit(x, y, 1)

print('MÉTODO DE AJUSTE LINEAL POR MÍNIMOS CUADRADOS',end="\n\n")

# Imprime la ecuación de mínimos cuadrados
print("Este método te cálcula los parametros a y b para la ecuacion f(x) = a * x + b mediante ajuste lineal por mínimos cuadrados")
a = p[0] # Párametro a
b = p[1] # Párametro b
# print(p)
print("a = "+ str(a) + ", b = " + str(b),end="\n\n")
print("La ecuación es f(x) = " + str(round(a,3)) +" * x + "+ str(round(b,3)),end="\n\n")


# Valores de y calculados del ajuste
y_ajuste = p[0]*x + p[1]
# Dibujamos los datos experimentales
p_datos, = plt.plot(x, y, 'b.')
# Dibujamos la recta de ajuste
p_ajuste, = plt.plot(x, y_ajuste, 'r-')

plt.title('Ajuste lineal por minimos cuadrados')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper left")
plt.show()

