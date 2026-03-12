print("================ADICIONAR NÚMEROS NEGATIVOS E POSITIVOS=================")
lista = []

while True:
    print(f"Números: {lista} ")
    opcao = input("1. Adicionar números   |    2. Sair\nEscolha:")
    
    if opcao == "1":
        numero = int(input("Número:"))
        lista.append(numero)
    elif opcao == "2":
        break
    else:
        print("Opção inválida")

lista_positivos = []

for numeros in lista:
    if (numeros) > 0:
        lista_positivos.append(numeros)
if len(lista_positivos) >= 0:
    print(f"Esses são os números positivos {lista_positivos}")
else:
        print("Não há números positivos na lista")