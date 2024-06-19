import sys
sys.path.append('../')
#from controls.calculos import Calculos
#from controls.tdaArray import TDAArray
from controls.tda.stack.stackOperation import StackOperation
from controls.tda.linked.linkedList import Linked_List

import random
import time


c=StackOperation(20)
lista = Linked_List()

try:

   #for i in range(10000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,0)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")

   #for i in range(10000):
   #      lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,1)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")
   #for i in range(10000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,2)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")

   #for i in range(20000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,0)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")

   #for i in range(20000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,1)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")
   #for i in range(20000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,2)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")
   #for i in range(25000):
   #    lista.add(round(random.random()*100,2))
   #    inicio = time.time()
   #    lista.sort(1,1) 
   #     fin = time.time()
   #     print(f"Tiempo de ejecucion: {fin - inicio}")
   #     print("---------------------------------------------------------")

   #for i in range(25000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,1)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")
   #for i in range(25000):
    #    lista.add(round(random.random()*100,2))
    #    inicio = time.time()
    #    lista.sort(1,2)
    #    fin = time.time()
    #    print(f"Tiempo de ejecucion: {fin - inicio}")
    #    print("---------------------------------------------------------")

    


   c.print()
except Exception as error:
   print("errores")
   print(error)

json_data = c.to_json()
print(json_data)




