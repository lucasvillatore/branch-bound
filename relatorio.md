**Aluno:** Lucas Block Villatore

## Descrição do problema

**Caminhada máxima:** Toda manhã Sr. Gump sai para caminhar por sua cidade. Ele não gosta de passar mais de uma vez por cada lugar. Mas ele gosta de demorar em seu passeio. Dado um conjunto de lugares (vértices), as ligações entre estes lugares (arestas) e os custos (tempo) de percorrer cada uma destas ligações, devemos encontrar um trajeto para o Sr. Gump que seja o mais longo possível, sem repetir lugares.

## Modelagem

Falar que precisamos pegar o caminho máximo possível e blablabla

## Análise da função limitante

## Detalhes da implementação

Nesse trabalho, para representar os caminhos possíveis, foi utilizado um grafo como estrutura de dados. Para representar esse grafo, utilizei uma matriz de adjacência Mn*n, onde n representa o número de vértices dado na leitura dos dados.

A implementação pode ser separada nos 4 tópicos a seguir:

- Leitura
- Geração da árvore de caminhos minimos
- Busca pelo custo e caminho máximo
- Mostra resultados na tela

### Leitura

Nessa parte, é construído a estrutura do Grafo. Para cada valor lido i * j, é atualizado no grafo de adjacência tanto na posição i * j quanto na posiçao j * i para facilitar a manipulação.

### Geração da árvore de caminhos mínimos

A partir do grafo gerado, o algoritmo realizará uma busca em profundidade para gerar uma árvore de caminhos mínimos. A cada caminho mínimo gerado, a busca em profundidade armazenará na váriavel *caminhos* todo o caminho percorrido até chegar novamente ao vértice inicial.

A busca em profundidade irá percorrer o próximo caminho se:

- O caminho é válido, i.e, não tentar ir até um vértice que já foi visitado
- Aresta *{v, u}* não tenha sido processada, i.e, não tiver no vetor de caminhos percorridos [..., v, u, ...]
- O caminho não estiver finalizado, i.e, não ter voltado para o vértice inicial.

### Busca pelo custo e caminho máximo

Nessa parte, o algoritmo vai fazer uma busca simples na árvore gerada pela etapa anterior. O algoritmo percorre o caminho que foi utilizado na busca em profundidade e armazena o custo desse caminho. O caminho que tiver o maior custo será retornado para o programa principal.

### Mostrar resultados na tela

O algoritmo mostrará 3 informações:

- Na saída de erro, quantos nós na árvore de caminhos mínimos foram gerados
- Na saída padrão
  - O custo do caminho
  - O caminho percorrido.





## Melhorias possíveis no algoritmo



## Exemplos de entrada





