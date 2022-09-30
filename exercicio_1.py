def encontrar_valor_frete(quantidade):
    if quantidade < 11:
        valor_frete = 30.00
    elif quantidade >= 11 and quantidade < 101:
        valor_frete = 60.00
    elif quantidade >= 101 and quantidade < 1001:
        valor_frete = 120.00
    elif quantidade >= 1001:
        valor_frete = 240.00
    else:
        print("Por favor, insira um número válido igual ou maior que 0")
    return valor_frete

def main():
    print("Bem-vindo à loja da Maquele Antunes de Oliveira")
    valor_produto = float(input("Informe o valor do produto: "))
    quantidade_digitada = float(input("Informe a quantidade: "))

    valor_frete = encontrar_valor_frete(quantidade_digitada)
    valor_total = valor_produto * quantidade_digitada
    valor_total_com_frete = valor_total + valor_frete
    print("O valor sem frete foi {}".format(valor_total))
    print("O valor com frete foi {}".format(valor_total_com_frete))

if(__name__ == "__main__"):
    main()