#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agenda de Afinación de Pianos
Autor: Tomas
Descripción:
  Permite registrar datos técnicos y de contacto de cada piano,
  mostrar la agenda, actualizar la última afinación y guardar
  todo en un archivo JSON entre sesiones.
"""

import json
import os

ARCHIVO_JSON = "agenda_pianos.json"

def cargar_agenda():
    """Carga la agenda desde el archivo JSON o devuelve un diccionario vacío."""
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_agenda(agenda):
    """Guarda la agenda en el archivo JSON con formato legible."""
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)
    print("💾 Agenda guardada correctamente.\n")

def mostrar_agenda(agenda):
    """Imprime en consola todos los pianos registrados y sus datos."""
    if not agenda:
        print("📭 La agenda está vacía.\n")
        return

    for clave, datos in agenda.items():
        print(f"🎹 {clave}: {datos['marca']} {datos['modelo']} ({datos['año']})")
        print(f"   🗓️ Última afinación: {datos['última_afinación']}")
        dueño = datos["dueño"]
        print(f"   👤 Dueño: {dueño['nombre']}")
        print(f"   📍 Dirección: {dueño['dirección']}")
        print(f"   📧 Correo: {dueño['correo']}")
        print(f"   📞 Teléfono: {dueño['teléfono']}")
        print("-" * 50)
    print()

def agregar_piano(agenda):
    """Solicita datos por consola y agrega un nuevo piano a la agenda."""
    clave = input("🔑 ID del piano (ej. piano1): ").strip()
    if clave in agenda:
        print(f"❗ Ya existe la clave '{clave}'. Elige otro identificador.\n")
        return

    marca      = input("🎹 Marca: ").strip()
    modelo     = input("📘 Modelo: ").strip()
    try:
        año = int(input("📅 Año de fabricación: ").strip())
    except ValueError:
        print("❌ Año inválido. Debe ser un número.\n")
        return
    afinacion  = input("🗓️ Última afinación (YYYY-MM-DD): ").strip()
    nombre     = input("👤 Nombre del dueño: ").strip()
    direccion  = input("📍 Dirección: ").strip()
    correo     = input("📧 Correo electrónico: ").strip()
    telefono   = input("📞 Teléfono: ").strip()

    agenda[clave] = {
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "última_afinación": afinacion,
        "dueño": {
            "nombre": nombre,
            "dirección": direccion,
            "correo": correo,
            "teléfono": telefono
        }
    }
    print(f"✅ Piano '{clave}' agregado con éxito.\n")

def actualizar_afinacion(agenda):
    """Permite actualizar la fecha de última afinación de un piano existente."""
    clave = input("🔑 ID del piano a actualizar: ").strip()
    if clave not in agenda:
        print(f"❌ No existe la clave '{clave}'.\n")
        return
    nueva_fecha = input("🗓️ Nueva fecha de última afinación (YYYY-MM-DD): ").strip()
    agenda[clave]["última_afinación"] = nueva_fecha
    print(f"🔄 Fecha de afinación de '{clave}' actualizada a {nueva_fecha}.\n")

def main():
    agenda_pianos = cargar_agenda()

    while True:
        print("🎼 Menú de la Agenda de Afinación de Pianos")
        print("1. Mostrar agenda")
        print("2. Agregar nuevo piano")
        print("3. Actualizar última afinación")
        print("4. Guardar y salir")
        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            mostrar_agenda(agenda_pianos)
        elif opcion == "2":
            agregar_piano(agenda_pianos)
        elif opcion == "3":
            actualizar_afinacion(agenda_pianos)
        elif opcion == "4":
            guardar_agenda(agenda_pianos)
            break
        else:
            print("❌ Opción inválida. Intentá de nuevo.\n")

if __name__ == "__main__":
    main()