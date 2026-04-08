# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
   
    limpio = texto.replace(" ", "").lower()
    
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    return " ".join(palabra.capitalize() for palabra in texto.split())


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiouAEIOU"
    return sum(1 for char in texto if char in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = []
    for char in texto:
        if char.isalpha():
            # Determinar base ASCII (65 para 'A', 97 para 'a')
            base = ord('A') if char.isupper() else ord('a')
            # Fórmula: (posición_actual + despl - base) % 26 + base
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado.append(nuevo_char)
        else:
            resultado.append(char)
    return "".join(resultado)
