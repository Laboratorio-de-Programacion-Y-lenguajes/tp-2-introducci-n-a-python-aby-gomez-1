# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: 
Gemini
**Prompt usado**:
> Patron Tutor
>Actúa como un tutor experto en Python 3.13. Mi objetivo es resolver un ejercicio de programación para aprender los fundamentos por mi cuenta.

>Reglas estrictas:

>No me entregues el código completo de la solución bajo ninguna circunstancia.

>Si te presento un error de sintaxis, explica por qué ocurre y dame un ejemplo genérico similar, pero no corrijas mi función directamente.

>Si no sé cómo avanzar, hazme preguntas que me ayuden a razonar la lógica (loops, condicionales, etc.).

>Valida mi razonamiento y señala errores conceptuales de forma directa y técnica.

**Resultado obtenido**:
Tests ok

**¿Lo usaste tal cual o lo modificaste?**
Solo lo use para consultas de sintaxis

---

### 2 - condicionales.py

**Herramienta**: 

**Prompt usado**:
Se utilizo el mismo promt que el anterior

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 3 - listas.py

**Herramienta**:
Gemini
**Prompt usado**:
> Patrón: Verificador Cognitivo / Tutor Técnico

>"Actúa como un revisor de código experto en Python 3.13. Estoy trabajando con manipulación de listas y necesito razonar la lógica de 5 funciones sin que me des el código final.

>Tareas a discutir:

>Para invertir_lista: Explícame la diferencia técnica entre usar el método .reverse() y el slicing [::-1], específicamente respecto a la mutabilidad de la lista original.

>Para eliminar_duplicados: ¿Cómo puedo mantener el orden de aparición sin usar un simple set() (que desordena los elementos)? Explícame la lógica de usar una estructura auxiliar.

>Para aplanar_lista: Explícame conceptualmente cómo funciona un 'nested loop' (bucle anidado) para extraer elementos de sublistas.

>Análisis de casos borde: Enumera qué debería retornar cada función si recibe una lista vacía [].

>Regla de oro: No escribas las funciones. Si te propongo una línea de código, analiza si es eficiente o si viola la regla de 'no modificar la lista original' cuando el docstring lo prohíbe."

**Resultado obtenido**:
Todo ok

**¿Lo usaste tal cual o lo modificaste?**
Ejercicio 1 : 
Mi propuesta inicial
>  total: float = 0
 >   for num in numeros:
 >        total += num
  >  return total

Gemini sugiere cambiar el for por sum por eficiencia y al estar implementada en c es mas rapida, tambien declarar la variable como int en vez de float para un retorno dinmaico ya que python convierte automaticamente a float si encuentra un decimal. 
Decidi no utilizar sum() porque no tiene en cuenta el caso de una lista de strings, dando un error de ser esta.

Para el resto de ejercicios fue de consulta de metodos que se usan en listas y demás
https://gemini.google.com/share/c9024c7795bf
---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> > Patrón: Interacción Invertida / Tutor Técnico
>"Actúa como un tutor de Python 3.13. Necesito resolver 4 funciones sobre diccionarios: contar_palabras, invertir_diccionario, merge_diccionarios y filtrar_por_valor.

>Instrucciones de interacción:

>No escribas el código de las funciones.

>Primero, explícame conceptualmente cómo se accede a las claves y valores en Python y cuál es la diferencia técnica entre usar d[clave] y d.get(clave).

>Para la función de contar_palabras, hazme 2 preguntas sobre cómo debería normalizar el texto antes de contar para evitar duplicados por mayúsculas o espacios.

>Para invertir_diccionario, explícame qué pasaría si el diccionario original tiene dos claves distintas con el mismo valor (ej: {'a': 1, 'b': 1}).

>Una vez que te responda, valida si mi razonamiento es correcto y, si tengo errores de sintaxis en mis propuestas, señálalos directamente sin darme la solución corregida."

**Resultado obtenido**:
tests ok

**¿Lo usaste tal cual o lo modificaste?**
https://gemini.google.com/share/09ff0253d891

---

### 5 - loops.py

**Herramienta**: 
Gemini
**Prompt usado**:
> Actúa como un verificador de lógica de algoritmos en Python 3.13. Estoy diseñando funciones para trabajar con bucles (loops) y necesito tu análisis técnico antes de codear.Mis objetivos son:Implementar es_primo(n) de forma eficiente. ¿Cuál es el límite matemático óptimo para el rango del bucle y por qué no debería iterar hasta n?Implementar fibonacci(n) devolviendo una lista. Explícame el concepto de 'asignación múltiple' en Python ($a, b = b, a + b$) y cómo ayuda a simplificar este algoritmo.Para suma_digitos(n), compárame la eficiencia de usar un bucle sobre el string del número vs. usar operadores aritméticos (// y %).Regla: No generes el código completo. Explícame los conceptos y enumera los casos borde (como n=0 o n=1) que mis tests deberían cubrir

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> Patrón: Reflexión / Análisis de Flujo

>"Actúa como un mentor de programación funcional en Python 3.13. Necesito razonar la lógica de 4 funciones de orden superior: aplicar_funcion, componer, memoizar y reducir.

>Instrucciones de guía:

>No generes el código.

>Para aplicar_funcion, explícame cómo pasar una función como argumento (callback) y cómo se diferencia de llamar a la función inmediatamente.

>En componer, explícame el concepto de 'clausura' (closure) y cómo puedo definir una función interna que capture los argumentos f y g para ejecutarlos después.

>Para memoizar, descríbeme el flujo lógico: ¿Qué debe verificar la función interna en el diccionario cache antes de ejecutar func? ¿Cómo se guardan los resultados para futuras llamadas?

>En reducir, ayúdame a visualizar el proceso paso a paso (acumulación): ¿Cómo se actualiza el valor 'inicial' en cada iteración de la lista?

>Si te presento un borrador de código, analiza si estoy respetando el ámbito de las variables (scopes) y si la lógica de retorno es correcta."

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
