
class Sessao:
    secoes = []

    @classmethod
    def adicionar_sessao(cls):
        nome = input("Digite o nome da sessão (ex: Alimentos, Bebidas): ")
        codigo = input("Digite um código para a sessão: ")

        sessao = {
            "nome": nome,
            "codigo": codigo
        }

        cls.secoes.append(sessao)
        print("Sessão adicionada com sucesso!\n")

    @classmethod
    def listar_sessoes(cls):
        if not cls.secoes:
            print("Nenhuma sessão cadastrada.\n")
            return

        print("\n--- Sessões disponíveis ---")
        for s in cls.secoes:
            print(f"Código: {s['codigo']} - Nome: {s['nome']}")
        print()

    @classmethod
    def obter_sessao_por_codigo(cls, codigo):
        for s in cls.secoes:
            if s["codigo"] == codigo:
                return s
        return None
