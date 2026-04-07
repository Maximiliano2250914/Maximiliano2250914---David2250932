class Nodo:
    def __init__(self, data):
        self.data=data
        self.siguiente=None
        
class ListaSE:
    def __init__(self):
        self.cabeza=None
    
    def agregarInicio(self,data):
        nuevo=Nodo(data)
        if self.cabeza is None:
            self.cabeza=nuevo
            return
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza=nuevo
            return
    
    def imprimir(self):
        actual=self.cabeza
        while actual is not None:
            print(actual.data)
            actual=actual.siguiente
        
arbolito=ListaSE()
nodo1=ListaSE()

nodo1.agregarInicio(5)
arbolito.agregarInicio(nodo1)
arbolito.imprimir()
