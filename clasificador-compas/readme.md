#  Clasificador de Compases Musicales

Este programa en Python permite identificar el tipo y tamaño de un compás según su cifra rítmica (ej. 2/4, 6/8, 3/2). Ideal para músicos, estudiantes y programadores con ritmo.

##  ¿Qué hace?

- Recibe una cifra como `"6/8"`  
- Determina si el compás es **Binario simple**, **Ternario**, **Compuesto** o **Irregular**
- Traduce la cifra a tamaño de compás con figuras musicales (ej. “seis corcheas”, “tres blancas”)

##  Conceptos utilizados

- `input()` para capturar cifras
- `if / elif / else` para tomar decisiones
- Separación de datos con `.split("/")`
- `int()`, `print()`, operaciones básicas
- Lógica musical rítmica aplicada a programación

##  Ejemplo de uso

Ingrese una cifra de compás (ej: 3/4, 6/8, 2/2): 6/8
  Compás: 6/8
  Tipo: Compuesto
  Tamaño: 6 corchea


##  Propuestas futuras

- Clasificación por género musical (ej. folclore, jazz, clásica)
- Visualización de pulsos con arte ASCII o animación
- Interfaz interactiva con `tkinter`
- Exportación del análisis como texto educativo

---

