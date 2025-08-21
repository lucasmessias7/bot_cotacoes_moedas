from classes import Requisicao_api


url = 'https://economia.awesomeapi.com.br/json/'



def last_recorrence_coin(endpoint,chave_primaria):
    reponse = Requisicao_api(url,endpoint)
    data = reponse.request('GET')
    valores = data.get(chave_primaria, []) # -> 
    if valores:
        saida_name = valores['name']
        maior_valor_dia = valores['high']
        menor_valor_dia = valores['low']
        variacao_compra_dia_anterior = valores['varBid']
        mercado_paga_dolar = valores['bid']
        mercado_vende_dolar = valores['ask']
        

        return f'{saida_name}\nMaior valor em 24h: {maior_valor_dia}\nMenor valor em 24h: {menor_valor_dia}\nVariação comparada ao dia anterior: {variacao_compra_dia_anterior}\nValor de compra do Dólar: {mercado_paga_dolar}\nValor de vendo do Dólar: {mercado_vende_dolar}'



# exemplo - > last_recorrence_coin('last/USD-CNH', 'USDCNH'))

    