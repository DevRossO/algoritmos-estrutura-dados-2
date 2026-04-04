# Crie um array com 100 valores aleatórios faça uma busca para verificar se o valor 25
# está presente. Identifique a complexidade do pior caso
import random
arr = [random.randint(1, 150) for _ in range(100)] # list comprehension
procurado = 25
print(arr)

if procurado in arr: # Se a ideia é apenas saber se o 25 está presente essa é a maneira mais performática de se fazer.
    print(f"O número {procurado} está presente dentro do array")
else:
    print(f"Não foi encontrado o número {procurado} dentro do array")

# for i, valor in enumerate(arr): # Uma maneira de descobrir se o 25 esta presente e também saber o indice dele.
#     if valor == procurado:
#         print(f"Achei o valor {valor} na posição {i}")
#         break
