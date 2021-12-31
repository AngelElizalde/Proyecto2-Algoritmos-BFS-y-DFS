"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""
from BFS import Bfs
from DFS import Dfs

#Llamada a los Algoritmos
def main():
    g = Grafica()
    h = Bfs()
    k = Dfs()

#Genera vertices
    l = [0, 1, 2, 3, 4, 5, 6]
    for v in l:
        g.agregaVertice(v)
        #print(v)

#Genera aristas
    l = [1, 2, 1, 5, 2, 3, 2, 5, 3, 4, 4, 5, 4, 6]
    for i in range(0, len(l) - 1, 2):
        a = l[i]
        b = l[i + 1]
        g.agregarArista(a, b)
        #print(a, b)

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

    print ("\n")
    h.bfs(2)
    print ("\n")
    print ("(1, NULL)")
    k.dfs(1)

main()
