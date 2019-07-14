# Librería numpy
import numpy as np
 
def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A
 
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H
 
# Inserte la Matriz a descomponer en Q R
a = np.array((
    (16, 4, 1),
    (25, 5, 1),
    (36, 6, 1),
))

print('MÉTODO DE HOUSE HOULDER',end="\n\n")

print("Este método te descompone la matriz en dos matrices Q, R para encontrar las soluciones de manera mas sencilla",end="\n\n")
 
q, r = qr(a)
print('Matriz Q:\n', q.round(6))
print('\nMatriz R:\n', r.round(6))


print("\nPara calcular la solucion 'x' del problema, resolveremos R * x = Qt(Q transpuesta) * b",end="\n\n")

qt = np.transpose(q) # Transpuesta de una matriz

# Inserte el vector 'b'
b = np.array(
    (2, 5, 9)
)

print('Matriz Q transpuesta:\n', qt.round(6))
print('\nVector b:\n', b.round(6))

x = np.linalg.solve(r, qt @ b) # Desarrollo del sistema R * x = Qt(Q transpuesta) * b

print("\nSolucion de 'x':",x.round(6), end="\n\n")