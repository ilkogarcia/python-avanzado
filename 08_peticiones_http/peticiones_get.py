from urllib import response
import requests

'''respuesta = requests.get("https://api.github.com")
print(respuesta)
print(respuesta.headers)
print(respuesta.status_code)
print(respuesta.content)
print(respuesta.text)
print(respuesta.json())
print(respuesta.json()["current_user_url"])'''

respuesta = requests.get(
    "http://api.github.com/search/repositories",
    params={"q": "python"}
)
print(respuesta.status_code)
print(respuesta.json())

data = respuesta.json()
print(data.keys())
