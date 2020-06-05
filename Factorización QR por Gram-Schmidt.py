# Librerías numpy y scipy
import math
from  time  import*
import numpy as np

def sumaGramm(A,m,x):
	suma = 0.0
	for k in range(m):
		suma = suma + A[k][x]*A[k][x]
	return suma

def productoGramm(A,m,x,y):
	producto = 0.0
	for k in range(m):
		producto = producto + (A[k][x]*A[k][y])
	return producto

def metodoGramm(A,b,n):
	#La matriz A es mxn por tanto la matriz E sera de orden mxn y U nxn

	#Creamos matriz E
	E = []
	for i in range(n):
		E.append([0]*n)
	#Creamos matriz U
	U = []
	for i in range(n):
		U.append([0]*n)
	
	#Algoritmo
	for j in range(n):
		for k in range(n):
			E[k][j] = A[k][j]
		for i in range(j):
			producto = 0.0
			U[i][j] = productoGramm(E,n,i,j)
			for k in range(n):
				E[k][j] = E[k][j] - U[i][j]*E[k][i]
		U[j][j] = math.sqrt(sumaGramm(E,n,j))
		for k in range(n):
			E[k][j] = E[k][j]/U[j][j]

	y = np.linalg.solve(E,b)
	x = np.linalg.solve(U,y)

	Q = np.array(E,float)
	R = np.array(U,float)

	print("Al finalizar el algoritmo tendremos:\n")
	print('Matriz Q:\n', Q.round(7))
	print('\nMatriz R:\n', R.round(7))

	return Q, R 

print('MÉTODO DE GRAM-SCHMIDT',end="\n\n")

print("Este método te descompone la matriz en dos matrices Q, R para encontrar las soluciones mediante el método de ortogonalización de Gram-Schmidt",end="\n\n")

# Insetar la matriz A
A = np.array([[10, 30, 70],
    		[30, 50, 20],
    		[70, 20, 10]],float)

# Inserte el vector 'b'
b = np.array([44, 38, 18],float)

n = A.shape

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
Q, R = metodoGramm(A,b,n[0])
t2=perf_counter(); #Calcula tiempo final del algoritmo

Qt = np.transpose(Q)

print("\nPara calcular la solucion 'x' del problema, resolveremos R * x = Qt(Q transpuesta) * b",end="\n")

print('\nMatriz Q transpuesta:\n', Qt.round(7))

print('\nVector b:\n', b.round(7))

# Para matrices nxn
x = np.linalg.solve(R, Qt @ b) # Desarrollo del sistema R * x = Qt(Q transpuesta) * b

print("\nSolucion de 'x':",x.round(7), end="\n")

print("\nEl tiempo de ejecución es: "+str(t2-t1))

R = x - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.norm(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.norm(A,np.inf)))