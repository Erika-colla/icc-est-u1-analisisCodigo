class MetodoOrdenamiento:
    
    def sort_bubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):  
            for j in range(0, n - i - 1): 
                if arreglo[j] > arreglo[j + 1]:  
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo 

    def sort_seleccion(self, arreglo): 
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
            arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
        return arreglo