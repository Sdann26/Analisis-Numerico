import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

#--------------------------  N E W T O N  -----------------------------------------
def coef_Newton(x_0,y_0,verbose=False):
    if verbose:
        print("INTERPOLACIÓN POLINÓMICA DE NEWTON\n")
        print("Este metodo genera una funcion P_n(x) representando al polinomio interpolado por Newton \n")
        print("Se usara los datos de \'x\':", x_0)
        print("Se usara los datos de \'y\':", y_0)

    x = np.copy(x_0)
    y = np.copy(y_0)
    n = np.shape(x_0)[1]
    a = np.zeros(n*n).reshape(n,n)
    for i in range(n):
        a[i,0] = y[0,i]

    for j in range(1,n):
        for i in range(0,n-j):
            a[i,j] = (a[i+1,j-1]-a[i,j-1])/(x[0,i+j] - x[0,i])
    
# ---- Mostrar data frame-----------
    name_col = ['x_k', 'y_k']   
    index = ['k_0']
    data = []
    for fil in range(n):
        if fil < n-1 : 
            name_col.append(f'D.D. Orden {fil+1}')
            index.append(f'k_{fil+1}')
        lst = [x[0][fil]]
        for j in range(n):
            if j < fil+1:
                i = fil-j
                lst.append(a[i,j])
            else: lst.append(' ')
         
        data.append(lst)
    df = pd.DataFrame(data,columns = name_col, index=index)
    line = '----------------------------------------'
    print(f'\n{line}\n\tData Frame - Metodo Newton\n{line}\n\n{df}')
        
    return a

def solve_Pol_Newton(a_0,x_0,pto):
    a = np.copy(a_0)
    x = np.copy(x_0)
    n = len(a)
    line = '------------------------------------------'
    eval = 0
    for i in range(0,n):    
        temp = 1
        for j in range(0,i):
            temp = temp*(pto-x[0,j])
        
        temp = temp*a[i]
        eval = eval + temp  
    print("\nFinalmente, P_{}({}) : {}\n{}".format(n,pto, eval,line))
    return eval


if __name__ == '__metodos_Iterpolacion' :
    print("__metodos_Interpolacion se ha importado correctamente.")


if __name__ == '__main__':

    #-------------- N E W T O N -------------------------
    t = np.array([0, 0.5, 1, 2, 3, 5, 9, 15],dtype=float).reshape(1,8)
    Cb = np.array([100, 42, 14, 7.5, 0.4, 0.11, 0.05, 0.002],dtype=float).reshape(1,8)
    
    #Imprimir como la tabla como data frame
    Matriz = coef_Newton(t,Cb,True)
    #La diagonal es la primera fila
    diag = Matriz[0,:]
    """Tener en cuenta que los coeficientes son desde el termino independiente hasta el coeficiente de grado mayor de izquierda a derecha"""
    print(f"\nCOEFICIENTES DEL POLINOMIO:\n{diag}")
    sol = solve_Pol_Newton(diag,t,5.5)