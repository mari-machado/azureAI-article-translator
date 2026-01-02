import requests
import uuid

key = "Sua chave aqui!"  #Inserção de chave
endpoint = "https://api.cognitive.microsofttranslator.com"
region = "Região do serviço"  #Alterar a região do serviço

texto = input()

path = "/translate"
params = {
    "api-version": "3.0",
    "to": ["pt"]
}

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Ocp-Apim-Subscription-Region": region,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4())
}

body = [{"text": texto}]

response = requests.post(
    endpoint + path,
    params=params,
    headers=headers,
    json=body
)

resultado = response.json()

print("Texto original:")
print(texto)
print("\nTexto traduzido:")
print(resultado[0]["translations"][0]["text"])
