# Librería numpy
import numpy as np
from  time  import*

print('MÉTODO LU SIN PIVOTEO',end="\n\n")

print("Este método te halla las matrices L y U y cálcula la solución del sistema L * U * X = b.")

'''
Este algoritmo usa método de Crout proporciona una forma alternativa de factorizar A en una descomposición LU
sin pasar por la molestia de la eliminación gaussiana.
'''

def luDecomposition(A, n): 

    L = np.zeros((n, n))  
    U = np.zeros((n, n))

    print(L)

    for k in range (n):
        for i in range(k,n):
            sum1=0
            for p in range (k):
                sum1+=L[i][p]*U[p][k]
            L[i][k]=(A[i][k]-sum1)

        for i in range(k+1,n):
            if L[k][k] == 0:
                exit('Debe usar el pivoteo parcial')
            sum2=0
            for p in range(k):
                sum2+=L[k][p]*U[p][i]
            U[k][i]=(A[k][i]-sum2)/L[k][k]

    U = U + np.eye(n, dtype=float)

    return L,U

# Coloca la matriz A:
A=np.array([[1,1,0,-1,0],[1,0,0,0,-1],[4,4,1,-2,-4],[0,1,0,0,-2],[0,0,2,0,0]],float)

# Coloca el vector solución b:
b=np.array([0,2,8,0,4],float)


t1=perf_counter(); #Calcula tiempo inicio del algoritmo
# Función LU, aquí se inserta la matriz y su tamaño
L,U=luDecomposition(A, 5);
t2=perf_counter(); #Calcula tiempo final del algoritmo

A = np.array(A,float)
L = np.array(L,float)
U = np.array(U,float)

print("\nMatriz A:\n"+str(A))
print("\nMatriz L:\n"+str(L))
print("\nMatriz U:\n"+str(U))
print("\nVector solución b: \n"+str(b))

print("\nEl tiempo de ejecución es: "+str(t2-t1))

print("\nPrimero, resolvemos L * Y = b:")
y = np.linalg.solve(L,b)
print("La solución Y es:" +str(y.round(7)))
print("\nLuego desarrollamos U * X = Y:")
x = np.linalg.solve(U,y)
print("La solución X es: "+str(x.round(7)))

R = x - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))