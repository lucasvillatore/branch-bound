#!/usr/bin/python3

def splita_entrada_em_inteiros(entrada):
    quantidade = map(int, entrada.split())
    quantidade_em_inteiros = list(quantidade) 

    return quantidade_em_inteiros

matriz = []
if __name__ == '__main__':
    numero_vertices = int(input())
    for index in range(0, numero_vertices - 1):
        quantidade = splita_entrada_em_inteiros(input())
        for i in range(0, index):
            quantidade.insert(0, -1)     
        matriz.append(quantidade)


    for i in range(numero_vertices - 1):
        for j in range(numero_vertices - 1):
            # if (matriz[i][j] == -1):
                # print("  ",end="")
            # else:
            print(f"{matriz[i][j]} ", end="")
        print("")