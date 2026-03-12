def contar_digitos_pares(numero):
    numero = str(numero)
    contador = 0
    for caractere in numero:
        if (int(caractere) % 2 == 0):
            contador += 1
    return contador

valor = input('Qual valor voçê quer analisar dígitos pares?')
resultado = contar_digitos_pares(valor)        
print(f"o número que você digitou tem {resultado} números pares")