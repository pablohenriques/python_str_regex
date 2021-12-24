import re
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
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é válida")

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

    def __len__(self):
        return len(self.url)

    def __str__(self):
        params = self.get_url_parametros()
        url_base = self.get_url_base()
        return f"URL: {self.url}\nParâmetros: {params}\nURL base: {url_base}"

    def __eq__(self, other):
        return self.url == other.url


if __name__ == "__main__":
    # url = None or ""
    url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
    ext = ExtratorURL(url)
    ext2 = ExtratorURL(url)
    valor_quantidade = ext.get_valor_parametro('quantidade')
    print(valor_quantidade)
    print(f"O tamanho da URL: {len(url)}")
    print(ext)
    print(ext == ext2)
    print(f"End Memoria EXT : {id(ext)}")
    print(f"End Memoria EXT2: {id(ext2)}")