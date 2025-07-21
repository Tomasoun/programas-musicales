#  Clasificador de Modos Gregorianos

Este programa en Python analiza los datos de una escala musical (nombre, cantidad de tonos, semitonos y nota inicial) y determina si corresponde a un modo gregoriano tradicional. Además, clasifica su especie como **Mayor**, **Menor** o **Exótica** si no coincide con ningún modo estándar.

##  ¿Cómo funciona?

- Recibe entrada por consola:
  - 📖 Nombre de la escala (ej: Dórico, Frigio...)
  - 🔢 Cantidad de tonos (`int`)
  - 🔬 Cantidad de semitonos (`float`)
  - 🎹 Si comienza en la nota "Do" (`booleano`)
- Verifica si corresponde con alguno de los modos definidos
- Imprime un reporte clasificatorio en consola

##  Ejemplo de uso

Ingrese el nombre del modo (ej: Dórico, Locrio, etc.): Frigio
Ingrese cantidad de tonos enteros: 5
Ingrese cantidad de semitonos: 2
¿Comienza en Do? (s/n): s
📄 Clasificación de modo musical
Nombre ingresado: Frigio
Tonos: 5 | Semitonos: 2
¿Comienza en Do? Sí
🎶 Modo reconocido: Frigio (Menor)

##  Tipos de datos aplicados

- `str` → nombre de la escala
- `int` → cantidad de tonos
- `float` → cantidad de semitonos
- `bool` → nota inicial ("Do")
- `dict` → definición interna de modos
- `function` → lógica encapsulada en `clasificar_modo()`

##  Modo gregoriano en contexto

Los modos como Jónico, Dórico o Frigio tienen raíces en la música medieval y constituyen la base teórica de muchas escalas actuales. Este programa ayuda a identificarlos desde una perspectiva computacional.

##  Ideas para expansión

- Validación más profunda de las notas reales que integran la escala
- Inclusión de modos modernos y escalas exóticas
- Interfaz gráfica con selectores desplegables
- Representación visual en pentagrama o teclado

---



