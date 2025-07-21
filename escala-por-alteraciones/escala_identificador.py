print("=" * 40)
print("🎶 Identificador de Escalas Mayores por Alteraciones")
print("=" * 40)

# Diccionarios de referencia
escalas_sostenidos = {
    0: "Do mayor",
    1: "Sol mayor",
    2: "Re mayor",
    3: "La mayor",
    4: "Mi mayor",
    5: "Si mayor",
    6: "Fa# mayor",
    7: "Do# mayor"
}

escalas_bemoles = {
    0: "Do mayor",
    1: "Fa mayor",
    2: "Si♭ mayor",
    3: "Mi♭ mayor",
    4: "La♭ mayor",
    5: "Re♭ mayor",
    6: "Sol♭ mayor",
    7: "Do♭ mayor"
}

# Bucle principal
while True:
    entrada = input("\nIngrese  los sostenidos (#) o bemoles (b) \nej: 2#, 3b, 5#,etc. para concluir escribir 'salir': ").strip().lower()

    if entrada == "salir":
        print(" ¡Gracias por usar el identificador de escalas!")
        break

    if len(entrada) >= 2 and entrada[:-1].isdigit() and entrada[-1] in ['#', 'b']:
        cantidad = int(entrada[:-1])
        tipo = entrada[-1]

        if tipo == "#":
            if 0 <= cantidad <= 7:
                print(f"🔎 {cantidad} sostenido(s) → {escalas_sostenidos[cantidad]}")
            else:
                print("⚠️ Número de sostenidos fuera de rango (0 a 7)")
        else:
            if 0 <= cantidad <= 7:
                print(f"🔎 {cantidad} bemol(es) → {escalas_bemoles[cantidad]}")
            else:
                print("⚠️ Número de bemoles fuera de rango (0 a 7)")

    else:
        print("❌ Entrada inválida. Use formato como '3#' o '1b'")
