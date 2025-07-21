print("=" * 40)
print("🎵 Clasificador de Compases Musicales")
print("=" * 40)

# Entrada del usuario
compas = input("Ingrese una cifra de compás (ej: 3/4, 6/8, 2/2): ").strip()

# Separar numerador y denominador
if "/" in compas:
    partes = compas.split("/")
    numerador = int(partes[0])
    denominador = int(partes[1])

    # Determinar tipo de compás
    if numerador % 2 == 0 and denominador in [4, 2]:
        tipo = "Binario simple"
    elif numerador == 3 and denominador in [4, 8, 2]:
        tipo = "Ternario simple"
    elif numerador in [6, 9, 12] and denominador == 8:
        tipo = "Compuesto"
    else:
        tipo = "No estándar o irregular"

    # Determinar tamaño del compás en figuras
    if denominador == 4:
        figura = "negra"
    elif denominador == 8:
        figura = "corchea"
    elif denominador == 2:
        figura = "blanca"
    else:
        figura = "figura desconocida"

    print(f"\n Compás: {compas}")
    print(f" Tipo: {tipo}")
    print(f" Tamaño: {numerador} {figura}s")
else:
    print("Error: La cifra debe tener formato x/y, como 3/4 o 6/8")