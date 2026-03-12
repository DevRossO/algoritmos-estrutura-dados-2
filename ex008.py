def buscar_telefone(nome, dicionario_contatos):
    if nome in dicionario_contatos:
        return dicionario_contatos[nome]
    else:
        return "Contato não encontrado"

def listar_ordem_alfabetica(lista_telefonica):
    nomes_ordenados = sorted(lista_telefonica.keys())
    if len(nomes_ordenados) > 0:
        for nome in nomes_ordenados:
            print(f"Nome: {nome} - Telefone: {lista_telefonica[nome]}")
    else:
        print("Agenda está vazia")
    return

agenda = {}

while True:
    print("==========LISTA TELEFONICA==========")
    opcao = str(input("1. Adicionar nome e telefone\n2. Buscar telefone da pessoa pelo nome\n3. Listar em ordem alfabética\n4. Sair\nEscolha: "))
    if opcao == "1":
        nome = str(input("Nome que você quer adicionar: "))
        telefone = int(input(f"Qual telefone de {nome} : "))
        agenda[nome] = telefone
        print(f"Adicionado a agenda:\nContato {nome} e Telefone {telefone}")
    elif opcao == "2":
        nome_lista = str(input("Qual nome você quer buscar? "))
        res = buscar_telefone(nome_lista, agenda)
        print(f"{res}")
    elif opcao == "3":
        listar_ordem_alfabetica(agenda)
    elif opcao == "4":
        break
    else:
        print("Opcao inválida")
        



