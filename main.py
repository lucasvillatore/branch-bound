#!/usr/bin/python3

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


if __name__ == '__main__':
    numero_vertices = int(input())
    grafo = pega_grafo_input(numero_vertices)