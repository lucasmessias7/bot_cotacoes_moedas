import httpx

class Requisicao_api():
    def __init__(self, url, endpoint):
        self.url = url
        self.endpoint = endpoint


    def request(self, metodo):
        url = f'{self.url}{self.endpoint}'
        if metodo == 'GET':
            response = httpx.get(url)
            data = response.json()
            return data
