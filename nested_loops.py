# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    result=[]
    for lst in matrix:
        for i in lst:
            result.append(i)

    return result



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    result = []
    for lst in matrix:
        t=0
        for i in lst:
            t+=i
        result.append(t)
        t=0
    return result

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    one=0
    two=0
    three=0
    for lst in matrix:
        one+=lst[0]
        two+=lst[1]
        three+=lst[2]

    result=[one,two,three]
    return result
a=col_sums([[1, 2, 3], [4, 5, 6]])
print(a)