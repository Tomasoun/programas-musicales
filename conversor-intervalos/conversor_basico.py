print("=" * 40)
print("Conversor de Intervalos Musicales")
print("=" * 40)

print("Ingrese la cantidad de semitonos (0-24) para conocer el intervalo musical correspondiente contabilizado en semitonos.\nA saber: 0 = Unísono perfecto, 1 = semitono, 2 = tono, 3 = tono y medio, 4 = dos tonos, 5 = dos tonos y medio, etc.")
# Diccionario de referencia: semitonos → nombre de intervalo
intervalos = {
    0: "Unísono perfecto",
    1: "Segunda menor",
    2: "Segunda mayor",
    3: "Tercera menor",
    4: "Tercera mayor",
    5: "Cuarta justa",
    6: "Tritono",
    7: "Quinta justa",
    8: "Sexta menor",
    9: "Sexta mayor",
    10: "Séptima menor",
    11: "Séptima mayor",
    12: "Octava perfecta",
    13: "Novena menor",
    14: "Novena mayor",
    15: "Tercera menor sobre octava",
    16: "Oncena disminuida",
    17: "Oncena justa",
    18: "Oncena aumentada",
    19: "Quinta justa sobre octava",
    20: "Trecena menor",
    21: "Trecena mayor",
    22: "Séptima menor sobre octava",
    23: "Séptima mayor sobre octava",
    24: "Octava Aguda"
}

def convertir_intervalo(semitonos):
    if semitonos in intervalos:
        return f"{semitonos} semitonos = {intervalos[semitonos]}"
    else:
        return "Intervalo fuera de rango. Debe estar entre 0 y 24 semitonos."

# Interacción básica con el usuario
while True:
    entrada = input("Ingrese cantidad de semitonos (0-24) o 'salir': ")
    if entrada.lower() == "salir":
        print("¡Gracias por usar el conversor!")
        break
    if entrada.isdigit():
        semitonos = int(entrada)
        resultado = convertir_intervalo(semitonos)
        print(resultado)
    else:
        print("Entrada inválida. Ingrese un número o 'salir'.")