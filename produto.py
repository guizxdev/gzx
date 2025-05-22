from datetime import datetime
from sessao import Sessao
from validacao import validar_data_validade  


class Produto:
    produtos = []

    @classmethod
    def adicionar_produto(cls):
        if not Sessao.secoes:
            print("Você precisa cadastrar pelo menos uma sessão antes de adicionar produtos.\n")
            return

        print("Escolha uma sessão para este produto:")
        Sessao.listar_sessoes()
        codigo_sessao = input("Digite o código da sessão desejada: ")
        sessao_escolhida = Sessao.obter_sessao_por_codigo(codigo_sessao)

        if not sessao_escolhida:
            print("Sessão não encontrada. Produto não cadastrado.\n")
            return

        nome = input("Digite o nome do produto: ")
        codigo = float(input("Digite o código: "))
        preco = float(input("Digite o preço do produto: "))
        qntd = float(input("Digite a quantidade do produto: "))
        validade = input("Digite a data de validade do produto (dd/mm/aaaa): ")
        peso = input("Digite o peso: ")

        produto = {
            "nome": nome,
            "preco": preco,
            "qntd": qntd,
            "codigo": codigo,
            "validade": validade,
            "sessao": sessao_escolhida["nome"],
            "peso": peso
        }

        cls.produtos.append(produto)
        print("Produto adicionado com sucesso!\n")

    @classmethod
    def listar_produtos(cls):
        if not cls.produtos:
            print("Nenhum produto cadastrado.\n")
            return

        print("\n--- Lista de Produtos ---")
        for i, p in enumerate(cls.produtos, 1):
            print(f"{i}. Nome: {p['nome']}, Código: {p['codigo']}, Preço: R${p['preco']}, Quantidade: {p['qntd']}, Validade: {p['validade']}, Sessão: {p['sessao']}")
        print()

    @classmethod
    def verificar_validade(cls):
        if not cls.produtos:
            print("Nenhum produto cadastrado.\n")
            return

        print("\n--- Produtos disponíveis ---")
        for p in cls.produtos:
            print(f"Código: {p['codigo']} - Nome: {p['nome']} - Validade: {p['validade']}")

        codigo = input("Digite o código do produto para verificar validade: ")

        produto = None
        for p in cls.produtos:
            if str(p["codigo"]) == codigo:
                produto = p
                break

        if not produto:
            print("Produto não encontrado.\n")
            return

        data_validade = validar_data_validade(produto["validade"])
        if not data_validade:
            print("Formato de data de validade inválido no produto! Use dd/mm/aaaa.\n")
            return

        data_atual = datetime.now()

        if data_atual <= data_validade:
            print("Produto está dentro da validade.\n")
        else:
            print("Produto está fora da validade!\n")

    @classmethod
    def buscar_por_codigo(cls):
        if not cls.produtos:
            print("Nenhum produto cadastrado.\n")
            return

        codigo = input("Digite o código do produto para buscar: ")

        produto_encontrado = None
        for p in cls.produtos:
            if str(p["codigo"]) == codigo:
                produto_encontrado = p
                break

        if produto_encontrado:
            print(f"Produto encontrado: Nome: {produto_encontrado['nome']}, Código: {produto_encontrado['codigo']}, Preço: R${produto_encontrado['preco']}, Quantidade: {produto_encontrado['qntd']}, Validade: {produto_encontrado['validade']}, Sessão: {produto_encontrado['sessao']}\n")
        else:
            print("Produto não encontrado.\n")
