class Edge:
    
    # Atributos: -------------------------------------
    
    vertex0 = None  
    vertex1 = None  
    cost    = None  
    
    # Construtor: ------------------------------------
    
    def __init__( self, vertex0, vertex1, cost ):
        
        self.vertex0    =   vertex0
        self.vertex1    =   vertex1
        self.cost       =   cost
