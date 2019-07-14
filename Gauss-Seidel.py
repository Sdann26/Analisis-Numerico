import numpy as np

def gaussSeidel(A, b, x, N, tol):
    maxIterations = 1000000 # No modificar
    xprev = [0.0 for i in range(N)]
    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if (k != j):
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])  
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tol) and i != 0:
            print("\nLa solución converge en x: [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]\nLuego de", i + 1, "iteraciones\n")
            return
    print("La matriz no converge.")

# Matriz A
'''A = [[-4.6658333e+01, -8.6801220e+00, -1.6502950e+00],
[0.0, 1.2866580e+00, 5.2480200e-01],
[0.0, 0.0, 3.3315000e-02]]'''
A = np.array((
    (3.0, -0.1, -0.2),
    (0.1, 7.0, -0.3),
    (0.3, -0.2, -10.0),
))

# Vector b
'''b = [-10.308984, -1.929987, -0.0]'''
b = [7.85, -19.30, 71.40]

# Xo vector de iteraciòn inicial
v_inicial = [0.0, 0.0, 0.0]

print('MÉTODO DE GAUSS-SEIDEL',end="\n\n")

print("Este método te halla la solucion al sistema lineal si es que converge, caso contrario te mostrara que no converge, además que te da el numero de iteraciones necesarias para que converga",end="\n\n")

print('Matriz A:\n', A.round(6))

print('\nVector b:\n', b)

gaussSeidel(A, b, v_inicial, 3, 0.001)

# Recomendaciones:

'''Intentar siempre ordenar las ecuaciones tal que en la diagonal se encuentre los coeficientes mayores para asegurar la
 convergencia'''

'''En el caso de no tener vector inicial en algun problema tomar el convencional(Aquel que todos sus párametros son 0)'''

'''Si se busca hallar la solucion para un número N de iteraciones, debemos reducir o aumentar la 
toleracia(Quinto atributo de la función gaussSeidel) para que se modifiquen el numeor de iteraciones'''