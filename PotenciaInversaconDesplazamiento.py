from __future__ import print_function
import numpy as np
import sys

print('MÉTODO DE POTENCIA INVERSA CON DESPLAZAMIENTO',end="\n\n")

print("Este método sirve para proximar un valor propio λ y un vector propio asociado a partir de una estimación λ¯ a λ.",end="\n")

'''
Si no te dan el valor de lambda, puedes elegir uno tu mismo.
'''

#Matriz A 
A = np.array([[0.7,0.3,0.1],
[0.2,0.6,0.3],
[0.1,0.1,0.6]]
)

# Lambda aproximado 
lamb = 0.3

#C = A - λ * I
C = A - lamb * np.eye(3)

# Matriz inversa de C
C_inv = np.linalg.inv(C)


x = np.array([[5],
             [1],
             [1]])
print("\nMatriz C:")
print(C)
print("\nMatriz C inversa:")
print(C_inv)   
print("\nVector x(0):")
print(x)
y=np.zeros((3,1))
y_c=np.zeros((3,1))
contador = 1    
estado=True

c0 = 99999
    
while(estado):
	y_c=y
	y=C_inv.dot(x)


	c=y.flat[abs(y).argmax()]

	if(abs((1/c)-(1/c0)) < 1.0e-6):
		estado=False 
		break

	c0 = c	

	print('\nIteracion '+str(contador)+':')
	print("\ny(",end='')
	print(contador,end='')
	print('):')
	print(y)
	print('\nc(' ,end='')
	print(contador,end='')
	print(')=',end='')
	print(c.round(7))
	x=(1/c)*y
	print("\nx(",end='')
	print(contador,end='')
	print('):')
	print(x)
	contador=contador+1

print("\nResultados para ",end='')
print(contador-1,end='')
print(' iteraciones:')
print('*Autovalor de A, λ = ', end='')
lamb= 1/c0.round(7) + lamb
print(lamb.round(7))
print("*Autovector Asociado, v:")
print(x)
print("\nDatos para el calculo del error:")
e=A.dot(x)-(lamb)*x
print("<<A * v>>")
print(A.dot(x))
print("\n<<λ * v>>")
print((lamb)*x)
print("\n<<A * v - λ *v>>")
print(e)
error=np.linalg.norm(e,np.inf)
print("\nError:",end='')
print(error)
