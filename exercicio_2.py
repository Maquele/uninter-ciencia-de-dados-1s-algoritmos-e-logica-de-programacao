import pandas as pd

def calculo_pagamento(tamanho, codigo):
    if tamanho == "p":
        if codigo == "tr":
            preco_sorvete = 6.00
        elif codigo == "es":
            preco_sorvete = 7.00
        elif codigo == "pr":
            preco_sorvete = 8.00 

    elif tamanho == "m":
        if codigo == "tr":
            preco_sorvete = 10.00
        elif codigo == "es":
            preco_sorvete = 12.00
        elif codigo == "pr":
            preco_sorvete = 14.00

    elif tamanho == "g":
        if codigo == "tr":
            preco_sorvete = 18.00
        elif codigo == "es":
            preco_sorvete = 21.00
        elif codigo == "pr":
            preco_sorvete = 24.00
    
    return(
        preco_sorvete
    )

def cardapio():
    cardapio_sorvetes = [["TR", "Sabores tradicionais", "R$ 6,00", "R$ 10,00", "R$ 18,00"],
                        ["ES", "Sabores especiais", "R$ 7,00", "R$ 12,00", "R$ 21,00"],
                        ["PR", "Sabores premium", "R$ 8,00", "R$ 14,00", "R$ 24,00"],
    ]
    df = pd.DataFrame(cardapio_sorvetes, columns=["Código", "Descrição", "Tamanho P (500ml)", "Tamanho M (1000ml)", "Tamanho G (2000ml)"])
    return print(df)

def mensagem_bem_vindo():
    print("*********************************")
    print("Bem-vindo à sorveteria da Maquele Antunes de Oliveira")
    print("*********************************")
    cardapio()

def main():

    mensagem_bem_vindo()

    encerra_pedido = False

    valor_pagamento = 0

    while(not encerra_pedido): 
        tamanho_pote_sorvete = (input("Informe o tamanho do pote de sorvete desejado (P/M/G): ")).strip().lower()
        if tamanho_pote_sorvete == "p" or tamanho_pote_sorvete == "m" or tamanho_pote_sorvete == "g":
            codigo_sabor_sorvete = (input("Informe o código do sabor do sorvete desejado (TR/ES/PR): ")).strip().lower()
            if codigo_sabor_sorvete == "tr" or codigo_sabor_sorvete == "es" or codigo_sabor_sorvete == "pr":
                deseja_novo_pedido = (input("Deseja pedir mais alguma coisa? (S/N) ")).strip().lower()
                novo_valor = calculo_pagamento(tamanho_pote_sorvete, codigo_sabor_sorvete)
                valor_pagamento = valor_pagamento + novo_valor
            else:
                print("CÓDIGO inválido")
                continue
        else:
            print("TAMANHO inválido")
            continue

        if deseja_novo_pedido == "n":
            break
    
    print("O total a ser pago é de {}".format(valor_pagamento))

if(__name__ == "__main__"):
    main()