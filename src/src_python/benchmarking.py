import random
import time
import metodosordenamiento  

class Benchmarking:
    def __init__(self):
        print("Bench inicializando")

    def ejemplo(self): 
        self.mOrdenamiento = metodosordenamiento.MetodoOrdenamiento()  
        self.arreglo = self.build_arreglo(50000)  

        tarea = lambda: self.mOrdenamiento.sortByBubble(self.arreglo)
        
        tiempoMillis = self.contar_con_current_time_millies(tarea)
        print(tiempoMillis, "milisegundos")
        
        tiempoNano = self.contar_con_nano_time(tarea)
        print(tiempoNano, "milisegundos")
    
    def build_arreglo(self, size):
        return [random.randint(0, 99999) for _ in range(size)]

    def contar_con_current_time_millies(self, tarea):
        inicio = time.time()
        tarea()  
        fin = time.time()
        return (fin - inicio) * 1000 

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns() 
        tarea()  
        fin = time.time_ns()  
        return (fin - inicio) / 1_000_000  
    
    def medir_tiempo(self,tarea,array):
        inicio=time.perf_counter()
        tarea(array)
        fin= time.perf_counter()
        return fin - inicio