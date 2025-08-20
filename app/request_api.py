from main import Requisicao_api
from bot import send_mensage


url = 'https://economia.awesomeapi.com.br/json/'



def real_dolar():
    endpoint = 'last/USD-BRL'
    data = Requisicao_api(url,endpoint)
    saida_json = data.request('GET')
    send_mensage(saida_json)



# def moeda_cotacao():  
