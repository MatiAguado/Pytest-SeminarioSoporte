import requests

def obtener_usuario(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "nombre": data["name"],
            "email": data["email"]
        }
    else:
        return None
