import math
import random
import copy
def leer_coordenadas(nombre_archivo):
    coordenadas = []

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                
                x, y = map(int, linea.split())
                
                
                if x == -1 and y == -1:
                    break
                
                coordenadas.append(poste(x, y))

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except ValueError:
        print("El archivo contiene datos inválidos.")
    
    return coordenadas

def escribir_coordenadas(nombre_archivo, postes):
    try:
        with open(nombre_archivo, "w") as archivo:
            i=0
            while i<len(postes):
                archivo.write(f"{postes[i].posicion_x} {y} \n")
                i+=1
        print(f"Archivo de salida '{nombre_archivo}' generado correctamente.")
    except IOError:
        print(f"No se pudo escribir el archivo '{nombre_archivo}'.")

class poste:
    def __init__(self,posicion_x,posicion_y):
        self.posicion_x=posicion_x
        self.posicion_y=posicion_y

def base(punto1,punto2):
    base=math.sqrt((punto1.posicion_x - punto2.posicion_x)**2 + (punto1.posicion_y - punto2.posicion_y)**2)

    
    return base
def altura(punto1,punto2,punto3):
    if punto1.posicion_x != punto2.posicion_x:
        
        pendiente=(punto1.posicion_y - punto2.posicion_y)/(punto1.posicion_x - punto2.posicion_x)
        distancia=abs(pendiente*punto3.posicion_x - punto3.posicion_y - pendiente*punto1.posicion_x + punto1.posicion_y)/math.sqrt(pendiente**2 + 1)
    else:
        distancia=abs(punto3.posicion_x-punto1.posicion_x)
    
    return distancia
def area_postes(poste1, poste2, poste3):
    if poste1.posicion_x == poste2.posicion_x and poste1.posicion_y == poste2.posicion_y:
        return 0
    else:
        Base=base(poste1,poste2)

        Altura=altura (poste1, poste2, poste3)
    
        return Base*Altura/2

def encuentra_area_bruta(Arreglo_poste):
    i=0
    area_mayor=0
    postes_del_area=[0,0,0]
    while i<len(Arreglo_poste)-2:
        j=i+1
        while j<len(Arreglo_poste)-1:
            k=j+1
            while k<len(Arreglo_poste):
                area_cal=area_postes(Arreglo_poste[i],Arreglo_poste[j],Arreglo_poste[k])
                if area_cal>area_mayor:
                    area_mayor=area_cal
                    postes_del_area[0]=i
                    postes_del_area[1]=j
                    postes_del_area[2]=k
                    
                
                
                k+=1
            j+=1
        
        i+=1
    print(area_mayor)
    print("los postes son")
    print(postes_del_area)
Arr_postes=[]
z=0
while z<500:
    x=random.randint(1,999)
    y=random.randint(1,999)
    Arr_postes.append(poste(x,y))
    z+=1





def postes_cercanos(poste, arreglo_postes):
    i=0
    postes=[0 for i in range(10)]
    distancias=[1000,1000,1000,1000,1000]
    while i<len(arreglo_postes):
        distancia_aux=base(poste,arreglo_postes[i])
        if distancia_aux<distancias[0]:
            postes[0]=i
            distancias[0]=distancia_aux
            j=0
            while j<len(distancias)-1 and distancias[j]<distancias[j+1]:
                aux=distancias[j]
                distancias[j]=distancias[j+1]
                distancias[j+1]=aux
                aux=postes[j]
                postes[j]=postes[j+1]
                postes[j+1]=aux
                j+=1
        i+=1

    return postes


def diez_mas_derecha(arreglo_postes):
    postes=[0 for _ in range(10)]
    poste_aux=poste(arreglo_postes[0].posicion_x, arreglo_postes[0].posicion_y)
    arreglo_postes[0].posicion_x=0
    
    i=0
    while i<len(arreglo_postes):
        if arreglo_postes[postes[0]].posicion_x <arreglo_postes[i].posicion_x:
            postes[0]=i
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_x > arreglo_postes[postes[j+1]].posicion_x:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
        i+=1
    arreglo_postes[0].posicion_x = poste_aux.posicion_x
    if arreglo_postes[postes[0]].posicion_x <arreglo_postes[0].posicion_x:
            postes[0]=0
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_x > arreglo_postes[postes[j+1]].posicion_x:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
    return postes

def diez_mas_izquierda(arreglo_postes):
    postes=[0 for _ in range(10)]
    poste_aux=poste(arreglo_postes[0].posicion_x, arreglo_postes[0].posicion_y)
    arreglo_postes[0].posicion_x=1000
    i=0
    while i<len(arreglo_postes):
        if arreglo_postes[postes[0]].posicion_x > arreglo_postes[i].posicion_x:
            postes[0]=i
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_x < arreglo_postes[postes[j+1]].posicion_x:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
        i+=1
    arreglo_postes[0].posicion_x=poste_aux.posicion_x
    if arreglo_postes[postes[0]].posicion_x > arreglo_postes[0].posicion_x:
            postes[0]=0
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_x < arreglo_postes[postes[j+1]].posicion_x:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
    return postes

