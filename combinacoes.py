features = ["ler", "escrever", "exportar", "apagar"] # N atividades do usuário

def gerar_subconjuntos(features):
    if not features:
        return [[]] # Só existe o conjunto
        
    primeiro = features [0] # Declarando o primeiro item da lista para poder lidar com o resto
    resto = gerar_subconjuntos(features[1:]) #Tratando os demais itens da lista

    # Para cada atividade(subconjunto) do resto, temos duas opções:
    # 1) Combinar com o 'primeiro'
    # 2) Combinar sem o 'primeiro'
    resultado = [] # criando a variável resultado para agregar as combinações
    for subconjunto in resto: # Aqui eu digo para ele percorrer todo meu conjunto 
        resultado.append(subconjunto)   # sem o primeiro, onde fazemos as combinações desconsiderando o primeiro
        resultado.append([primeiro] + subconjunto) # primeiro (0) + subconjunto

    return resultado

todas_combinacoes = gerar_subconjuntos(features) #variavel criada fora da função para receber os dados dela
print(f"Número total de combinações: {len(todas_combinacoes)}")
print("Exemplo de combinações:")
for c in todas_combinacoes: # variavel c criada para exemplificar todas combinações
    print(c)

    

    