# Librerías
import numpy as np

print('MÉTODO DE GAUSS-JORDAN',end="\n\n")

print("Este método te cálcula la inversa de una matriz A")

# Inserta la matriz A
A = np.array([[4,0,0,0],
              [4,1,0,0],
              [-1,2,-1,0],
              [1,3,1,2]])

tamano = np.shape(A)
n = tamano[0]
m = tamano[1]

# Añade la matriz identidad
identidad = np.identity(n)
AI = np.concatenate((A,identidad), axis=1)
m = 2*m

# Gauss elimina hacia adelante
casicero = 1e-15
for i in range(0,n,1):
    pivote = AI[i,i]
    adelante = i+1 
    for k in range(adelante,n,1):
        if (np.abs(pivote)>=casicero):
            factor = AI[k,i]/pivote
            AI[k,:] = AI[k,:] - factor*AI[i,:]
        else:
            factor = 'Division para cero'
# Gauss-Jordan elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    # Normaliza a 1 elemento diagonal
    AI[i,:] = AI[i,:]/AI[i,i]
    pivote = AI[i,i] # uno
    # arriba de la fila i
    atras = i-1 
    for k in range(atras,0-1,-1):
        if (np.abs(pivote)>=casicero):
            factor = AI[k,i]/pivote
            AI[k,:] = AI[k,:] - factor*AI[i,:]
        else:
            factor= 'Division para cero'

inversa = AI[:,n:]

# Para verificar el resultado
verifica = np.dot(A,inversa)

# SALIDA
print('\nLa matriz inversa es:')
print(inversa)

print('\nVerificamos el método A.inversa * A debe ser Identidad: ')
print(verifica.round(7))