Arreglo=[4,8,75,9,25,64]
import copy
import time
import random
Arreglo_arreglos=[[0 for _ in range(10)],
                  [0 for _ in range(100)],
                  [0 for _ in range(1000)],
                  [0 for _ in range(10000)],
                  [0 for _ in range(100000)],]
i=0
while i<len(Arreglo_arreglos):
    j=0
    while j<len(Arreglo_arreglos[i]):
        Arreglo_arreglos[i][j]=random.randint(0, 10000000)
        j+=1
    i+=1
    
matriz_resultados = [[0.0 for _ in range(5)] for _ in range(5)]

def burbuja(Arreglo):
    i=0
    while i<len(Arreglo)-1:
        i+=1
        j=0
        while j<len(Arreglo)-1:
            if Arreglo[j]>Arreglo[j+1]:
                aux=Arreglo[j]
                Arreglo[j]=Arreglo[j+1]
                Arreglo[j+1]= aux
            j+=1
def burbuja_mejorada(Arreglo):
    i=0
    while i<len(Arreglo)-1:
        
        j=0
        while j<len(Arreglo)-1 -i:
            if Arreglo[j]>Arreglo[j+1]:
                aux=Arreglo[j]
                Arreglo[j]=Arreglo[j+1]
                Arreglo[j+1]= aux
            j+=1
        i+=1
def quicksort (Arreglo, Inicio, Final):
    inicio= Inicio
    final= Final
    if inicio<final :
        while inicio<final:
            hubo_intercambio=False
            while not hubo_intercambio and inicio<final:
                if Arreglo[inicio]>Arreglo[final]:
                    aux=Arreglo[final]
                    Arreglo[final]=Arreglo[inicio]
                    Arreglo[inicio]= aux
                    hubo_intercambio=True
                else:
                    final-=1
                    
                    
            hubo_intercambio=False
            while not hubo_intercambio and inicio<final:
                if Arreglo[inicio]>Arreglo[final]:
                    aux=Arreglo[final]
                    Arreglo[final]=Arreglo[inicio]
                    Arreglo[inicio]= aux
                    hubo_intercambio=True
                else:
                    inicio+=1
        quicksort(Arreglo,inicio+1,Final)
        quicksort(Arreglo,Inicio,final-1)
def insercion (Arreglo):
    i=1
    while i<len(Arreglo):
        j=i
        while j>0 and Arreglo[j]<Arreglo[j-1]:
            aux=Arreglo[j]
            Arreglo[j]=Arreglo[j-1]
            Arreglo[j-1]=aux
            j-=1
        i+=1        
def seleccion(Arreglo):
    i=0
    while i<len(Arreglo)-1:
        j=i
        aux=i
        while j<len(Arreglo):
            if Arreglo[aux]>Arreglo[j]:
                aux=j
            
            j+=1
        tmp=Arreglo[aux]
        Arreglo[aux]=Arreglo[i]
        Arreglo[i]=tmp
        i+=1
def mergesort(Arreglo):
    if len(Arreglo) > 1:

        mid = len(Arreglo) // 2
        Lado_derecho= Arreglo[:mid]
        Lado_Izquiedo = Arreglo[mid:]
        mergesort(Lado_derecho)
        mergesort(Lado_Izquiedo)

        i = j = k = 0

        while i < len(Lado_Izquiedo) and j < len(Lado_derecho):
            if Lado_Izquiedo[i] < Lado_derecho[j]:
                Arreglo[k] = Lado_Izquiedo[i]
                i += 1
            else:
                Arreglo[k] = Lado_derecho[j]
                j += 1
            k += 1

        while i < len(Lado_Izquiedo):
            Arreglo[k] = Lado_Izquiedo[i]
            i += 1
            k += 1

        while j < len(Lado_derecho):
            Arreglo[k] = Lado_Izquiedo[j]
            j += 1
            k += 1


i=0
while i<len(Arreglo_arreglos):
    aux= Arreglo_arreglos[i][:]

    inicio=time.perf_counter()
    burbuja(aux)
    fin=time.perf_counter()
    matriz_resultados[i][0]= fin-inicio
    
    aux= Arreglo_arreglos[i][:]
    inicio=time.perf_counter()
    insercion(aux)
    fin=time.perf_counter()
    matriz_resultados[i][1]= fin-inicio
    
    aux= Arreglo_arreglos[i][:]
    inicio=time.perf_counter()
    seleccion(aux)
    fin=time.perf_counter()
    matriz_resultados[i][2]= fin-inicio
    
    aux= Arreglo_arreglos[i][:]
    inicio=time.perf_counter()
    mergesort(aux)
    fin=time.perf_counter()
    matriz_resultados[i][3]= fin-inicio
    print(1)
    i+=1
print(matriz_resultados)
                
                
                
        
        

                