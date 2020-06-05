# Librería numpy
import numpy as np
from  time  import*

print('MÉTODO DE GAUSS CON PIVOTEO PARCIAL',end="\n\n")

print("Este método transforma la matriz del sistema a una forma triangular superior usando pivoteo parcial.")

def gauss(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1)	# Matriz aumentada
	print("\nMatriz:\n")
	print(c)
	for  e  in  range(n):
		p=e
		for i in range(e+1,n): # Pivoteo
			if abs(c[i,e])>abs(c[p,e]): 
				p=i
				print("\nPivote: "+str(c[p,e]))
		for j in range(e,n+1): # Intercambio de filas
			t=c[e,j] 
			c[e,j]=c[p,j] 
			c[p,j]=t
		print("\nMatriz con las filas intercambiadas:\n")
		print(c)
		t=c[e,e]
		print("\nCoeficiente para dividir la fila "+str(e+1)+": "+str(t))
		if abs(t)<1e-20: # Sistema singular
			return []
		c[e,e:]=c[e,e:]/c[e,e] # Normalizar fila e
		print("\nMatriz:\n")
		print(c)
		print("\nRealizamos la eliminación de filas:\n")
		for i in range(e+1,n): 
			c[i,e:]=c[i,e:]-c[i,e]*c[e,e:] # Reducir filas debajo
		print(c)
	x=np.zeros([n]) 
	x[n-1]=c[n-1,n]
	for  i  in  range(n-2,-1,-1): # Sistema singular
		x[i]=c[i,n]-np.dot(x[i+1:n],c[i,i+1:n])
	return x

# Coloca la matriz A:
A=np.array([[1,1,0,-1,0],[1,0,0,0,-1],[4,4,1,-2,-4],[0,1,0,0,-2],[0,0,2,0,0]],float)

# Coloca el vector solución b:
b=np.array([[0],[2],[8],[0],[4]],float)

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
x=gauss(A,b)
t2=perf_counter(); #Calcula tiempo final del algoritmo

print("\nLa solución es: "+str(x))
print("\nEl tiempo de ejecución es: "+str(t2-t1))

x = np.array([x],float)

R = np.transpose(x) - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))