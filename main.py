#!/usr/bin/python3.8

def splita_entrada_em_inteiros(entrada):
    quantidade = map(int, entrada.split())
    quantidade_em_inteiros = list(quantidade) 

    quantidade_em_inteiros.insert(0, 0) 
    
    return quantidade_em_inteiros

def deixa_lista_mesmo_tamanho(index, quantidade):
    for i in range(0, index):
        quantidade.insert(0, 0)    

    return quantidade

def existe_caminho_para_inicio(indice, grafo):
    if grafo[indice][0] > 0:
        return True
    return False

def pega_grafo_input(numero_vertices):
    grafo = []
    for index in range(0, numero_vertices - 1):
        quantidade = deixa_lista_mesmo_tamanho(index, splita_entrada_em_inteiros(input()))
        grafo.append(quantidade)           
    
    ultimo_elemento = [0 for i in range(0, numero_vertices)]
    grafo.append(ultimo_elemento)

    for i in range(0, numero_vertices):
        for j in range(0, i):
            grafo[i][j] = grafo[j][i]
    
    return grafo

def pega_vizinhos(grafo, indice):
    vizinhos = []
    numero_vertices = len(grafo[0])
    for i in range(0, numero_vertices):
        if (grafo[indice][i] > 0):
            vizinhos.append(i)
    return vizinhos

def mesma_aresta(vertice_a, vertice_b, vertice_c, vertice_d):
    return (vertice_a == vertice_c and vertice_b == vertice_d) or (vertice_a == vertice_d and vertice_b == vertice_c)

def aresta_processada(vertice_a, vertice_b, caminho):
    for i in range(0, len(caminho) - 1):
        if (mesma_aresta(vertice_a, vertice_b, caminho[i], caminho[i+1])):
            return True
    return False

caminhos = []

def caminho_valido(vertice, caminho_atual):
    return vertice not in caminho_atual or vertice == 0

def caminho_finalizado(caminho_atual):
    return caminho_atual.count(0) > 1

def busca_profundidade(grafo, vertice, caminho_atual):
    vizinhos = pega_vizinhos(grafo, vertice)

    caminho_atual.append(vertice)
    for vizinho in vizinhos:
        if (
            caminho_valido(vizinho, caminho_atual) and 
            not aresta_processada(vertice, vizinho, caminho_atual) and
            not caminho_finalizado(caminho_atual)
        ):
            busca_profundidade(grafo, vizinho, caminho_atual.copy())
    
    if (vertice == 0 and len(caminho_atual) > 1):
        caminhos.append(caminho_atual)

def calcula_custo(caminho, grafo):
    vertice_atual = 0
    custo = 0 

    for proximo_vertice in range(0, len(caminho)):
        custo += grafo[vertice_atual][caminho[proximo_vertice]]
        vertice_atual = caminho[proximo_vertice]
    
    # print(custo)

    return custo

def pega_custo_e_caminho_maximo(grafo):
    custo_maximo = 0
    caminho_maximo = []
    # exit()
    for indice in range(0, len(caminhos)):
        caminho_atual = caminhos[indice]
        # print(caminho_atual)
        custo_atual = calcula_custo(caminho_atual, grafo)
        if (custo_atual > custo_maximo):
            custo_maximo = custo_atual
            caminho_maximo = caminho_atual

    caminho_maximo = [str(k + 1) for k in caminho_maximo]

    return custo_maximo, caminho_maximo

def mostra_grafo(grafo, numero_vertices):
    for i in range(0, numero_vertices):
        for j in range(0, numero_vertices):
            print(str(grafo[i][j]) + "\t", end="")
        print("")

if __name__ == '__main__':
    numero_vertices = int(input())
    grafo = pega_grafo_input(numero_vertices)

    busca_profundidade(grafo, 0, [])

    # mostra_grafo(grafo, numero_vertices)
    custo_maximo, caminho_maximo = pega_custo_e_caminho_maximo(grafo)

    print(custo_maximo)
    print(" ".join(caminho_maximo))