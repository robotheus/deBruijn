import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

def main():
    arquivo = open("input.txt")
    entradas = arquivo.readlines()

    for entrada in entradas:
        tamanho, qtdSimbolos = map(int, entrada.strip("\n ").split())
        sequencia = deBruijn(tamanho, qtdSimbolos)
        print(f'Sequencia De Bruijn B({tamanho}, {qtdSimbolos}): {sequencia}')

def deBruijn(tamanho, qtdSimbolos):
    alfabeto = criaAlfabeto(qtdSimbolos)
    vertices = criaVertices(tamanho, alfabeto)
    grafo = criaGrafo(vertices)
    
    caminhoEuleriano = list(nx.eulerian_circuit(grafo))
    sequencia = caminhoEuleriano[0][0]

    for aresta in caminhoEuleriano:
        sequencia += aresta[1][-1]
    
    return sequencia

def criaAlfabeto(qtdSimbolos):
    alfabeto = []
    
    for x in range(qtdSimbolos):
        alfabeto.append(str(x))
    
    return alfabeto

def criaVertices(tamanho, alfabeto):
    vertices = []
    combinacoes = product(alfabeto, repeat=tamanho-1)
    
    for combinacao in combinacoes:
        vertices.append("".join(combinacao))

    return vertices

def criaGrafo(vertices):
    grafo = nx.DiGraph()

    for vertice1 in vertices:
        aux1 = vertice1
        aux1 = aux1[1:]
        
        for vertice2 in vertices:
            aux2 = vertice2
            aux2 = aux2[:-1]
            
            if aux1 == aux2:
                grafo.add_edge(vertice1, vertice2)
    
    # plt.figure(figsize=(8, 6))
    # pos = nx.spring_layout(grafo)
    # nx.draw_networkx(grafo, pos, with_labels=True, node_size=500, node_color='lightblue')
    # plt.title("Grafo de De Bruijn")
    # plt.axis("off")
    # plt.show()

    return grafo

main()