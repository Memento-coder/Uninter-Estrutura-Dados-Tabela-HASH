class Nodo:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            valor = ord(sigla[0]) + ord(sigla[1])
            return valor % 10

    def inserir(self, sigla, nome):
        indice = self.funcao_hash(sigla)
        novo = Nodo(sigla, nome)

        # inserção no início
        novo.proximo = self.tabela[indice]
        self.tabela[indice] = novo

    def imprimir(self):
        for i in range(10):
            print(f"{i}:", end=" ")
            atual = self.tabela[i]

            while atual is not None:
                print(f"{atual.sigla}->", end="")
                atual = atual.proximo

            print("None")


def inserir_estados(tabela):
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"),
        ("AM", "Amazonas"), ("BA", "Bahia"), ("CE", "Ceará"),
        ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
        ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)


# PROGRAMA PRINCIPAL

tabela = TabelaHash()

print("Tabela hash vazia:")
tabela.imprimir()

print("\nInserindo estados...\n")
inserir_estados(tabela)

print("Tabela hash com estados:")
tabela.imprimir()

# estado fictício
tabela.inserir("LF", "Leonardo Felipe")

print("\nTabela hash com estado fictício:")
tabela.imprimir()
