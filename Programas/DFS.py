"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

#clase DFS
class Dfs:
    g = Grafica()
    def __ini__(self):
        self.dfs = {}

#Generación de DFS
    def dfs(self, r):
        g = Grafica()
        if r in g.vertices:
            g.vertices[r].visitado = True
            for nodo in g.vertices[r].vecinos:
                if g.vertices[nodo].visitado == False:
                    g.vertices[nodo].padre = r
                    print("(" + str(nodo) + ", " + str(r) + ")")
                    g.dfs(nodo)
