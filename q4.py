# Explique o que acontece fisicamente na estrutura quando um novo item é inserido no início

# Fisicamente quando eu aloco um item no ínicio da estrutura todos os itens da frente precisam avançar uma casa
# ou seja, ele mexe em toda estrutura de dados, o computador não cria do nada aquele espaço, ele começa primeiro
# movimentando o último item para direita, penúltimo e assim sucessivamente até liberar o espaço onde e determinei
# imagina 1 milhão de itens, ele vai fazer essa movimentação 1 milhão de vezes, mas agora se eu quero colocar no final
# ele simplesmente cria a última "casa" e adiciona o item, sem precisar mexer no restante todo do algoritmo