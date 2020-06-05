# Librería numpy
import numpy as np
from  time  import*
import math

def metodoCholesky(A,b,n):

	# Creamos matriz nula G
	G = [[0.0]*n]*n

	# Creamos matriz nula GT
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma = suma - A[k][i]**2
		if suma < 0: # No es definida positiva
			return ["NULL","NULL"]
		A[i][i] = math.sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma = suma - A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0
	Gt = A
	G = np.transpose(Gt)

	print ('\nMatriz G:')
	print(G)

	print ('\nMatriz G transpuesta:')
	print(Gt)

	return G,Gt

print('MÉTODO DE CHOLESKY SIN PIVOTEO',end="\n\n")

print("Este método descompone la matriz A en las matrices L y Lt para encontrar de manera mas sencilla la solución x\n")

# Inserta el rango de la matriz A
n = int(input('Ingrese orden de la matriz A: '))

'''
Este algoritmo se aplica a una matriz simétrica definida positiva, esta puede ser descompuesta como el producto de una matriz 
triangular inferior y la traspuesta de la matriz triangular inferior. La matriz triangular inferior es el triángulo de Cholesky 
de la matriz original positiva definida.

'''

A=[]
L=[]
b=[]
y=[]
x=[]
m = 0
band = True

for i in range(n):
	A.append([])
	L.append([])
	x.append(0)
	y.append(0)
	b.append(0)
	for j in range(n):
		A[i].append(0)
		L[i].append(0)

# Matriz a usar:
A = np.array([[4,-1,0],
			[-1,4,-1],
			[0,-1,4]],float) 

# Copiar la matriz A aqui con el nombre Ap:
Ap = np.array([[4,-1,0],
			[-1,4,-1],
			[0,-1,4]],float) 

# Coloca el vector solución b
b=np.array([1,0,0],float)

np.linalg.cholesky(A)
	
print ('Matriz A:')
print(A)

print ('Vector b:')
print(b)

G, Gt = metodoCholesky(A,b,n)

y = np.array(y,float)
x = np.array(x,float)

print("\nPrimero, resolvemos L * y =  b:")
y = np.linalg.solve(G,b)
print("La solución de 'y' es:\n" +str(y.round(7)))

print("\nLuego desarrollamos Lt * x = y:")
x = np.linalg.solve(Gt,y)
print("La solución de 'x' es: \n"+str(x.round(7)))

R = x - np.linalg.solve(Ap,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(Ap,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(Ap,np.inf)))