def diez_mas_arriba(arreglo_postes):
    postes=[0 for _ in range(10)]
    poste_aux=poste(arreglo_postes[0].posicion_x, arreglo_postes[0].posicion_y)
    arreglo_postes[0].posicion_y=0
    i=0
    while i<len(arreglo_postes):
        if arreglo_postes[postes[0]].posicion_y <arreglo_postes[i].posicion_y:
            postes[0]=i
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_y > arreglo_postes[postes[j+1]].posicion_y:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
        i+=1
    arreglo_postes[0].posicion_y=poste_aux.posicion_y
    if arreglo_postes[postes[0]].posicion_y <arreglo_postes[0].posicion_y:
            postes[0]=0
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_y > arreglo_postes[postes[j+1]].posicion_y:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
    return postes

def diez_mas_abajo(arreglo_postes):
    postes=[0 for _ in range(10)]
    poste_aux=poste(arreglo_postes[0].posicion_x, arreglo_postes[0].posicion_y)
    arreglo_postes[0].posicion_y=1000
    i=0
    while i<len(arreglo_postes):
        if arreglo_postes[postes[0]].posicion_y >arreglo_postes[i].posicion_y:
            postes[0]=i
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_y < arreglo_postes[postes[j+1]].posicion_y:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
        i+=1
    arreglo_postes[0].posicion_y=poste_aux.posicion_y
    if arreglo_postes[postes[0]].posicion_y >arreglo_postes[0].posicion_y:
            postes[0]=0
            j=0
            while j<len(postes)-1:
                if arreglo_postes[postes[j]].posicion_y < arreglo_postes[postes[j+1]].posicion_y:
                    aux=postes[j+1]
                    postes[j+1]=postes[j]
                    postes[j]=aux
                j+=1
    return postes

def encuentra_area_bruta2(Arreglo_poste, Arreglo_pst, Arr_poste,Arr_pst):
    i=0
    area_mayor=0
    postes_del_area=[0,0,0,0]
    while i<len(Arr_pst):
        j=0
        while j<len(Arreglo_pst):
            k=0
            while k<len(Arr_poste):
                area_cal=area_postes(Arreglo_poste[Arr_pst[i]], Arreglo_poste[Arreglo_pst[j]], Arreglo_poste[Arr_poste[k]])
                if area_cal>area_mayor:
                    area_mayor=area_cal
                    postes_del_area[0]=Arr_pst[i]
                    postes_del_area[1]=Arreglo_pst[j]
                    postes_del_area[2]=Arr_poste[k]
                    postes_del_area[3]=area_mayor
                    
                
                
                k+=1
            j+=1
        
        i+=1

    return postes_del_area

def encuentra_mejorado(Arreglo_poste):
    poste_inferior_izquierdo=poste(0,0)
    poste_inferior_derecho=poste(1000,0)
    poste_superior_izquierdo=poste(0,1000)
    poste_superior_derecho=poste(1000,1000)
    cercanos_izq_inf=postes_cercanos(poste_inferior_izquierdo,Arreglo_poste)
    cercanos_izq_sup=postes_cercanos(poste_superior_izquierdo,Arreglo_poste)
    cercanos_der_inf=postes_cercanos(poste_inferior_derecho,Arreglo_poste)
    cercanos_der_sup=postes_cercanos(poste_superior_derecho,Arreglo_poste)
    
    superiores=diez_mas_arriba(Arreglo_poste)
    inferiores=diez_mas_abajo(Arreglo_poste)
    derechos=diez_mas_derecha(Arreglo_poste)
    izquierdos=diez_mas_izquierda(Arr_postes)
    
    
    area_mayor=encuentra_area_bruta2(Arreglo_poste, cercanos_izq_inf, cercanos_der_inf, superiores)
    aux=encuentra_area_bruta2(Arreglo_poste, cercanos_izq_inf, cercanos_izq_sup, derechos)
    if area_mayor[3]<aux[3]:
    
        area_mayor=copy.copy(aux)

    aux=encuentra_area_bruta2(Arreglo_poste, cercanos_der_sup, cercanos_der_inf, izquierdos)
    if area_mayor[3]<aux[3]:
    
        area_mayor=copy.copy(aux)

    aux=encuentra_area_bruta2(Arreglo_poste, cercanos_izq_sup, cercanos_der_sup, inferiores)
    if area_mayor[3]<aux[3]:
    
        area_mayor=copy.copy(aux)

    coordenada_post=[]
    coordenada_post.append(Arreglo_poste[area_mayor[0]])
    coordenada_post.append(Arreglo_poste[area_mayor[1]])
    coordenada_post.append(Arreglo_poste[area_mayor[2]])
    
    escribir_coordenadas("campo.out", coordenada_post)

    
    
postes_coor=leer_coordenadas("campo.in")
 
encuentra_mejorado(Arr_postes)


