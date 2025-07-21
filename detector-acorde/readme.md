# Detector de Acordes por Notas

Este script permite ingresar un conjunto de notas musicales (como `C E G`) y detectar automáticamente la especie del acorde: mayor, menor, disminuido, aumentado, etc. Una herramienta simple para la armonía programada.

## ¿Cómo funciona?

1. El usuario ingresa las notas separadas por espacio.
2. Se comparan sus intervalos respecto a la nota raíz.
3. El programa reconoce la especie del acorde usando fórmulas predefinidas.

## Acordes reconocidos

- Mayor: `[0, 4, 7]`
- Menor: `[0, 3, 7]`
- Disminuido: `[0, 3, 6]`
- Aumentado: `[0, 4, 8]`
- Quinta justa (power chord): `[0, 7]`

## Tecnologías y conceptos

- Listas, diccionarios, operadores y lógica musical
- Entrada por `input()` y validación con `all()`
- Intervalos relativos en una escala cromática

## Ejemplo de uso

Ingrese las notas separadas por espacio (ej: C E G):
→ Acorde: C-E-G
→ Intervalos: [0, 4, 7]
→ Especie: Acorde Mayor

## Ideas para expansión

- Soporte para acordes con séptimas, novenas y inversiones
- Integración con sonido (`numpy`, `sounddevice`)
- Interfaz gráfica con teclado visual 🎹

---

*Una fusión de lógica y música hecha en Python.* 🧬🎶