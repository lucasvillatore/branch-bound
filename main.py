#!/usr/bin/python3.8
import sys

caminhos = []

def splita_entrada_em_inteiros(entrada: str):
    return [0] + [int(x) for x in entrada.split()]

def deixa_lista_mesmo_tamanho(quantidade: int, lista: list):
    return [0] * quantidade + lista

def pega_grafo_input(numero_vertices: int):
    grafo = []
    for index in range(0, numero_vertices - 1):
        quantidade = deixa_lista_mesmo_tamanho(index, splita_entrada_em_inteiros(input()))
        grafo.append(quantidade)           
    
    ultimo_elemento = [0] * numero_vertices
    grafo.append(ultimo_elemento)

    for i in range(0, numero_vertices):
        for j in range(0, i):
            grafo[i][j] = grafo[j][i]
    
    return grafo

def pega_vizinhos(grafo: list, indice: int):
    vizinhos = []
    numero_vertices = len(grafo[0])
    for i in range(0, numero_vertices):
        if (grafo[indice][i] > 0):
            vizinhos.append(i)
    return vizinhos

def mesma_aresta(v1: int , v2: int, v3: int, v4: int):
    return v1 == v3 and v2 == v4

def aresta_processada(vertice_a: int, vertice_b: int, caminho: int):
    return any(
        mesma_aresta(vertice_a, vertice_b, c1, c2)
        for c1, c2
        in zip(caminho[:-1], caminho[1:])
    )

def caminho_valido(vertice: int, caminho_atual: list):
    return vertice not in caminho_atual or vertice == 0

def caminho_finalizado(caminho_atual: list):
    return caminho_atual.count(0) > 1


def existe_caminho_ate_raiz(grafo:list , vertice: int, visitados:list):
    if (vertice == 0):
        return True
    vizinhos = pega_vizinhos(grafo, vertice)
    visitados.append(vertice)
    for vizinho in vizinhos:
        if (vizinho not in visitados or vizinho == 0) and existe_caminho_ate_raiz(grafo, vizinho, visitados):
            return True
    return False


def branch_bound(grafo: list, vertice: int, caminho_atual: list):
    vizinhos = pega_vizinhos(grafo, vertice)

    caminho_atual.append(vertice)
    for vizinho in vizinhos:
        if (
            caminho_valido(vizinho, caminho_atual) and 
            not aresta_processada(vertice, vizinho, caminho_atual) and
            not caminho_finalizado(caminho_atual)
            # and existe_caminho_ate_raiz(grafo, vertice, caminho_atual.copy())
        ):
            branch_bound(grafo, vizinho, caminho_atual.copy())
    
    if (vertice == 0 and len(caminho_atual) > 1):
        caminhos.append(caminho_atual)

def calcula_custo(caminho: list, grafo: list):
    vertice_atual = 0
    custo = 0 

    for proximo_vertice in range(0, len(caminho)):
        custo += grafo[vertice_atual][caminho[proximo_vertice]]
        vertice_atual = caminho[proximo_vertice]
    
    return custo

def pega_custo_e_caminho_maximo(grafo: list):
    custo_maximo = 0
    numero_nos_arvore = 0
    caminho_maximo = []
    for indice in range(0, len(caminhos)):
        caminho_atual = caminhos[indice]
        custo_atual = calcula_custo(caminho_atual, grafo)
        numero_nos_arvore += len(caminhos[indice])
        if (custo_atual > custo_maximo):
            custo_maximo = custo_atual
            caminho_maximo = caminho_atual

    caminho_maximo = [str(k + 1) for k in caminho_maximo]

    return numero_nos_arvore, custo_maximo, caminho_maximo

def mostra_grafo(grafo:list, numero_vertices: int):
    for i in range(0, numero_vertices):
        for j in range(0, numero_vertices):
            print(str(grafo[i][j]) + "\t", end="")
        print("")


if __name__ == '__main__':
    numero_vertices = int(input())
    grafo = pega_grafo_input(numero_vertices)

    branch_bound(grafo, 0, [])

    numero_nos_arvore, custo_maximo, caminho_maximo = pega_custo_e_caminho_maximo(grafo)

    # print(f'Número de nós na árvore gerada: {numero_nos_arvore}', file=sys.stderr)
    print(custo_maximo)
    print(" ".join(caminho_maximo))