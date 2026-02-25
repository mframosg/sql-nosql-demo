"""
Operaciones CRUD básicas con MongoDB

Este script muestra cómo crear, leer, actualizar y eliminar
documentos en una colección de MongoDB.
"""
from pymongo import MongoClient
from pprint import pprint


# --- CONEXIÓN ---

class BaseDeDatos:
    """Maneja la conexión a MongoDB y expone la colección a usar."""

    def __init__(self, nombre_bd="escuela", nombre_coleccion="estudiantes"):
        self.cliente = MongoClient('localhost', 27017)
        self.bd = self.cliente[nombre_bd]
        self.coleccion = self.bd[nombre_coleccion]
        print(f"Conectado a: {nombre_bd}.{nombre_coleccion}")

    def cerrar_conexion(self):
        self.cliente.close()
        print("Conexión cerrada")


# --- OPERACIONES CRUD ---

def crear_estudiante(db, estudiante):
    """CREATE: inserta un documento en la colección."""
    resultado = db.coleccion.insert_one(estudiante)
    print(f"  Estudiante creado con ID: {resultado.inserted_id}")
    return resultado.inserted_id


def listar_estudiantes(db, filtro=None):
    """READ: devuelve todos los documentos que coincidan con el filtro."""
    if filtro is None:
        filtro = {}

    estudiantes = list(db.coleccion.find(filtro))

    if not estudiantes:
        print("  No se encontraron estudiantes.")
        return []

    for estudiante in estudiantes:
        estudiante['_id'] = str(estudiante['_id'])  # ObjectId → string legible
        pprint(estudiante)

    return estudiantes


def buscar_un_estudiante(db, filtro):
    """READ (uno): devuelve el primer documento que coincida con el filtro."""
    estudiante = db.coleccion.find_one(filtro)
    if estudiante is None:
        print("  No se encontró ningún estudiante.")
        return None
    estudiante['_id'] = str(estudiante['_id'])
    pprint(estudiante)
    return estudiante


def actualizar_estudiante(db, filtro, nuevos_valores):
    """UPDATE: modifica todos los documentos que coincidan con el filtro."""
    resultado = db.coleccion.update_many(filtro, {"$set": nuevos_valores})
    print(f"  Documentos modificados: {resultado.modified_count}")
    return resultado.modified_count


def eliminar_estudiante(db, filtro):
    """DELETE: elimina todos los documentos que coincidan con el filtro."""
    resultado = db.coleccion.delete_many(filtro)
    print(f"  Documentos eliminados: {resultado.deleted_count}")
    return resultado.deleted_count


# --- DEMO ---

def main():
    """
    Recorre las cuatro operaciones CRUD en orden.
    Empieza limpiando la colección para que la demo sea reproducible.
    """
    db = BaseDeDatos()

    try:
        # Limpiar la colección para empezar desde cero en cada ejecución
        db.coleccion.drop()
        print("Colección limpiada.\n")

        # ── CREATE ────────────────────────────────────────────────────────────
        print("=== 1. CREAR estudiantes ===")

        # Un estudiante puede cursar varias carreras (lista) o solo una (string)
        estudiante_1 = {
            "nombre": "Juan",
            "edad": 20,
            "carrera": ["Ingeniería de Sistemas", "Matemáticas"],
            "telefonos": ["3001234567", "3109876543"],
            "activo": True
        }
        estudiante_2 = {
            "nombre": "María",
            "edad": 22,
            "carrera": "Ingeniería de Sistemas",
            "telefonos": ["3205556677"],
            "activo": True
        }
        crear_estudiante(db, estudiante_1)
        crear_estudiante(db, estudiante_2)

        # ── READ ──────────────────────────────────────────────────────────────
        print("\n=== 2. LEER todos los estudiantes ===")
        listar_estudiantes(db)

        # Operadores de comparación de MongoDB (llevan $ para distinguirlos de campos):
        #   $gte  >=    $gt  >    $lte  <=    $lt  <    $eq  ==    $ne  !=
        print("\n=== 2b. LEER con filtro (edad >= 21) ===")
        listar_estudiantes(db, {"edad": {"$gte": 21}})

        print("\n=== 2c. BUSCAR uno (find_one) ===")
        # find_one devuelve solo el primer documento que coincida, no una lista
        buscar_un_estudiante(db, {"nombre": "Juan"})

        # ── UPDATE ────────────────────────────────────────────────────────────
        print("\n=== 3. ACTUALIZAR estudiante ===")
        actualizar_estudiante(db, {"nombre": "Juan"}, {"edad": 21})

        print("  Verificando el cambio:")
        listar_estudiantes(db, {"nombre": "Juan"})

        # ── DELETE ────────────────────────────────────────────────────────────
        print("\n=== 4. ELIMINAR estudiante ===")
        eliminar_estudiante(db, {"nombre": "María"})

        print("  Estudiantes restantes:")
        listar_estudiantes(db)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.cerrar_conexion()


if __name__ == "__main__":
    main()
