# Librería numpy
import numpy as np
from  time  import*

def sumD(n,A,t,x):
	s = 0
	for i in range(0,n):
		s=s+A[t][i]*x[i]
	return s
def sumI(j,n,A,t,x):
	s = 0
	if j>=n :
		return 0
	for i in range(j,n):
		s=s+A[i][t]*x[i]
	return s

def sum1(i,j,A):
	s = 0
	if i==0:
		return 0
	for k in range(0,i):
		s=s+A[j][k]*A[i][k]
	return s

def pivoteT(n,i,A,b):
	if i>=0 and i<n:
		p=i
		for k in range(i+1,n):
			if abs(A[p][p])<abs(A[k][k]):
				p=k
		if p!=i:
			t=0
			for z in range(n):
				t=A[i][z]
				A[i][z] = A[p][z]
				A[p][z] = t
			for z in range(n):
				t=A[z][i]
				A[z][i] = A[z][p]
				A[z][p] = t
			t=b[i]
			b[i]=b[p]
			b[p]=t

print('MÉTODO DE CHOLESKY CON PIVOTEO',end="\n\n")

print("Este método descompone la matriz A en las matrices G y Gt para encontrar de manera mas sencilla la solución x\n")

# Inserta el rango de la matriz A
n = int(input('Ingrese orden de la matriz A: '))

'''
Este algoritmo se aplica a una matriz simétrica definida positiva, esta puede ser descompuesta como el producto de una matriz 
triangular inferior y la traspuesta de la matriz triangular inferior. La matriz triangular inferior es el triángulo de Cholesky 
de la matriz original positiva definida.
En el caso que se desee la descomposición LDLt. Se pasara G = L * D' y Gt = D* * Lt. Siendo L y Lt matrices con diagonal llena de 1
y D = D' * D*, siendo D una matriz diagonal con los elementos al cuadrado de ambas matrices.
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
A = np.array([[4,-1,0,-1,0,0],
			[-1,4,-1,0,-1,0],
			[0,-1,4,0,0,-1],
			[-1,0,0,4,-1,0],
			[0,-1,0,-1,4,-1],
			[0,0,-1,0,-1,4]],float) 

# Coloca el vector solución b
b=np.array([56,25,62,41,10,47],float)

	
print (' ')
print ('Matriz A:')
print(A)

print ('Vector b:')
print(b)

print ('\nRealizamos pivoteo si es necesario, A:')
for i in range(n):
	pivoteT(n,i,A,b)  
print(A)   

for i in range(0,n):	  
	if A[i][i] == 0:
		band = False
		break

if band:
	for j in range(n):
		for i in range(j,n):
			if i==j:
				L[i][i]=(A[i][i] - sum1(i,j,L))**0.5
			else:
				L[i][j]=(A[i][j] - sum1(i,j,L))/L[j][j]
	
	L = np.array(L,float)
	print ('\nMatriz G:')
	print(L)

	print ('\nMatriz G transpuesta:')
	print(np.transpose(L))

	# Desarrollo del sistema G * y = b 
	for i in range(0,n):
		y[i] = (b[i]-sumD(i,L,i,y))/L[i][i]
	print ('\nSolucion de G * y = b es:')
	y = np.array(y,float)
	print (y.round(7))
	
	# Desarrollo del sistema (Gt) * x = y 
	for i in range(0,n):
		x[n-1-i] = (y[n-1-i]-sumI(n-i,n,L,n-1-i,x))/L[n-1-i][n-1-i]
	print ('\nSolución de Gt * x = y es:')
	x = np.array(x,float)
	print (x.round(7))
	print("Tener en cuenta que es solución de la matriz pivoteada")
else:
	print ('No hay solución unica')

