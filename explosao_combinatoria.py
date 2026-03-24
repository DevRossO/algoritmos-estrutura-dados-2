# A lista começa com a base vazia (return[[]]), e a cada nível da recursão o número de combinações dobra, criando um cenário para cada possibilidade (verdadeiro ou falso) de cada item da lista.

# A variável pega o primeiro item da lista e isola ele, depois chama a função novamente para o resto da lista (sem o primeiro item).

# Chamamos a função novamente na variável 'resto', mas ignorando o primeiro item. O Python "pausa" esta execução e abre uma nova para resolver o que sobrou.

# Em resultado adicionamos dois cenários para cada cenário que o 'resto' nos devolveu: um onde a condição atual é falsa e outro onde é verdadeira. Isso dobra o número de cenários a cada nível da recursão, criando uma explosão combinatória.

# O for serve para iterar com cara cenário que a váriavel 'resto' nos devolveu, trabalhando em cima de false e true, dobrando o cenário a cada recursão.

atividades_game = ["Envenenado", "Escudo", "Mana_Baixa", "Vida_Baixa", "Vantagem"]

def busca_explosiva(atividades_game):
    if not atividades_game:
        return [[]]    

    primeiro = atividades_game[0]
    resto = busca_explosiva(atividades_game[1:])
    resultado = []

    for combinacao in resto:
        resultado.append([(primeiro, False)] + combinacao)    
        resultado.append([(primeiro, True)] + combinacao)
    return resultado

combinacoes = busca_explosiva(atividades_game)
print("Exemplo de combinações:")
for indice, i in enumerate(combinacoes):
    print(f"case[{indice}] = {i}")