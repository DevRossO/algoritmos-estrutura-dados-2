# Recebe parametros de array e o número que vamos bucar
# Define left como posição 0 e right como tamanho do array -1
# Enquanto a janela de busca nao se fecha 
# # Define mid como 4: (9-0 = 9) 9//2 = 4, 0 + 4 = 4
# Se posição do mid == número buscado retorna mid
# Se posição mid < que número buscado adiciona 1 e retorna looping até encontrar
# Se o número que buscamos estiver na metade/esquerda, ele vai diminuindo até encontrar ele  


def busca_binaria(array, target):
    left, right = 0, len(array) -1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

print(busca_binaria([10,20,30,40,50,60,70], 50))