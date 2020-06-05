from __future__ import print_function
import numpy as np

print('MÉTODO DE POTENCIA INVERSA',end="\n\n")

print("Este método sirve para el cálculo del autovector asociado a un autovalor conocido",end="\n")


# Matriz de coeficientes ecuacion 
A = np.array([[0.7,0.3,0.1],
[0.2,0.6,0.3],
[0.1,0.1,0.6]]
)

print("La matriz de coeficientes A es \n")
print(A)


# El X(0) inicial para la iteracion 
x = np.array([[1],
             [1],
             [1]])

A_inv = np.linalg.inv(A)

print("\nMatriz A:")
print(A)
print("\nMatriz inversa de A:")
print(A_inv)   
print("\nVector x(0):")
print(x)

y=np.zeros((3,1))
y_c=np.zeros((3,1))
contador = 1    
estado=True
    
while(estado):
	y_c=y
	y=A_inv.dot(x)

	if((y.round(7)==y_c.round()).all()):
		estado=False 
		break

	print('\nIteracion '+str(contador)+':')
		
	print("\ny(",end='')
	print(contador,end='')
	print('):')
	print(y)
	
	#Obtiene el maximo valor en valor absoluto
	c=y.flat[abs(y).argmax()]
	
	print('\nc(' ,end='')
	print(contador,end='')
	print(')=',end='')
	print(c.round(7))
	x=(1/c.round(7))*y
	print("\nx(",end='')
	print(contador,end='')
	print('):')
	print(x)
	
	#Cuenta el total de iteraciones realizadas
	contador=contador+1
 
print("\nResultados para ",end='')
print(contador-1,end='')
print(' iteraciones:')
print('*Autovalor Minimo de A, λ = ', end='')
print(1/c.round(7))
print("*Autovector Asociado, v:")
print(y.round(7))
print("\nDatos para el calculo del error:\n")
e=A.dot(y)-(1/c)*y
print("<<A * v>>")
print(A.dot(y))
print("\n<<λ * v>>")
print((1/c)*y)
print("\n<<A * v - λ * v>>")
print(e)
error=np.linalg.norm(e,np.inf)
print("\nError:",end='')
print(error)



# Recomendaciones:

'''Tener en cuenta que la matriz A debe ser una matriz invertible, no singular'''