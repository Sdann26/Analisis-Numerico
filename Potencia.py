import numpy as np
from scipy import linalg

print('MÉTODO DE POTENCIAS',end="\n\n")

print("Este método iterativo cálcula sucesivas aproximaciones a los autovectores y autovalores de una matriz",end="\n")

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

ya=np.zeros((3,1))
yp=np.zeros((3,1))
print("\nEl valor de x(0)")
print(x)
print("\n")
i=1
estado=True


while(estado):
		ya=yp
		yp=A.dot(x)

		if((yp.round(7)==ya.round(7)).all()):
			estado=False
			break

		print("Iteracion "+str(i)+":")

		print("El y("+str(i)+") es")
		print(yp)
		domin=yp.flat[abs(yp).argmax()]
		print("\nEl componente dominante es ="+str(domin.round(7))+"\n")
		x=(1/domin.round(7))*yp
		print("El x("+str(i)+") es")
		print(x)
		print("\n")
		i=i+1


print("La solución del valor propio de A es: λ = "+str(domin.round(7)))
print("El vector propio asociado es:\n"+str(np.array(yp)))

print("\nDatos para el calculo del error:")
e=A.dot(yp)-(domin)*yp
print("\nA * x")
print(A.dot(yp))
print("\nλ * x")
print((domin)*yp)
print("\nA * x - λ * x")
print(e)
error=np.linalg.norm(e,np.inf)
print("\nError:")
print(error)
	