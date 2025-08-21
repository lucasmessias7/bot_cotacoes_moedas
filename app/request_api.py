from bot import send_mensage
from classes import Requisicao_api


url = 'https://economia.awesomeapi.com.br/json/'

def request_values(endpoint):
    endpoint_url = endpoint
    reponse = Requisicao_api(url,endpoint_url)
    data = reponse.request('GET')
    return data


def last_recorrence_coin(endpoint,chave_primaria):
    response = request_values(endpoint=endpoint)
    valores = response.get(chave_primaria, []) # -> 
    if valores:
        saida_name = valores['name']
        maior_valor_dia = valores['high']
        menor_valor_dia = valores['low']
        variacao_compra_dia_anterior = valores['varBid']
        mercado_paga_dolar = valores['bid']
        mercado_vende_dolar = valores['ask']
        

        return f'{saida_name}\nMaior valor em 24h: {maior_valor_dia}\nMenor valor em 24h: {menor_valor_dia}\nVariação comparada ao dia anterior: {variacao_compra_dia_anterior}\nValor de compra do Dólar: {mercado_paga_dolar}\nValor de vendo do Dólar: {mercado_vende_dolar}'



print(last_recorrence_coin('last/USD-BRL', 'USDBRL'))
print()
print(last_recorrence_coin('last/EUR-BRL', 'EURBRL'))
print()
print(last_recorrence_coin('last/BTC-BRL', 'BTCBRL'))
    