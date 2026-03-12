def encontra_palavra(frase):
    lista_palavras = frase.split()
    contagem = {}

    for p in lista_palavras:
        if p in contagem:
            contagem[p] += 1
        else:
            contagem[p] = 1

    return contagem


palavras = str(input("Digite uma frase com palavras repetidas e vamos tratar ela como um dicionário:"))
res = encontra_palavra(palavras)
print(f"{res}") 
