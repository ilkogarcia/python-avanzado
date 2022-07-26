from urllib import response
import requests

url = "https://webhook.site/97d689c7-e30c-402a-be62-e486c53d8897"
payload = {"plato": "pasta", "cantidad": 2}
query_params = {"nombre": "Paco"}
respuesta = requests.post(url, data=payload, params=query_params)
#print(respuesta.status_code)
#print(response.json())

