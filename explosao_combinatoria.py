# 1. Definimos a lista inicial com os nomes das condições do jogo.
atividades_game = ["Envenenado", "Escudo", "Mana_Baixa", "Vida_Baixa", "Vantagem"]

def busca_explosiva(atividades_game):
    # 2. CASO BASE: Se a lista estiver vazia, retornamos uma lista contendo uma lista vazia [[]].
    # Isso é o "chão" da nossa escada; é onde as combinações começam a ser montadas.
    if not atividades_game:
        return [[]]    

    # 3. ISOLAMENTO: Pegamos o primeiro item da lista atual (ex: "Envenenado").
    primeiro = atividades_game[0]
    
    # 4. RECURSÃO (A DESCIDA): Chamamos a função novamente, mas ignorando o primeiro item.
    # O Python "pausa" esta execução e abre uma nova para resolver o que sobrou.
    resto = busca_explosiva(atividades_game[1:])

    # 5. CONSTRUÇÃO (A SUBIDA): Aqui criamos uma lista vazia para guardar os novos cenários.
    resultado = []

    # 6. O LOOP DE EXPLOSÃO: Para cada cenário que o "resto" nos devolveu...
    for combinacao in resto:
        # 6a. Criamos um cenário onde a condição atual é FALSA e "colamos" no resto.
        resultado.append([(primeiro, False)] + combinacao)
        
        # 6b. Criamos um cenário onde a condição atual é VERDADEIRA e "colamos" no resto.
        # Isso dobra o número de elementos a cada nível da recursão!
        resultado.append([(primeiro, True)] + combinacao)

    # 7. RETORNO: Devolvemos a lista 'resultado' (com o dobro de itens) para a função acima.
    return resultado

# 8. CHAMADA INICIAL: O programa começa aqui, chamando a função com os 5 itens.
combinacoes = busca_explosiva(atividades_game)

# 9. EXIBIÇÃO: Usamos o enumerate para mostrar o índice (case[n]) de cada combinação gerada.
print("Exemplo de combinações:")
for indice, i in enumerate(combinacoes):
    print(f"case[{indice}] = {i}")