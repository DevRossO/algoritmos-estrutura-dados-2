def inverte_palavra(palavra):
    pilha = []
    res = ''
    for caractere in palavra:
        pilha.append(caractere)
    while len(pilha) > 0:
        res += pilha.pop()
    return res


palavra_usuario = str(input("Digite uma palavra:"))
resultado = inverte_palavra(palavra_usuario)
print(f"{resultado}")