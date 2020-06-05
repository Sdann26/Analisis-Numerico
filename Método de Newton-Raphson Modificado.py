# Librería numpy
import numpy as np
from  time  import*
import matplotlib.pyplot as plt

gx=[]
gy=[]


print('MÉTODO NEWTON-RAPHSON MODIFICADO',end="\n\n")

print("Este método es una modificación basa en el metodo de Newton-Raphson usando además una segunda derivada que ayuda en el manejo de funciones con varias raices.")

def newton_rapshon_method(x,f,df,ddf,maxiter,tol):

	for n in range(maxiter):
		y = x
		x = x - f(x)*df(x)/(df(x)**2-f(x)*ddf(x))
		gy.append(x)
		gx.append(n+1)
		print ("Para la iteración "+str(n+1)+": X = "+str("{:10.10f}".format(x))+"\tError: "+str(abs(x-y)))
		if (abs(x-y)<=tol):
			grafico(gx,gy)
			return [x,n]
	return maxiter

def grafico (x,y):
    plt.plot(gx,gy,'r')
    plt.title('Método de Newton-Raphson Modificado')
    plt.xlabel("Numéro de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

# Defina la función a usar
def f(x): return x ** 2 - 1

# Defina la derivada de la función a usar
def df(x): return 2 * x

# Defina la derivada de la función a usar
def ddf(x): return 2 

# Punto Xo
Xo = 5
gy.append(Xo)
gx.append(0)

# Numéro de iteraciones
maxite=50


print("Tenemos la funcion f(x) = x^2 - 1\n")

print("Iniciamos con un valor Xo = ",str(Xo),"\n")

# Poner la cota de error de la raíz
tol = 1.0e-8

[x,k] = newton_rapshon_method(Xo,f,df,ddf,maxite,tol) 

if k==maxite:
	print("El método diverge o no converge para la cota de error pedido")

else:
	print("\nLa raíz buscada es: "+str(x))