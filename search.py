# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """

    result=-1
    for i in range(len(lst)):
        if lst[i]==target:
            if result == -1:
                result = i
    return result



def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    contador=0
    result = -1
    for i in range(len(lst)):
        if contador>= start:
         if lst[i] == target:
            if result==-1:
             result = i
            contador+=1

        else:
            contador+=1
    return result


def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    result = -1
    for i in range(len(lst)):
        if lst[i] == "":
            if result==-1:
             result = i
    return result

colors =   ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors))
#print(index_of_by_index("Black", colors, 1))