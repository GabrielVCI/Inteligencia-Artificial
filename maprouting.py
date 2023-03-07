#Clase Nodo

#Ricardo Baez
class Nodo:
    
    # Se inicializa la clase
    def __init__(self, name, parent, g, h, f):                                          
        self.name = name
        self.parent = parent
        self.g = g  # Distancia al nodo inicial
        self.h = h  # Distancia al nodo objetivo
        self.f = f  # Costo total
            
     # Comparamos los nodos       
    def __eq__(self, other):                                                            
        return self.name == other.name
    
    
    # Clasificamos nodos
    def __lt__(self, other):                                                            
        return self.f < other.f
    
     # Imprimimos(devolvemos) nodos
    def __repr__(self):                                                                
        return ('({0},{1})'.format(self.name, self.f))
    
    #Método simplemente para dar formato de como queremos que se vea el resultado del print
    def imprimirNodo(self):                                                             
        print(self.name, end = " - ")
        print(self.parent, end = " : ")
        print(self.g, end = " : ")
        print(self.h, end=" : ")
        print(self.f)

#Ricardo Baez


#Angel Peinado
#Clase del Grafo
class Graph:
    
    # Iniciamos la clase
    def __init__(self, graph_dict=None, directed=True):                                 
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
                
    # Creamos un grafo no dirigido añadiendo aristas          
    def make_undirected(self):                                                          
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
                    
    # Método que va a realizar las conexiones. Básicamente unimos dos puntos, el A y B con una distancia dada.                
    def connect(self, A, B, distance=1):                                               
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
               
    # Función para obtener a los vecinos        
    def get(self, a, b=None):                                                           
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
#Angel Peynado




#Channel
    # Metodo en donde retornamos una lista de nodos en el grafo       
    def nodes(self):                                                                    
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
    # Obtenemos el vecino que tenga menor costo
    def getNode(self, city, heuristics, end):                                           
        nodes = list()
        min = 999
        for (b,dist) in self.graph_dict[city].items():
            if(b == end):
                return Nodo(city, b, dist, heuristics[b], dist+heuristics[b] )
            nodes.append(Nodo(city, b, dist, heuristics[b], dist+heuristics[b] ))
            if (dist+heuristics[b]) < min:
                min = dist+heuristics[b]
                minnode = Nodo(city, b, dist, heuristics[b], dist+heuristics[b] )       
        return minnode
        
    #Imprimimos cada borde del grafo
    def printgraph(self):                                                               
         for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                print (self.graph_dict.setdefault(a,{})[b], end = " : ")
                print(a, end = " - ")
                print(b)
#Channel


#Gabriel
#Implementamos el algoritmo de búsqueda A*
def A_Star(graph, heuristics, start, end):
    open_list = list() #Creamos  objetos de tipo lista
    closed_list = list()  
    path = list()  #Almacena el camino que estamos tomando
    curr_node = graph.getNode(start,heuristics, end)   #Inicializa el nodo
    open_list.append(curr_node)
    totalcost = 0

    if(end not in graph.graph_dict):                 #Aquí está el condicional donde se evalúa si se llego al estado objetivo
        # Si no existe tal meta, o no ha llegado
        print("No ha llegado a su objetivo")
        return None

    while(curr_node.name != end):       #Mientras no se llegue a la meta o al final
        totalcost += curr_node.g
        path.append(curr_node.name)
        curr_node = open_list.pop()
        #El pop es un método de las listas que elimina de la lista el elemento en el índice dado y devuelve el elemento eliminado.
        closed_list.append(curr_node) #El append, que también es un método de la lista, va a añadir un elemento al final de la lista.
        curr_node = graph.getNode(curr_node.parent, heuristics, end)
        open_list.append(curr_node)
        if(curr_node.name == end): #Si el nodo en el que estamos, es el nodo objetivo, llegamos a nuestra meta.
            path.append(curr_node.name)
            break
        
    print("MENOR COSTO TOTAL ---> " + str(totalcost))
    return path
#Gabriel


#Chardinson de la Cruz
#FUNCIÓN MAIN
def main():
    # Creamos el grafo
    graph = Graph()
        
    # Creamos las conexiones del grafo (Distancias entre cada punto)
    graph.connect('Villa Mella', 'Arroyo Hondo', 12)
    graph.connect('Villa Mella', 'Capotillo', 9)
    graph.connect('Zona Colonial', 'Ciudad Universitaria', 4)
    graph.connect('Capotillo', 'Zona Colonial', 4)
    graph.connect('Alma Rosa', 'Capotillo', 7)
    graph.connect('Alma Rosa', 'Las Praderas', 14)
    graph.connect('Bella Vista', 'Zona Colonial', 6)
    graph.connect('Bella Vista', 'Arroyo Hondo', 8)
    graph.connect('Ciudad Universitaria','Las Praderas', 6)
    graph.connect('Capotillo', 'Arroyo Hondo', 8)
    graph.connect('Ciudad Universitaria', 'Alma Rosa', 11)
        
    # Hacemos el grafo, creando las conexiones
    graph.make_undirected()
        
    # Creamos lo que serían las heurísticas (distancia yendo a pie) para cualquier destino en Santo Domingo
    heuristics = {}
    heuristics['Zona Colonial'] = 6
    heuristics['Santo Domingo'] = 0
    heuristics['Ciudad Universitaria'] = 5
    heuristics['Villa Mella'] = 11
    heuristics['Arroyo Hondo'] = 5
    heuristics['Las Praderas'] = 6
    heuristics['Alma Rosa'] = 11
    heuristics['Capotillo'] = 5
    heuristics['Bella Vista'] = 5  
        
    # Imprimimos los nodos
    graph.printgraph()
    print("--------------------------------\n\n")
    
    path_1 = input("Ingrese punto de partida: ")
    path_2 = input("Ingrese punto de llegada: ")

    # Ejecutamos el A*
    path = A_Star(graph, heuristics, path_1, path_2)
    print("PATH: ", end = " ")
    print(path)

# Tell python to run main method
if __name__ == "__main__": main()