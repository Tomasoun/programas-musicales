# Lista de notas cromáticas en orden
notas_cromaticas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Función para obtener los semitonos entre la raíz y otras notas
def calcular_intervalos(notas_ingresadas):
    raiz = notas_ingresadas[0]
    indice_raiz = notas_cromaticas.index(raiz)
    intervalos = []
    
    for nota in notas_ingresadas:
        diferencia = (notas_cromaticas.index(nota) - indice_raiz) % 12
        intervalos.append(diferencia)
    
    intervalos_ordenados = sorted(set(intervalos))
    return intervalos_ordenados

# Función para identificar acorde según los intervalos
def identificar_acorde(intervalos):
    especie = {
        (0, 4, 7): "Acorde Mayor",
        (0, 3, 7): "Acorde Menor",
        (0, 3, 6): "Disminuido",
        (0, 4, 8): "Aumentado",
        (0, 5, 7): "Suspensión Cuarta",
        (0, 2, 7): "Suspensión Segunda",
        (0, 7): "Quinta justa (Power chord)",
        (0,): "Nota única"
    }
    return especie.get(tuple(intervalos), "Especie de acorde no reconocida")

# Entrada de notas por el usuario
print("=" * 40)
print("Programa para identificar especies de triadas musicales")
print("=" * 40)
print("Identificador de especies de triadas(mayor;menor;aumentada;disminuida;suspendida)\nlas notas del acorde deben estar sin inversión (estado fundamental) \nla raíz es la primera nota ingresada")
entrada = input("Ingrese las notas separadas por espacio (ej: C E G): ")
notas_usuario = entrada.strip().upper().split()

# Validación
if all(nota in notas_cromaticas for nota in notas_usuario):
    intervalos = calcular_intervalos(notas_usuario)
    tipo = identificar_acorde(intervalos)
    print(f"\nAcorde: {'-'.join(notas_usuario)}")
    print(f"Intervalos: {intervalos}")
    print(f"Especie: {tipo}")
else:
    print("Error: Una o más notas no son válidas. Usá notas como C, D#, F#, etc.")