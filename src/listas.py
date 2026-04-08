# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    total: int = 0
    for num in numeros:
         total += num
    return total


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    lista_pares: list = []

    for num in numeros:
        if(num%2==0):
            lista_pares.append(num)

    
    return lista_pares


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    return lista[::-1] #reverse modifica el objeto y devuelve None
 #slicing [inicio(no hay nada asume 0):final(no hay nada asume final de la lista):intervalo entre elementos]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    lista_sin_duplicados: list = []
    for l in lista : 
        if l not in lista_sin_duplicados: #in equivalente a un contains() en java
            lista_sin_duplicados.append(l)
        
    return lista_sin_duplicados


 


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    lista_aplanada: list = []

    for elemento in lista:
        for e in elemento:
            lista_aplanada.append(e)

    return lista_aplanada
