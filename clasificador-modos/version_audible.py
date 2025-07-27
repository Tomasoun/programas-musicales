import numpy as np
import sounddevice as sd

# Diccionario de modos en T/S
modos_ts = {
    "jonio":     ["T", "T", "S", "T", "T", "T", "S"],
    "dorio":     ["T", "S", "T", "T", "T", "S", "T"],
    "frigio":    ["S", "T", "T", "T", "S", "T", "T"],
    "lidio":     ["T", "T", "T", "S", "T", "T", "S"],
    "mixolidio": ["T", "T", "S", "T", "T", "S", "T"],
    "eolio":     ["T", "S", "T", "T", "S", "T", "T"],
    "locrio":    ["S", "T", "T", "S", "T", "T", "T"]
}

# Conversión T/S a semitonos numéricos
def convertir_modo_a_semitonos(modo_str):
    return [2 if paso == "T" else 1 for paso in modo_str]

modos = {nombre: convertir_modo_a_semitonos(pasos) for nombre, pasos in modos_ts.items()}
notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Generar secuencia de notas
def generar_modo(nota_base, nombre_modo):
    idx = notas.index(nota_base)
    secuencia = [nota_base]
    for paso in modos[nombre_modo]:
        idx = (idx + paso) % len(notas)
        secuencia.append(notas[idx])
    return secuencia

# Parámetros de sonido
FREQ_BASES = {"C": 261.63, "C#": 277.18, "D": 293.66, "D#": 311.13, "E": 329.63, 
              "F": 349.23, "F#": 369.99, "G": 392.00, "G#": 415.30, "A": 440.00, 
              "A#": 466.16, "B": 493.88}
FS = 44100
DUR = 0.3

# Generar escala sonora
def generar_escala(nombre_modo, nota_base, dur=DUR):
    escala = [FREQ_BASES[nota_base]]
    frec = FREQ_BASES[nota_base]
    for paso in modos[nombre_modo]:
        frec *= 2 ** (paso / 12)
        escala.append(frec)

    sonido = np.concatenate([
        0.5 * np.sin(2 * np.pi * f * np.linspace(0, dur, int(FS * dur), False))
        for f in escala
    ])
    sd.play(sonido, samplerate=FS)
    sd.wait()

# 🎛️ Selección del usuario
modo_input = input(f"Elegí un modo {list(modos.keys())}: ").lower()
nota_input = input(f"Elegí la nota base {notas}: ").upper()

if modo_input in modos and nota_input in notas:
    print("Notas:", generar_modo(nota_input, modo_input))
    generar_escala(modo_input, nota_input)
else:
    print("Modo o nota inválido. Probá de nuevo.")