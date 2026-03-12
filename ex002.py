def substitui_caracter(palavra):
    res = ''
    vogais = "aeiouAEIOU"
    for caractere in palavra:
        if (caractere in vogais):
            res += "*"
        else:
            res += caractere
    return res

palavra_vogais = str(input("Digite uma palavra que vai aparecer sem vogais:"))
resultado = substitui_caracter(palavra_vogais)
print(f"{resultado}")