# Librerías numpy y scipy
from  time  import*
import numpy as np
import pprint
import scipy
import scipy.linalg  

print('MÉTODO LDU CON PIVOTEO',end="\n\n")

print("Este método te halla las matrices L, U y P y cálcula la solución del sistema L * U * X = P * b. Siendo L * U = P * A.\n")

# Coloca la matriz A:
A = np.array([[5,1,-2,0],
			[1,2,0,0],
			[-2,0,4,1],
			[0,0,1,3]],float) 
'''
A=np.array([[1,1,0,-1,0],[1,0,0,0,-1],[4,4,1,-2,-4],[0,1,0,0,-2],[0,0,2,0,0]],float)

'''

# Coloca el vector solución b:
b=np.array([100,150,100,0],float)
'''
b=np.array([0,2,8,0,4],float)
'''

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
# Función LU, aquí se inserta la matriz y su tamaño
P, L, U = scipy.linalg.lu(A)
t2=perf_counter(); #Calcula tiempo final del algoritmo

A = np.array(A,float)
P = np.array(P,float)
L = np.array(L,float)
U = np.array(U,float)

# Calculo de la matriz D
n = A.shape

D = np.zeros((n[0], n[0]))

for i in range(n[0]):
	D[i][i] = U[i][i]
	
for i in range(n[0]):
	for j in range(n[0]):
		U[i][j] = U[i][j]/D[i][i]



print ("Matriz A:")
pprint.pprint(A)
print ("Matriz P:")
pprint.pprint(np.linalg.inv(P))
print ("Matriz L:")
pprint.pprint(L)
print ("Matriz D:")
pprint.pprint(D)
print ("Matriz U:")
pprint.pprint(U)
print("\nVector solución b: \n"+str(b))

print("\nPrimero, resolvemos L * Z =  P * b:")
L = np.dot(P,L)
z = np.linalg.solve(L,b)
print("La solución Z es:\n" +str(z))

print("\nLuego desarrollamos D * Y = Z:")
y = np.linalg.solve(D,z)
print("La solución Y es: \n"+str(y))

print("\nLuego desarrollamos U * X = Y:")
x = np.linalg.solve(U,y)
print("La solución X es: \n"+str(x))

print("\nEl tiempo de ejecución es: "+str(t2-t1))

R = x - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))