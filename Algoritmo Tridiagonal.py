def MeThomas(a, b, c, d):
    n = len(d)  # número de filas

    # Modifica los coeficientes de la primera fila
    c[0] /= b[0]  # Posible división por cero
    d[0] /= b[0]

    # Sustitución de coeficientes
    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i-1])
        c[i] /= ptemp
        d[i] = (d[i] - a[i] * d[i-1])/ptemp

    # Sustitución hacia atrás
    x = [0 for i in range(n)]
    x[-1] = d[-1]


    # Aplicacion Gaussiana
    for i in range(-2, -n-1, -1):
        x[i] = d[i] - c[i] * x[i+1]

    return x
# La Matriz a usar es:  [2.04,-1,0,0,0 ]
#                       [-1,2.04,-1,0,0]
#                       [0,-1,2.04,-1,0]
#                       [0,0,-1,2.04,-1]
#                       [0,0,0,-1,2.04 ]

# El Vector Solución:   [40.8,0.8,0.8,200.8,0]

A = [0,-1,-1,-1,-1]
B = [2.04,2.04,2.04,2.04,2.04]
C = [-1,-1,-1,-1,0]
D = [40.8,0.8,0.8,200.8,0]

Sol = MeThomas(A,B,C,D)

print ("La Solución es: "+str(Sol))