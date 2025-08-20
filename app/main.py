import httpx

class Requisicao_api():
    def __init__(self, url):
        self.url = url


    def request(self, metodo, endpoint):
        url = f'{self.url}{endpoint}'
        if metodo == 'GET':
            response = httpx.get(url)
            data = response.json()
            return data




if __name__ == "__main__":
    