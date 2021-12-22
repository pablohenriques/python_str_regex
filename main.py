# url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
url = " "

# sanitizacao da url
url  = url.strip()

# validacao url
if url == "":
    raise ValueError("A URL está vazia")

indice_interrogacao = url.find('?')

# url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


# parametro_busca = "moedaOrigem" 
# parametro_busca = "moedaDestino" 
parametro_busca = "quantidade" 
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]



if __name__ == "__main__":
    print(f"URL: {url}")
    #print(f"URL BASE: {url_base}")
    print(f"URL PARAMETROS: {url_parametros}")
    print(f"Valor: {valor}")