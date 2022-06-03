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