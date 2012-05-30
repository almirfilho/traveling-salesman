import time
from getopt import os
from classe_graph import Graph

g = Graph( "in2.txt")

#------------------------------------------------
#        TESTE PARA CAXEIRO:
#------------------------------------------------
#time.clock()
#
#g.findHamiltonianCircle( g.edges[0].vertex1 )
#
#print g.bestCost, time.clock()
#
#os.system( "pause" )

#------------------------------------------------
#        TESTE PARA MATRIZ CAMINHO:
#------------------------------------------------
#ma = {
#      "A": [0,1,0],
#      "B": [1,0,1],
#      "C": [0,1,0]
#      }
#
#r = g.getMatrixPath( ma )
#
#for i in sorted( r.iteritems() ):
#    print i