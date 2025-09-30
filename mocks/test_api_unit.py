from unittest.mock import patch, Mock
from api_client import obtener_usuario

@patch("api_client.requests.get")
def test_obtener_usuario_unitario(mock_get):
    #Configurar la respuesta falsa de la API
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 1,
        "name": "Juan Perez",
        "email": "juan@gmail.com"
    }
    mock_get.return_value = fake_response

    # Llamamos a la función bajo prueba
    resultado = obtener_usuario(1)

    # Verificamos que requests fue llamado con la URL correcta
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")

    # Verificamos que el resultado es correcto
    assert resultado == {
        "id": 1,
        "nombre": "Juan Perez",
        "email": "juan@gmail.com"
    }
