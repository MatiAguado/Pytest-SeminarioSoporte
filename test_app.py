import pytest
from app import registrar_usuario
from db import get_connection

# db_conn = get_connection()
@pytest.fixture
def db_conn():
  conn = get_connection()
  yield conn         # Esto es lo que recibe el test
  conn.close()       # Se ejecuta al terminar el test

def test_registro_usuario_integracion(db_conn):
    # Ejecutamos el flujo completo
    resultado = registrar_usuario("Carlos", "carlos@gmail.com", db_conn)

    # Verificamos que se ingresó correctamente
    assert resultado is not None
    assert resultado[1] == "Carlos"
    assert resultado[2] == "carlos@gmail.com"

    # Validamos en la base de datos
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = ?", ("carlos@gmail.com",))
    count = cursor.fetchone()[0]
    assert count == 1

def test_registro_dos_usuarios(db_conn):
    registrar_usuario("Ana", "ana@gmail.com", db_conn)
    registrar_usuario("Luis", "luis@gmail.com", db_conn)

    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    count = cursor.fetchone()[0]
    assert count == 2
