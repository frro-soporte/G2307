"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""
    conexion: sqlite3.Connection = sqlite3.connect('data.db')
    try:
        persona = buscar_persona(id_persona)
        if not persona:
            return False
        cursor: sqlite3.Cursor = conexion.cursor()
        cursor.execute(
            """
            SELECT * FROM PersonaPeso 
            WHERE IdPersona = (?) AND Fecha > (?);
            """,
            (id_persona, fecha)
        )
        persona_peso = cursor.fetchall()
        if persona_peso:
            return False
        cursor.execute(
            """
            INSERT INTO PersonaPeso(IdPersona, Fecha, Peso) VALUES(?,?,?);
            """,
            (id_persona, fecha, peso)
        )
        ultimo_id = cursor.lastrowid
        conexion.commit()
        return ultimo_id
    except:
        conexion.rollback()
        return False
    finally:   
        conexion.close()




# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False
if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
