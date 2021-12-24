import re


if __name__ == "__main__":
    endereco = "Rua das Flores, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
    # padrao_cep = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
    padrao_cep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
    busca_cep = padrao_cep.search(endereco)

    if busca_cep:
        cep = busca_cep.group()
        print(f"CEP: {cep}")
