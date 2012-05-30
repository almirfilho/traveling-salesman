from classe_vertex import Vertex
from classe_edge import Edge
import math
import time

class Graph:
    
    # Atributos: -----------------------------------------
    
    vertexes    = None  # Lista com todos os vertices do grafo
    edges       = None  # Lista com todas as arestas do grafo
    bestCost    = 10000000
    stack       = []
    atualCost   = 0
    lenVertexes = None
    matrix      = None
    
    
    # Construtor: ----------------------------------------
    
    def __init__( self, file = None ):
        
        self.vertexes   = []
        self.edges      = []
        self.matrix     = {}
        
        if file != None:
            self.__buildByFile( file )
        
        self.lenVertexes = len( self.vertexes )
            
    # Metodos: -------------------------------------------
    
    def __buildByFile( self, file ):
        """
        Constroi o grafo a partir de um arquivo informado.
        """
        file = open( file, 'r' )  # abre arquivo em modo leitura
        # retorna uma lista com strings separadas para cada linha lida do arquivo:
        lines = [ line.rstrip( '\n' ).split( ' ' ) for line in file.readlines() ]
        # apenas converte todos os numeros de coordenadas da lista para inteiros:
        lines = [ [ int(line[0]), int(line[1]), int(line[2]) ] for line in lines ]
        # cria e adiciona todos os vertices a lista:
        for line in lines:
            self.vertexes.append( Vertex ( line[0] ) )
            self.matrix[ line[0] ] = {}
        
        # calculando os custos e criando todas as arestas do grafo:
        v = [] # criando copia da lista de vertices:
        for vertex in self.vertexes: v.append( vertex )
        
        for vertexIni in self.vertexes:
            if vertexIni in v:
                v.remove( vertexIni )
                coordinates = ( lines[ vertexIni.label-1 ][1], lines[ vertexIni.label-1 ][2] )
                for vertexEnd in v:
                    distance = math.sqrt( ( lines[ vertexIni.label-1 ][1] - lines[ vertexEnd.label-1 ][1] )**2 + ( lines[ vertexIni.label-1 ][2] - lines[ vertexEnd.label-1 ][2] )**2 )
                    edge = Edge( vertexIni, vertexEnd, distance )
                    self.edges.append( edge )
                    vertexIni.adjacenses.append( edge )
                    edge = Edge( vertexEnd, vertexIni, distance ) #add esse
                    vertexEnd.adjacenses.append( edge )
                    self.matrix[ vertexIni.label ][ vertexEnd.label ] = distance
                    self.matrix[ vertexEnd.label ][ vertexIni.label ] = distance
                self.sortEdges( vertexIni.adjacenses )
        
        self.sortEdges( self.edges )  # ordenando todas as arestas do grafo
        print 'grafo clique com', len( self.vertexes ), 'cidades criado.'
    
    def sortEdges( self, listEdges ):
        """
        Ordena todas as arestas do grafo pela ordem de custo crescente. ordenacao bolha.
        """
        changed = True
        while changed:
            changed = False
            for i in range( len(listEdges)-1 ):
                if listEdges[ i ].cost > listEdges[ i+1 ].cost:
                    changed = True
                    aux = listEdges[ i ]
                    listEdges[ i ] = listEdges[ i+1 ]
                    listEdges[ i+1 ] = aux
    
    def findHamiltonianCircle( self, vertexIni ):
        
        vertexIni.visited = True  # visita o vertice
        self.stack.append( vertexIni )  # empilha o vertice
        
        for edge in vertexIni.adjacenses:
            if edge.vertex1.visited:
                continue
            elif self.atualCost + edge.cost < self.bestCost:
                self.atualCost += edge.cost
                self.findHamiltonianCircle( edge.vertex1 )
                edge.vertex1.visited = False
                self.stack.pop()
                self.atualCost -= edge.cost
            
        # se nao houver adjacencias:
        if len( self.stack ) == self.lenVertexes:
            self.atualCost += self.matrix[ self.stack[0].label ][ self.stack[-1].label ]
            if self.atualCost < self.bestCost:
                self.bestCost = self.atualCost
                print [ v.label for v in self.stack ], ", c:", self.bestCost, ", t:", time.clock()
            self.atualCost -= self.matrix[ self.stack[0].label ][ self.stack[-1].label ]

    def getMatrixPath( self, matrixAdj ):
        
        matrixPath = matrixAdj.copy()
        
        for k in matrixPath.iterkeys():
            for i in matrixPath[ k ]:
                i = 0   # matriz caminho inicialmente eh nula.
        
        matrixAux = matrixAdj.copy()
        
        for i in range( 1, len( matrixAdj ) ):
            matrixAux = self.matrixMult( matrixAux, matrixAdj )
            matrixPath = self.matrixSum( matrixPath, matrixAux )
        
        return matrixPath
    
    def matrixMult( self, matrix0, matrix1 ):
        """
        retorna uma matriz resultado da multiplicacao entre duas matrizes dadas.
        """
        result = {}
        keys   = sorted( set( matrix0.keys() ) )
        count  = range( len( matrix0.keys() ) )
        
        for key in keys:
            result[ key ] = []
            for i in count:
                sum = 0
                for j in count:
                    sum += matrix0[ key ][j] * matrix1[ keys[j] ][i]
                result[ key ].insert( i, sum )
        
        return result
    
    def matrixSum( self, matrix0, matrix1 ):
        """
        retorna uma matriz resultado da soma entre duas matrizes dadas.
        """
        result = {}
        keys   = sorted( set( matrix0.keys() ) )
        count  = range( len( matrix0.keys() ) )
        
        for key in keys:
            result[ key ] = []
            for i in count:
                soma = matrix0[ key ][ i ] + matrix1[ key ][ i ]
                result[ key ].append( soma )
        
        return result