# Importando Numpy
import numpy as np
import pprint

print('MÉTODO DE JACOBI',end="\n\n")

print("Este método iterativo te cálcula la solución de un sistema de ecuaciones tomando un vector inicial.")

'''
La siguiente función en Python recibe la matriz de coeficientes  a  y el vector de constantes b  de un sistema lineal.
Adicionalmente recibe un vector inicial  x, la estimación del error   e y el máximo de iteraciones permitidas m. Esta 
función utiliza dentro de un ciclo, la función jacobi definida anteriormente. Entrega el vector x calculado y el número 
de iteraciones realizadas k. Si el método no converge, x contendrá un vector nulo.
'''

def jacobi(a,b,x): 
	n=len(x) 
	t=x.copy()
	for  i  in  range(n): 
		s=0
		for j in range(n): 
			if i!=j:
				s=s+a[i,j]*t[j]
				x[i]=(b[i]-s)/a[i,i]
	return x


def jacobim(a,b,x,e,m): 
	n=len(x)  
	t=x.copy()
	for  k  in  range(m): 
		x=jacobi(a,b,x)
		d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
		print ("Para la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(7)))+"\tError: "+str(abs(d)))
		if d<e:
			return [x,k] 
		else:
			t=x.copy() 
	return [[],m]

# Matriz a usar
A = np.array([[10,-1,2,0],
			[-1,11,-1,3],
			[2,-1,10,-1],
			[0,3,-1,8]],float)

# Vector Solución
b = np.array([[6],[25],[-11],[15]],float)

# Vector de Inicio
x=np.array([[0],[0],[0],[0]],float)

# Numéro de iteraciones
maxite=1000

print ("\nMatriz A:")
pprint.pprint(A)
print ("\nVector b:")
pprint.pprint(b)

print("")

# X es la solución y k las iteraciones
[x,k]=jacobim(A,b,x,1.e-14,maxite)

if(k==maxite):
	print("\nEl método diverge o no converge para la cota de error pedido")

else: 
	print("\nEl vector 'x' es:")
	print(x)

	print("\nEl numero de iteraciones es: "+str(k+1))