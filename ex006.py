def processador_dados(lista_bruta):
    sem_duplicatas = list(set(lista_bruta))

    vistos = set()
    repetidos = set()

    for x in lista_bruta:
        if x in vistos:
            repetidos.add(x)
        else:
            vistos.add(x)

    return sem_duplicatas, list(repetidos)

lista = []
while True:
    opcao = input("1. Adicionar números     |     2.Sair\nEscolha:")
    if opcao == "1":
        num = int(input("Digite o número:"))
        lista.append(num)
    elif opcao == "2":
        break
    else:
        print(f"Opção inválida")

unicos, duplicados = processador_dados(lista)
print(f"Limpos: {unicos}")
print(f"Repetidos: {duplicados}")

       
