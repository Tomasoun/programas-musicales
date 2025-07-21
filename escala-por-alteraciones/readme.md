# 🎹 Identificador de Escalas Mayores por Alteraciones

Este programa en Python permite reconocer en qué escala mayor te encontrás al ingresar la cantidad de alteraciones en la armadura (sostenidos `#` o bemoles `b`).  
Un asistente perfecto para estudiantes de teoría musical, compositores y curiosos del lenguaje tonal.

##  ¿Qué hace?

- Recibe un input como `3#` o `1b`
- Identifica si se trata de sostenidos o bemoles
- Devuelve el nombre de la escala mayor correspondiente
- Utiliza un bucle `while` para permitir múltiples consultas
- Realiza validaciones para entradas fuera de rango o formato incorrecto

##  Ejemplos de uso
Ingrese alteración (ej: 2#, 3b) o 'salir': 3#
🔎 3 sostenido(s) → La mayor
Ingrese alteración (ej: 2#, 3b) o 'salir': 1b
🔎 1 bemol(es) → Fa mayor

##  Estructura técnica

- Uso de `while True` para mantener el programa activo
- Uso de `if / else` para controlar decisiones según el input
- Diccionarios como mapas de equivalencia entre cantidad de alteraciones y escalas
- Validación de formato con `isdigit()` y análisis de caracteres

##  Educación aplicada

Las alteraciones armónicas en clave permiten identificar rápidamente la tonalidad de una obra. Este programa traduce la cantidad de signos en la armadura a una escala específica, replicando la lógica usada en lectura de partituras.

##  Ideas para expansión

- Visualización de la armadura con notas alteradas
- Inclusión de escalas menores relativas
- Versión en GUI con selección tipo desplegable
- Agregar sonido o teclado virtual (como en tus otros proyectos)

