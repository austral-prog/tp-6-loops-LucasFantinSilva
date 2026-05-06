# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    contador = 0
    nuevaLst = []
    for i in range(len(lst)):
        if lst[i] != "":
            nuevaLst.append(f"{contador}. {lst[i]}")
            contador = contador + 1

    return nuevaLst

def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    contador = 0
    nuevaLst = []

    for i in range(len(lst)):
        if lst[i] != "":
            word = lst[i]
            back = word[::-1]
            nuevaLst.append(f"{contador}. {back}")
            contador = contador + 1
    return nuevaLst

lista=["Red", "Green", "", "White"]
print(enumerate_list(lista))
print(enumerate_backwards(lista))