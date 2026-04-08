# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    x: int = 0
    if n>0:
     return [x := x + 1 for i in range(n)]
    else:
        return [x := x - 1 for i in range(abs(n))]



def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    multiplos: int = 1
    lista:list = []
    while multiplos <= 10:
        lista.append(n*multiplos)
        multiplos += 1
    return lista




def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    suma_total:int = 0
    n = abs(n)#para el caso si n es negativo

    while n > 0:
         
        suma_total+= n%10
        n= n//10
    return suma_total

def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    

    if n < 2:
        return False
    
    # Se busca un divisor en el rango [2, sqrt(n)]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    secuencia = [0, 1]
    
    # Se itera desde el índice 2 hasta n-1
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]#-1 ultimo -2 penultimo
        secuencia.append(siguiente)
        
    return secuencia
    
