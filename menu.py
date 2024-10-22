import main

def menu():
    while True:
        print("Selecione uma opção: ")
        print("1 - Buscar país")
        print("2 - Insert de país no banco de dados")
        print("3 - Buscar todos os países")
        print("4 - Deletar país")
        print("5 - Sair")

        opcao = input()

        if opcao == "1":
            codigo = input("Digite o código do país: ")
            resposta = main.buscar_da_api(codigo_pais=codigo)
            print(resposta)
        elif opcao == "2":
            codigo = input("Digite o código do país: ")
            main.buscar_e_inserir_pais(codigo_pais=codigo)
        elif opcao == "3":
            main.buscar_paises()
        elif opcao == "4":
            codigo = input("Digite o código do país: ")
            main.deletar_pais(codigo_pais=codigo)
        elif opcao == "5":
            break
        else:
            print("Opção inválida")

menu()
