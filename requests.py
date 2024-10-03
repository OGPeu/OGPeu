import requests

def converter_moeda(valor, de, para):
    url = f"https://api.exchangerate-api.com/v4/latest/{de}"
    response = requests.get(url)
    dados = response.json()
    taxa = dados['rates'][para]
    return valor * taxa

valor = float(input("Digite o valor a ser convertido: "))
de = input("Moeda de origem (ex: USD, EUR): ").upper()
para = input("Moeda de destino (ex: BRL, JPY): ").upper()

resultado = converter_moeda(valor, de, para)
print(f"{valor} {de} é igual a {resultado:.2f} {para}.")
