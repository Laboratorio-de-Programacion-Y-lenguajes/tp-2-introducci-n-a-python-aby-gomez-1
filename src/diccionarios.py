# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """
    texto = texto.split()#sin argumentos elimina cualquier cantidad de espacios en blanco y los extremos
    frecuencia_palabras = {}

    for palabras in texto:
        palabras = palabras.lower()
        if palabras not in frecuencia_palabras:
            frecuencia_palabras[palabras] = 1
        else:
            valor = frecuencia_palabras.get(palabras) +1
            frecuencia_palabras[palabras] = valor 
    return frecuencia_palabras


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
    """
    nuevo_dic : dict = {}
    for clave,valor in d.items():
        nuevo_dic[valor] = clave
    
    return nuevo_dic


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    return d1 | d2


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    nuevo_dic : dict = {}
    for clave,valor in d.items():
        if valor>=minimo:
            nuevo_dic[clave] = valor

    return nuevo_dic
