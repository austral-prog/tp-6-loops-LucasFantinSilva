# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
        Retorna la cantidad de pasos necesarios para llegar a 1
        siguiendo la conjetura de Collatz:
          - Si n es par: n = n // 2
          - Si n es impar: n = 3 * n + 1

        n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

        Ejemplo: collatz_steps(6) -> 8
          6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
        """
    steps=0
    if n==1:
        return 0
    else:
     while n!=1:
       if n%2==0:
        steps+=1
        n=n//2
       else:
         n= 3*n+1
         steps+=1
     return steps


def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    if n==1:
        return [1]
    else:
        lst=[]
        while n != 1:
            if n % 2 == 0:
                lst.append(n)
                n = n // 2
            else:
                lst.append(n)
                n = 3 * n + 1

        lst.append(1)
        return lst


print(collatz_steps(6))