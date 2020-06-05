# Librería numpy
import numpy as np
from  time  import*
import matplotlib.pyplot as plt

gx=[]
gy=[]

print('MÉTODO DE LA SECANTE',end="\n\n")

print("Este método se basa en el método de Newton con diferencia que al tomar la derivada lo toma como su teorema fundamental.\n")

def secante(x0,x1,f,maxiter,tol):

	for n in range(maxiter):
		y = x1
		x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
		gy.append(x)
		gx.append(n+2)
		print ("Para la iteración "+str(n+2)+": X = "+str("{:10.10f}".format(x))+"\tError: "+str(abs(x-y)))
		if (abs(x-y)<=tol):
			grafico(gx,gy)
			return [x,n]
		x0=x1
		x1=x
	return [x,999999]

def grafico (x,y):
    plt.plot(gx,gy,'r')
    plt.title('Método de la Secante')
    plt.xlabel("Numéro de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

# Defina la función a usar
def f(x): return x**3 + 4*x**2 - 10

# Punto Xo
X0 = 1
gy.append(X0)
gx.append(0)

# Punto X1
X1 = 1.1
gy.append(X1)
gx.append(1)

# Numéro de iteraciones
maxite=20



print("Tenemos la funcion f(x) = x^3 + 4*(x^2) - 10\n")

print("Iniciamos con un valor Xo = ",str(X0)," y con el valor X1 = ",str(X1),"\n")

# Poner la cota de error de la raíz
tol = 1.0e-8

[x,k] = secante(X0, X1, f, maxite, tol) 

if k==999999:
	print("El método diverge o no converge para la cota de error pedido")

else:
	print("\nLa raíz buscada es: "+str(x))