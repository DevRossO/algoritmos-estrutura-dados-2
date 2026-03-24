atividades_game = ["Envenenado", "Escudo", "Mana_Baixa", "Vida_Baixa", "Vantagem"]

def busca_explosiva(atividades_game):
    # A partir daqui a lista já começa a ser montada, tendo a lista vazia como base, e a cada nível da recursão, o número de combinações dobra, criando um cenário para cada possibilidade (verdadeiro ou falso) de cada item da lista.
    if not atividades_game:
        return [[]]    

    # Pegamos o primeiro item da lista atual (ex: "Envenenado").
    primeiro = atividades_game[0]
    # Chamamos a função novamente, mas ignorando o primeiro item.
    # O Python "pausa" esta execução e abre uma nova para resolver o que sobrou.
    resto = busca_explosiva(atividades_game[1:])
    # Aqui criamos uma lista vazia para guardar os novos cenários.
    resultado = []

    # Para cada cenário que o "resto" nos devolveu...
    for combinacao in resto:
        # Criamos um cenário onde a condição atual é FALSA e colamos no resto.
        resultado.append([(primeiro, False)] + combinacao)    
        # Criamos um cenário onde a condição atual é VERDADEIRA e colamos no resto.
        # Isso dobra o número de elementos a cada nível da recursão!
        resultado.append([(primeiro, True)] + combinacao)

    # Devolvemos a lista 'resultado' (com o dobro de itens) para a função acima.
    return resultado

# O programa começa aqui, chamando a função com os 5 itens.
combinacoes = busca_explosiva(atividades_game)

# Usamos o enumerate para mostrar o índice (case[n]) de cada combinação gerada.
print("Exemplo de combinações:")
for indice, i in enumerate(combinacoes):
    print(f"case[{indice}] = {i}")