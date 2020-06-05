# Librería numpy
import numpy as np
from  time  import*

print('NUMÉRO DE CONDICIÓN',end="\n\n")

print("Este algoritmo te permite hallar el numero de condición de una matriz ya sea por su norma infinita o por su norma 1")

# Coloca la matriz A:
A = np.array([[1,1,1,1],
			[8,4,2,1],
			[3,2,1,0],
			[12,2,0,0]],float)
print("\nLa matriz A es:\n"+str(A))

print("\nLa matriz A inversa es:\n"+str(np.linalg.inv(A)))

# Para norma infnita
n=np.linalg.norm(A,np.inf)
print("\nLa matriz A tiene por norma infinita: "+str(n))
m=np.linalg.norm(np.linalg.inv(A),np.inf)
print("La matriz A inversa tiene por norma infinita: "+str(m))
c=np.linalg.cond(A,np.inf)
print("Tiene como número de condición: "+str(c))

# Para norma 1
n=np.linalg.norm(A,1)
print("\nLa matriz A tiene por norma 1: "+str(n))
m=np.linalg.norm(np.linalg.inv(A),1)
print("La matriz A inversa tiene por norma 1: "+str(m))
c=np.linalg.cond(A,1)
print("Tiene como número de condición: "+str(c))