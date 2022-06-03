'''
Autor: Carlos Lucio
Para comenzar con la generación de los métodos de busqueda necesitaremos de las librerias necesarias
En python los metodos de busqueda se puede asociar con la teoria de Grafos.
Es por ello que para crear la clase Grafos
Importaremos la libreria Queue para generar listas en el programa
'''
#Importamos la libreria Queue
from queue import Queue

class Grafo():
    '''
    Creación de la clase Grafo para instanciar el objeto y generar nodos
    Esta clase contiene sus atributos y funciones que permiten generar
    el grafo deseado

    Atributos:
        m_numero_de_nodos: int
            Representa la cantidad de nodos que tendra el grafo
        m_nodos: int
            Representa el rango de nodos que tendra el grafo
        m_dirigido: bool
            Representa si el grafo es dirigido o no
        m_adyacencia_lista: dict
            Representa al diccionario de datos que almacena los nodos 
    
    Métodos:
        __init__(self, numero_de_nodos, dirigido=True):
            Constructor de la clase Grafo
        añadir_nodo(self, nodo1, nodo2, peso=1):
            Funcion que recibe por parámetro los nodos e ingresa los nodos a la lista
            en sus respectivas listas
        mostrar_lista_adyacencia(self):
            Funcion que permite mostrar la lista de adyacencia
        def dfs(self, nodo_de_inicio, objetivo, camino = [], visitado = set()):
            Funcion que permite realizar el recorrido en anchura en base a un 
            vértice dado

    '''
    def __init__(self, numero_de_nodos, dirigido=True):

        '''
        Este metodo permite instanciar el objeto de la clase Grafo por medio 
        Por medio de parámetros de entrada recibe el numero de nodos e indica 
        si el grafo es dirigido o no
        --------------------------------------------------------------
        Parametros(self, numero_de_nodos, dirigido=True):
            numero_de_nodos: int
                Representa el numero de nodos que tendra el grafo
            dirigido: bool
                Representa si el grafo es dirigido o no
        Retorna:
            No retorna nada
        --------------------------------------------------------------
        '''
        #Asignación del numero de nodos a nodo recibido por parámetro
        self.m_numero_de_nodos = numero_de_nodos 
        '''
        Esta variable determinar el rango de nodos que tendra el grafo
        enviando como parámetro la variable generada nodo.matriz_numero_de_nodos
        '''
        #Mide el rango de nodos
        self.m_nodos = range(self.m_numero_de_nodos) 
		
        #Dirigido o No Dirigido
        self.m_dirigido = dirigido
        '''
        Esta asignación representa la creación de un diccionario de datos
        Este determina el espacio en donde se almacenarán los nodos
        '''
        self.m_adyacencia_lista = {self: set() for self in self.m_nodos}     

    #Añade un nodo al grafo
    def añadir_nodo(self, nodo1, nodo2, peso=1):
        '''
        Funcion que recibe por parámetro los nodos 1 y 2, además del peso
        Asigna cada uno de los nodos a la lista de adyacencia.

        Parametros: (self, nodo1, nodo2, peso=1)
            nodo1: int
                Representa el nodo 1
            nodo2: int
                Representa el nodo 2
            peso: int
                Representa el peso de la arista
        Retorna:
            No retorna nada
        '''
        #Ingreso del nodo2 a la lista de adyacencia del nodo1
        self.m_adyacencia_lista[nodo1].add((nodo2, peso))
        #Estructura condicional en caso de que no sea dirigido
        if not self.m_dirigido: 
            #Ingreso del nodo1 a la lista de adyacencia del nodo2
            self.m_adyacencia_lista[nodo2].add((nodo1, peso)) #Añadir el nodo1 a la lista de adyacencia del nodo2

    # Imprime la representación del grafo
    def mostrar_lista_adyacencia(self):
        '''
        Muestra el grafo generado por parte de una clave a través de la lista de adyacencia
        Parametros():
            No recibe parámetros
        Retorna:
            No retorna nada
        '''
        #Generacion del ciclo for que permite recorrer el tamaño del nodo
        for clave in self.m_adyacencia_lista.keys(): 
            #Muestra en la terminal el grafo
            print("Nodo", clave, ": ", self.m_adyacencia_lista[clave]) 

    #Recorrido en amplitud
    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Esta funcion permite realizar el recorrido en anchura en base a un
        vértice dado y el objetivo a encontrar en el grafo generado 
         
        Parametros:
            ruta: lista
                Representa el nodo de inicio del recorrido
            visitado: diccionario
                Representa al diccionario de datos

        Retorna:
            No retorna nada
        """
        #Se añade a la ruta el nodo inicial
        ruta.append(inicio) 
        #Se añade a la la lista de nodos visitados el nodo inicial
        visitado.add(inicio) 
         #Si inicio es igual a objetivo
        '''
            Este condicional permite determinar si el nodo inicio es igual al objetivo
            en caso de que sea igual se imprime la ruta
        '''
        if inicio == objetivo: 
            return ruta #Retorna la ruta
        ''' 
            Esta estructura ciclica permite recorrer la lista de adyacencia
            de cada nodo
            Si el vecino no es visitado se realiza el recorrido en anchura
            Si el resultado del recorrido en anchura no es nulo se retorna el resultado
        '''
        for(vecino, peso) in self.m_adyacencia_lista[inicio]: 
            if vecino not in visitado:  #Si el vecino no se encuentra en el diccionario de nodos visitados
                resultado = self.dfs(vecino, objetivo, ruta, visitado) #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                #Si la lista resultado no esta vacio
                if resultado is not None: 
                    return resultado #Retorna resultado
                    
        '''
        Implementación de la función recursiva dfs
        '''
        ruta.pop() # elimina y retorna el elemento de la ruta
        return None 

if __name__ == "__main__":
    '''
     #Creación del grafo
    grafo = Grafo(5, dirigido=False)

    #Añadir nodos al grafo
    grafo.añadir_nodo(0, 1)
    grafo.añadir_nodo(0, 2)
    grafo.añadir_nodo(1, 3)
    grafo.añadir_nodo(2, 3)
    grafo.añadir_nodo(3, 4)

    #Mostrar la lista de adyacencia
    grafo.mostrar_lista_adyacencia()

    ruta_transversal = []
    ruta_transversal = grafo.dfs(0, 3)
    print(f" La ruta trasversal desde el nodo 0 hasta el nodo 3 es {ruta_transversal}")
    
    print("--------------------------------------------")
    print("Implementación de un nuevo grafo para el caso 1")
    grafo1 = Grafo(4, True)
    #Añadir nodos al grafo
    grafo1.añadir_nodo(0, 1)
    grafo1.añadir_nodo(0, 2)
    grafo1.añadir_nodo(0, 3)
    grafo1.añadir_nodo(1, 2)
    grafo1.añadir_nodo(1, 3)
    grafo1.añadir_nodo(2, 3)
    grafo1.añadir_nodo(3, 1)
    #Mostrar la lista de adyacencia
    grafo1.mostrar_lista_adyacencia()
    #Generar la ruta transversal
    ruta_transversal1 = []
    ruta_transversal1 = grafo1.dfs(0, 3)
    print(f" La ruta trasversal desde el nodo 0 hasta el nodo 3 es {ruta_transversal1}")
    
    #Creación del grafo
    print("--------------------------------------------")
    print("Implementación de un nuevo grafo para el caso 2")
    g2 = Grafo(8, dirigido=True)
    #Agregue bordes al grafo con peso predeterminado = 1
    g2.añadir_nodo(0, 1)
    g2.añadir_nodo(0, 5)
    g2.añadir_nodo(1, 5)
    g2.añadir_nodo(2, 1)
    g2.añadir_nodo(2, 5)
    g2.añadir_nodo(2, 4)
    g2.añadir_nodo(3, 4)
    g2.añadir_nodo(3, 7)
    g2.añadir_nodo(4, 2)
    g2.añadir_nodo(5, 3)
    g2.añadir_nodo(5, 4)
    g2.añadir_nodo(6, 3)
    g2.añadir_nodo(6, 7)
    g2.añadir_nodo(7, 6)

    #Mostrar la lista de adyacencia
    g2.mostrar_lista_adyacencia()

    #Generar la ruta transversal
    ruta_transversal2 = []
    ruta_transversal2 = g2.dfs(0, 7)
    print(f" La ruta trasversal desde el nodo 0 hasta el nodo 7 es {ruta_transversal2}")
    '''
    #Creación del grafo
    print("--------------------------------------------")
    print("Implementación de un nuevo grafo para el caso 3")
    #Instanciamos el nuevo objeto
    g3 = Grafo(3, dirigido=True)
    #Agregue bordes al grafo con peso predeterminado = 1
    g3.añadir_nodo(0, 1, 3)
    g3.añadir_nodo(0, 2, 2)
    g3.añadir_nodo(1, 2, 5)
    g3.añadir_nodo(2, 0, 4)
    #Imprime el grafo generado en el formulario nodo n: {(nodo, peso)}
    g3.mostrar_lista_adyacencia()
    #Generar la ruta transversal
    ruta_transversal3 = []
    ruta_transversal3 = g3.dfs(0, 2)
    print(f" La ruta trasversal desde el nodo 0 hasta el nodo 2 es {ruta_transversal3}")

