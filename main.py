# url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real"
url_base = url[0:19]
url_parametros = url[20:36]

if __name__ == "__main__":
    print(f"URL: {url}")
    print(f"URL BASE: {url_base}")
    print(f"URL PARAMETROS: {url_parametros}")