import numpy as np
import sounddevice as sd

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
}

def reproducir_intervalo(base_freq, semitonos):
    duracion = 0.8  # segundos
    fs = 44100  # frecuencia de muestreo
    nota2_freq = base_freq * 2 ** (semitonos / 12)

    def generar_seno(frecuencia):
        t = np.linspace(0, duracion, int(fs * duracion), False)
        onda = np.sin(2 * np.pi * frecuencia * t)
        return onda * 0.3  # volumen

    # Sonar notas secuenciales
    nota1 = generar_seno(base_freq)
    nota2 = generar_seno(nota2_freq)
    sd.play(np.concatenate((nota1, nota2)))
    sd.wait()

while True:
    entrada = input("Ingrese semitonos (0-12) o 'salir': ")
    if entrada.lower() == "salir":
        break
    if entrada.isdigit():
        semitonos = int(entrada)
        if 0 <= semitonos <= 12:
            print(f"🎶 {semitonos} semitonos = {intervalos[semitonos]}")
            reproducir_intervalo(base_freq=440, semitonos=semitonos)
        else:
            print("Rango válido: 0 a 12")
    else:
        print("Entrada inválida")