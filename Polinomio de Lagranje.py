# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

print('INTERPOLACIÓN POLINÓMICA DE LAGRANJE',end="\n\n")

print("Es una forma de presentar el polinomio que interpola un conjunto de puntos dado. ",end="\n\n")

# INGRESO , Datos de prueba

# Datos de X
xi = np.array([-1.5, -0.75, 0, 0.75, 1.5])

# Datos de F(X)
fi = np.array([-14.1014, -0.931596, 0, 0.931596, 14.1014])

# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0,n,1):
    # Termino de Lagrange
    termino = 1
    for j  in range(0,n,1):
        if (j!=i):
            termino = termino*(x-xi[j])/(xi[i]-xi[j])
    print("El L(",i,") es :", termino)
    polinomio = polinomio + termino*fi[i]
# Expande el polinomio
px = polinomio.expand()
# para evaluacion numérica
pxn = sym.lambdify(x,polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a,b,muestras)
fi_p = pxn(xi_p)

# Salida
print('\nPolinomio de Lagrange, expresiones:')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(px)

# Gráfica
plt.title('Interpolación Lagrange')
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(xi_p,fi_p, label = 'Polinomio')
plt.legend()
plt.show()