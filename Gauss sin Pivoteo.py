# Librería numpy
import numpy as np
from  time  import*

print('MÉTODO DE GAUSS SIN PIVOTEO',end="\n\n")

print("Este método transforma la matriz del sistema a una forma triangular superior.")

''' 
En esta primera versión del algoritmo se supondrá que el determinante de la matriz es diferente de cero y que no 
se requiere intercambiar filas. Además este método es mas rapido que el de Gauss-Jordan por realizar menos operaciones.
'''

def gauss1(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1) # Matriz aumentada
	print("\nMatriz:\n")
	print(c)
	for  e  in  range(n):
		t=c[e,e]
		print("\nCoeficiente para dividir la fila "+str(e+1)+": "+str(t))
		for j in range(e,n+1): # Normalizar fila	e
			c[e,j]=c[e,j]/t
		print("\nMatriz:\n")
		print(c)
		if e != n-1:
			print("\nRealizamos la eliminación de filas:\n")
		for i in range(e+1,n): # Reducir filas debajo
			t=c[i,e]
			for j in range(e,n+1): 
				c[i,j]=c[i,j]-t*c[e,j]
		if e != n-1:
			print(c)
	x=np.zeros([n,1]) # Celdas para el vector X 
	x[n-1]=c[n-1,n]
	for  i  in  range(n-2,-1,-1): 
		s=0
		for j in range(i+1,n): 
			s=s+c[i,j]*x[j]
		x[i]=c[i,n]-s 
	return x

# Coloca la matriz A:
A=np.array([[1,1,0,-1,0],[1,0,0,0,-1],[4,4,1,-2,-4],[0,1,0,0,-2],[0,0,2,0,0]],float)

# Coloca el vector solución b:
b=np.array([[0],[2],[8],[0],[4]],float)

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
x=gauss1(A,b)
t2=perf_counter(); #Calcula tiempo final del algoritmo

print("\nLa solución es:\n "+str(x))
print("\nEl tiempo de ejecución es: "+str(t2-t1))

R = x - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))


