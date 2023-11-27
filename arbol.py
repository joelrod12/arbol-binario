class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)


    def insertar(self, valor):
        self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        if self._buscar_recursivo(self.raiz, valor):
            return f"El nombre {valor} esta en el arbol."
        else:
            return f"El nombre {valor} no esta en el arbol."

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

# Ejemplo de uso:
arbol = Arbol("pablo")
arbol.insertar("isaac")
arbol.insertar("freddy")
arbol.insertar("jesus")

print(arbol.buscar("jesus")) 
print(arbol.buscar("isaac")) 
print(arbol.buscar("jose"))