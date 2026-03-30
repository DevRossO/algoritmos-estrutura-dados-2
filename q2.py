# Crie um array com 100 valores aleatórios faça uma busca para verificar se o valor 25
# está presente. Identifique a complexidade do pior caso

arr = [1, 4, 94, 32, 99, 410, 67, 69, 234, 27, 899, 515, 12, 8, 7, 99, 16, 15, 86, 32, 44, 55, 66, 77, 25, 88, 34, 17, 9, 11, 30,
       11, 9, 4, 2, 23, 28, 51, 50, 75, 98, 82, 79, 71, 69, 13, 100, 3123, 324, 3123, 5435, 656, 312, 564, 974, 1223, 1233 ]
procurado = 25

# if procurado in arr: # Se a ideia é apenas saber se o 25 está presente essa é a maneira mais performática de se fazer.
#     print(f"O número {procurado} está presente dentro do array")
# else:
#     print(f"Não foi encontrado o número {procurado} dentro do array")

for i, valor in enumerate(arr): # Uma maneira de descobrir se o 25 esta presente e também saber o indice dele.
    if valor == procurado:
        print(f"Achei o valor {valor} na posição {i}")
        break
