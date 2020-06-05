# Librería numpy
import numpy as np
from  time  import*

print('MÉTODO DE GAUSS-JORDAN',end="\n\n")

print("Este método te cálcula la solución del sistema A * X = b.")

''' 
En esta primera versión del algoritmo se supondrá que el determinante de la matriz es diferente de cero y que no se requiere
intercambiar filas.
'''

def gaussjordan1(a,b): 
	n=len(b)
	c=np.concatenate([a,b],axis=1)	# Matriz aumentada
	print("\nMatriz:\n")
	print(c)
	for  e  in  range(n):
		t=c[e,e]
		print("\nCoeficiente para dividir la fila "+str(e+1)+": "+str(t))
		for j in range(e,n+1):
			c[e,j]=c[e,j]/t	# Normalizar fila e
		print("\nMatriz:\n")
		print(c)
		print("\nRealizamos la eliminación de filas:\n")
		for i in range(n): 
			if i!=e:
				t=c[i,e]
				for j in range(e,n+1):
					c[i,j]=c[i,j]-t*c[e,j]	# Reducir otras filas
		print(c)
	x=c[:,n]
	return x

# Coloca la matriz A:
A=np.array([[1,1,0,-1,0],[1,0,0,0,-1],[4,4,1,-2,-4],[0,1,0,0,-2],[0,0,2,0,0]],float)

# Coloca el vector solución b:
b=np.array([[0],[2],[8],[0],[4]],float)

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
x=gaussjordan1(A,b)
t2=perf_counter(); #Calcula tiempo final del algoritmo

print("\nLa solución es: "+str(x))
print("\nEl tiempo de ejecución es: "+str(t2-t1))

x = np.array([x],float)

R = np.transpose(x) - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))