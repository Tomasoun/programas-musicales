# Diccionario de modos gregorianos
modos_gregorianos = {
    "jónico": {"tonos": 5, "semitonos": 2, "mayor": True},
    "dórico": {"tonos": 5, "semitonos": 2, "mayor": False},
    "frigio": {"tonos": 5, "semitonos": 2, "mayor": False},
    "lidio":  {"tonos": 6, "semitonos": 1, "mayor": True},
    "mixolidio": {"tonos": 5, "semitonos": 2, "mayor": True},
    "eólico": {"tonos": 5, "semitonos": 2, "mayor": False},
    "locrio": {"tonos": 5, "semitonos": 2, "mayor": False}
}

# Función principal
def clasificar_modo(nombre_escala, tonos, semitonos, comienza_en_do):
    nombre = nombre_escala.lower().strip()
    especie = "Exótico"

    if nombre in modos_gregorianos:
        info = modos_gregorianos[nombre]
        especie = "Mayor" if info["mayor"] else "Menor"
        coincidencia = (info["tonos"] == tonos) and (info["semitonos"] == round(semitonos))
    else:
        coincidencia = False
    
    # Reporte final
    print("\n Clasificación de modo musical")
    print(f"Nombre ingresado: {nombre_escala}")
    print(f"Tonos: {tonos} | Semitonos: {semitonos}")
    print(f"¿Comienza en Do? {'Sí' if comienza_en_do else 'No'}")
    
    if coincidencia:
        print(f"🎶 Modo reconocido: {nombre.capitalize()} ({especie})")
    else:
        print(" No coincide con ningún modo estándar → clasificado como Exótico")

# Entrada de datos
nombre_escala = input("Ingrese el nombre del modo (ej: Dórico, Locrio, etc.): ")
tonos = int(input("Ingrese cantidad de tonos enteros: "))
semitonos = float(input("Ingrese cantidad de semitonos: "))
inicio = input("¿Comienza en Do? (s/n): ")
comienza_en_do = inicio.lower() == "s"

clasificar_modo(nombre_escala, tonos, semitonos, comienza_en_do)