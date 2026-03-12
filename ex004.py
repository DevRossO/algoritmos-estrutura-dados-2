def remover_pessoa(fila):
    if len(fila) > 0:
        removido = fila.pop(0)
        print(f"{removido} saiu da fila")
    else:
        print("A fila está vazia")

def adicionar_pessoa(fila, nome):
    fila.append(nome)
    print(f"{nome} entrou na fila\n")

fila = []

while True:
    print(f"Fila atual: {fila}")
    opcao = input("1: Adicionar  |  2: Remover    3: Sair\nEscolha:")

    if opcao == "1":
        nome = input("Nome:")
        adicionar_pessoa(fila, nome)
    elif opcao == "2":
        remover_pessoa(fila)
    elif opcao == "3":
        break
    else:
        print("Opção inválida")