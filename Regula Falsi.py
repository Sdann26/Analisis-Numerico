# Librería numpy
import numpy as np
from  time  import*
import matplotlib.pyplot as plt

gx=[]
gy=[]

print('MÉTODO DE LA FALSA PROPOSCIÓN',end="\n\n")

print("Este método utiliza como base el método de la secante junto al de bisección para sus iteraciones.\n")

def RegulaFalsi(x0,x1,f,maxiter,tol):
	x2 = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
	i=1
	print ("Para la iteración "+str(i-1)+": X = "+str("{:10.10f}".format(x2)))

	while (i<=maxiter) and abs(x2-x1)>tol:
		i = i + 1
		if f(x1)*f(x2)<0:
			xo=x1
		x1=x2
		x2 = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
		gx.append(i)
		gy.append(x2)
		print ("Para la iteración "+str(i-1)+": X = "+str("{:10.10f}".format(x2))+"\tError: "+str(abs(x2-x1)))
	if abs(x2-x1)<tol:
		grafico(gx,gy)
		return [x2,i]
	else:
		return [x2,99999999]

def grafico (x,y):
    plt.plot(x,y,'r')
    plt.title('Método de la Falsa Proposición')
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
X1 = 2
gy.append(X1)
gx.append(1)

# Numéro de iteraciones
maxite=20


print("Tenemos la funcion f(x) = x^3 + 4*(x^2) - 10\n")

print("Iniciamos con un valor Xo = ",str(X0)," y con el valor X1 = ",str(X1),"\n")

# Poner la cota de error de la raíz
tol = 1.0e-8

[x,k] = RegulaFalsi(X0, X1, f, maxite, tol) 

if k==99999999:
	print("El método diverge o no converge para la cota de error pedido")

else:
	print("\nLa raíz buscada es: "+str(x))