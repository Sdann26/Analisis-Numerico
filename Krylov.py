import sympy as sp
import numpy as np

print('MÉTODO DE KRYLOV',end="\n\n")

print("Este método sirve para hallar el polinomio característico asociado a una matriz",end="\n")

x=sp.symbols('x')
print("\nUtilizando el método de Krylov para hallar el polinomio característico de la matriz: ")
print("Primero ingresamos la matriz A: ")
A=np.array([[0.7, 0.3, 0.1],
            [0.2, 0.6, 0.1],
            [0.1, 0.1, 0.6]])
print(A)
n=A.shape[0]
Ab=np.identity(n)
def krylov(A,n,Ab):
    m=A.shape[0]
    if n==1:
        b=np.zeros((m,1),)
        b[0,0]=1
        Ab[:,m-1]=b[:,0]
        return A@b
    else:
        Ab[:,m-n]=krylov(A,n-1,Ab)[:,0]
        return A@krylov(A,n-1,Ab)
b=-krylov(A,n,Ab)
print("\nSiendo b:\n",b)
coef=np.linalg.inv(Ab)@b
print("\nHallando los coeficientes:",coef)
print("\nCalculando A*b")
print(Ab)
pol= pow(x,n)
for i in range(n):
    pol= pol + coef[i,0]*pow(x,n-i-1)
print("\nEl polinomio característico de la matriz es: ",end="")
print(pol)
