lista_functionarios = []

def menu_principal():
    print("---------------------------MENU PRINCIPAL---------------------------")
    print("Escolha a opção desejada:")
    print("1-Cadastrar Funcionário")
    print("2-Consultar Funcionário(s)")
    print("3-Remover Funcionário")
    print("4-Sair")
    return (input(">>")).strip().lower()

def menu_consultar():
    print("---------------------MENU CONSULTAR FUNCIONÁRIO---------------------")
    print("Escolha a opção desejada:")
    print("1-Consultar Todos os Funcionários")
    print("2-Consultar Funcionário por Id")
    print("3-Consultar Funcionário(s) por Setor")
    print("4-Retornar")
    return (input(">>")).strip().lower()

def cadastrar_funcionario(id):
    print("Código do funcionário {}".format(id))
    nome = (input("Por favor entre com o NOME:")).strip().lower()
    setor = (input("Por favor entre com o SETOR:")).strip().lower()
    salario = (input("Por favor entre com o SALÁRIO (R$):")).strip().lower()
    novo_funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    lista_functionarios.append(novo_funcionario)

def print_funcionario(funcionario):
    print("id: {}".format(funcionario["id"]))
    print("nome: {}".format(funcionario["nome"]))
    print("setor: {}".format(funcionario["setor"]))
    print("salario: {}".format(funcionario["salario"]))

def consultar_funcionarios():
    
    sair = False
    while(not sair):
        opcao_selecionada = menu_consultar()
        if opcao_selecionada == "1":
            for funcionario in lista_functionarios:
                print_funcionario(funcionario)
        elif opcao_selecionada == "2":
            id_selecionado = (input("Digite o ID do funcionário:")).strip().lower()
            encontrado = False
            for funcionario in lista_functionarios:
                if str(funcionario["id"]) == id_selecionado:
                    encontrado = True
                    print_funcionario(funcionario)
            if not encontrado:
                print("O ID informado não foi encontrado")

        elif opcao_selecionada == "3":
            setor_selecionado = (input("Digite o setor do funcionário:")).strip().lower()
            encontrado = False
            for funcionario in lista_functionarios:
                if funcionario["setor"] == setor_selecionado:
                    encontrado = True
                    print_funcionario(funcionario)
            if not encontrado:
                print("O Setor informado não possui funcionários")
        elif opcao_selecionada == "4":
            sair = True
        else:
            print("Opção inválida!")
        print("-----------------------")

def remover_funcionario():
    print("-------------------------REMOVER FUNCIONÁRIO------------------------")
    id_selecionado = (input("Digite o ID do funcionário a ser removido:")).strip().lower()
    for i in range(len(lista_functionarios)):
        if str(lista_functionarios[i]["id"]) == id_selecionado:
            del lista_functionarios[i]
            break

def mensagem_bem_vindo():
    print("*********************************")
    print("Bem-vindo ao controle de funcionários da Maquele Antunes de Oliveira")
    print("*********************************")

def main():

    mensagem_bem_vindo()

    sair = False
    codigo_atual = 1

    while(not sair):
        opcao_selecionada = menu_principal()
        if opcao_selecionada == "1":
            cadastrar_funcionario(codigo_atual)
        elif opcao_selecionada == "2":
            consultar_funcionarios()
        elif opcao_selecionada == "3":
            remover_funcionario()
        elif opcao_selecionada == "4":
            sair = True
        else:
            print("Opção inválida!")

        codigo_atual += 1
    
    print("---------------------------FIM---------------------------")

if(__name__ == "__main__"):
    main()
