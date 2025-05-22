
from produto import Produto

vendas_realizadas = []

def calcular_valor_venda(produto, quantidade_vendida):
    preco = produto.get("preco", 0)
    total = preco * quantidade_vendida
    return total

def registrar_venda():
    if not Produto.produtos:
        print("Nenhum produto cadastrado para vender.\n")
        return

    print("\n--- Produtos disponíveis para venda ---")
    for p in Produto.produtos:
        print(f"Código: {p['codigo']} - Nome: {p['nome']} - Estoque: {p['qntd']}")

    try:
        codigo = float(input("Digite o código do produto que deseja vender: "))
    except ValueError:
        print("Código inválido.\n")
        return

    produto_encontrado = None
    for p in Produto.produtos:
        if p["codigo"] == codigo:
            produto_encontrado = p
            break

    if not produto_encontrado:
        print("Produto não encontrado.\n")
        return

    try:
        quantidade_vendida = float(input("Digite a quantidade que deseja vender: "))
    except ValueError:
        print("Quantidade inválida.\n")
        return

    if quantidade_vendida > produto_encontrado["qntd"]:
        print(f"Quantidade indisponível em estoque. Temos {produto_encontrado['qntd']} unidades.\n")
        return

    total = calcular_valor_venda(produto_encontrado, quantidade_vendida)

   
    produto_encontrado["qntd"] -= quantidade_vendida

  
    venda = {
        "codigo_produto": produto_encontrado["codigo"],
        "nome_produto": produto_encontrado["nome"],
        "quantidade": quantidade_vendida,
        "total": total
    }
    vendas_realizadas.append(venda)

    print(f"Venda registrada! Total: R${total:.2f}\n")

def listar_vendas():
    if not vendas_realizadas:
        print("Nenhuma venda realizada até o momento.\n")
        return

    print("\n--- Histórico de Vendas ---")
    for i, v in enumerate(vendas_realizadas, 1):
        print(f"{i}. Produto: {v['nome_produto']} (Código: {v['codigo_produto']}) - Quantidade: {v['quantidade']} - Total: R${v['total']:.2f}")
    print()
