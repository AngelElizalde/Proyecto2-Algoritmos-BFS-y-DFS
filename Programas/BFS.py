"""
Instituto Politécnico Nacional
Centro de investigación en computación
Maestría en ciencias en ingenieria de computo 

Análisis y diseño de Algoritmos 
Dr. Rolando Quintero Téllez

Corona Elizalde Luis Ángel
"""

#clase BFS
class Bfs:
    g = Grafica()
    def __ini__(self):
        self.bfs = {}

#Generación BFS
    def bfs(self, r):
        g = Grafica()
        if r in g.vertices:
            cola = [r]

            g.vertices[r].visitado = True
            g.vertices[r].nivel = 0

            print("("+ str(r) + ", "+ str(g.vertices[r].nivel)+")")

            while (len(cola) > 0):
                act = cola[0]
                cola = cola[1:]

                for v in g.vertices[act].vecinos:
                    if g.vertices[v].visitado == False:
                        cola.append(v)
                        g.vertices[v].visitado = True
                        g.vertices[v].nivel = g.vertices[act].nivel + 1
                        print("(" + str (v) + ", " + str(g.vertices[v].nivel) + ")")

