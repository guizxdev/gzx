from produto import Produto
from sessao import Sessao
from vendas import registrar_venda, listar_vendas
from validacao import validar_data_validade

def menu():
    while True:
        print("==== MENU ====")
        print("1. Adicionar sessão")
        print("2. Adicionar produto")
        print("3. Listar sessões")
        print("4. Listar produtos")
        print("5. Buscar produto por código")
        print("6. Registrar venda")
        print("7. Listar vendas")
        print("8. Verificar Validade")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Sessao.adicionar_sessao()
        elif opcao == "2":
            Produto.adicionar_produto()
        elif opcao == "3":
            Sessao.listar_sessoes()
        elif opcao == "4":
            Produto.listar_produtos()
        elif opcao == "5":
            Produto.buscar_por_codigo()
        elif opcao == "6":
            registrar_venda()
        elif opcao == "7":
            listar_vendas()
        elif opcao == "8":
            Produto.verificar_validade()
        elif opcao == "9":
            
            
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
