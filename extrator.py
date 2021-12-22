
class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitizar(url)
        self.validar()
    
    def sanitizar(self, url):
        if type(url) == str:
            return url.strip()
        return ""

    def validar(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        
        return valor


if __name__ == "__main__":
    # url = None or ""
    url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
    ext = ExtratorURL(url)
    valor_quantidade = ext.get_valor_parametro('quantidade')
    print(valor_quantidade)