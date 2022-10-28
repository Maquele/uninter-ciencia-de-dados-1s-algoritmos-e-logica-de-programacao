def mensagem_bem_vindo():
    print("*********************************")
    print("Bem-vindo ao Programa de Serviços de Limpeza da Maquele Antunes de Oliveira")
    print("*********************************")

def metragem_limpeza():
    metros = False
    while not metros:
        print("---------------------MENU 1/3---------------------")
        try:
            metros = float((input("Digite a metragem da casa (m²): ")))
        except:
            print("Digite um valor numérico inteiro válido")
        if metros >= 30 and metros < 300:
            valor = 60 + 0.3 * metros
            return valor
        elif metros >= 300 and metros < 700:
            valor = 120 + 0.5 * metros
            return valor
        else:
            metros = False
            print("Não aceitamos limpezas de casas com metragem inferior a 30m² ou superior a 700m²")
            continue

def tipo_limpeza():
    tipo = False
    while not tipo:
        print("---------------------MENU 2/3---------------------")
        print("Escolha o tipo da limpeza:")
        print("B - Básica (Indicada para sujeiras semanais ou quinzenais)")
        print("C - Completa (30% a mais. Indicada para sujeiras não rotineiras)")
        tipo = (input(">>")).strip().lower()
        if tipo == "b":
            multiplicador = 1.00
            return multiplicador
        elif tipo == "c":
            multiplicador = 1.30
            return multiplicador
        else:
            tipo = False
            print("Opção inválida!")
            continue

def adicional_limpeza():
    encerrar = False
    total_valor_adicional = 0
    while not encerrar:
        print("---------------------MENU 3/3---------------------")
        print("Deseja algum adicional?")
        print("0- Não desejo mais nada (encerrar)")
        print("1- Passar 10 peças de roupas - R$ 10.00")
        print("2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00")
        print("3- Limpeza de 1 Geladeira/Freezer - R$ 20,00")
        adicional = float((input(">>")))
        if adicional == 0:
            valor_adicional = 0.00
            encerrar = True
            return total_valor_adicional
        elif adicional == 1:
            valor_adicional = 10.00
        elif adicional == 2:
            valor_adicional = 12.00
        elif adicional == 3:
            valor_adicional = 20.00
        else:
            print("Opção inválida!")
            continue
        total_valor_adicional = total_valor_adicional + valor_adicional

def main():
    mensagem_bem_vindo()

    valor = metragem_limpeza()

    multiplicador = tipo_limpeza()

    total_valor_adicional = adicional_limpeza()

    total = valor * multiplicador + total_valor_adicional
    print(f"O valor total é de R$ {total}")
    print(f"Descritivo:")
    print(f"Metragem: R$ {valor} * Tipo Limpeza: R$ {multiplicador} + Adicional: R$ {total_valor_adicional}")

if(__name__ == "__main__"):
    main()