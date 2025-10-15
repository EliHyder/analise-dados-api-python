import requests
import pandas as pd
import json

ceps = ['01001000', '20040030', '70070150']

dados = []

for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    dado = requests.get(url).json()
    dados.append(dado)

df = pd.DataFrame(dados)
print(df)