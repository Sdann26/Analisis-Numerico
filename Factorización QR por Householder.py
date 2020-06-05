# Librerías
from  time  import*
import numpy as np
 
def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        print("Usamos la matriz H"+str(i+1)+": \n"+str(H),end="\n\n")
        Q = np.dot(Q, H)
        print("Formamos la matriz Q:\n"+str(Q),end="\n\n")
        A = np.dot(H, A)
        print("Formamos la matriz R:\n"+str(A),end="\n\n")
    return Q, A
 
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H
 
# Inserte la Matriz a descomponer en Q R
'''A = np.array((
    (9, 3, 1),
    (16, 4, 1),
    (25, 5, 1),
))'''
'''
A = np.array((
    (1,2,0,0,0),
    (4,5,6,0,0),
    (0,5,6,4,0),
    (0,0,4,7,8),
    (0,0,0,4,8)
    ))
'''
A = np.array((
    (10, 1, 1, 1),
    (2, 10, 1, 1),
    (1, 1, 10, 1),
    (1, 1, 1, 10)
))

print('MÉTODO DE HOUSE HOULDER',end="\n\n")

print("Este método te descompone la matriz en dos matrices Q, R para encontrar las soluciones de manera mas sencilla mediante el uso de reflexiones de Householder",end="\n\n")

t1=perf_counter(); #Calcula tiempo inicio del algoritmo
q, r = qr(A)
t2=perf_counter(); #Calcula tiempo final del algoritmo

print("Al finalizar el algoritmo tendremos:\n")
print('Matriz Q:\n', q.round(7))
print('\nMatriz R:\n', r.round(7))


print("\nPara calcular la solucion 'x' del problema, resolveremos R * x = Qt(Q transpuesta) * b",end="\n\n")

qt = np.transpose(q) # Transpuesta de una matriz

# Inserte el vector 'b'
'''b = np.array(
    (3,4,5,6,7)
    )
'''
b = np.array(
    (1, 1, 1, 1)
    )
'''
b = np.array(
    (0, 2, 5)
)'''
'''b = np.array(
    (15, 15, 15, 15, 15, 15, 15, 15, 12, 4, 8, 16)
)'''

print('Matriz Q transpuesta:\n', qt.round(7))
print('\nVector b:\n', b.round(7))

# Para matrices nxn
x = np.linalg.solve(r, qt @ b) # Desarrollo del sistema R * x = Qt(Q transpuesta) * b

print("\nSolucion de 'x':",x.round(7), end="\n")

'''# Para matrices mxn
s = qt @ b

print("\nCalculamos qt * b:",s.round(6), end="\n")'''

# Recomendaciones:

'''Para terminar esta matriz se recomienda pasarla a una matriz nxn dado que la matriz R tendra filas
con puros valores 0 y el vector qt * b tendra valores 0'''

print("\nEl tiempo de ejecución es: "+str(t2-t1))

R = x - np.linalg.solve(A,b)

print("\nLa calidad de la solución es:\n")
print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))