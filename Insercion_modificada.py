import random
Arr=[0 for _ in range(100)]
i=0
while i<len(Arr):
    Arr[i]=random.randint(0,500)
    i+=1
def busqueda_posición(Arreglo, posicion_final, valor_buscado):
    
    posicion_inicial=0
    no_encontrado=True
    pivote=0
    while posicion_final>=posicion_inicial and no_encontrado:
        pivote=posicion_inicial+((posicion_final - posicion_inicial)//2)

        if Arreglo[pivote]== valor_buscado:
            no_encontrado=False
        elif Arreglo[pivote]>valor_buscado:
            posicion_final=pivote-1
        else:
            posicion_inicial=pivote+1
    if Arreglo[pivote]<valor_buscado:
        pivote+=1
    return pivote

def inserta_en(Arreglo, lugar_a_insertar, lugar_del_dato):
    aux=Arreglo[lugar_del_dato]
    iterador=lugar_del_dato
    while iterador>lugar_a_insertar:
        Arreglo[iterador]=Arreglo[iterador-1]
        iterador-=1
    Arreglo[lugar_a_insertar]=aux

def ordena(Arreglo):
    i=1
    while i<len(Arreglo):
        lugar_dato=busqueda_posición(Arreglo,i-1,Arreglo[i])
        inserta_en(Arreglo,lugar_dato,i)
        i+=1


ordena(Arr)
print(Arr)
     

