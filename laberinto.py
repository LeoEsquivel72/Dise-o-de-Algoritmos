laberinto= [
    [1,1,1,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]
]
entrada=[2,1]
salida=[0,3]
encontrado=False
def encuentrasalida(labe,posicion_inicial, salida, salida_encontrada):
    labe[posicion_inicial[0]] [posicion_inicial[1]]=2
    if(posicion_inicial[0]==salida[0] and posicion_inicial[1]==salida[1]):
        salida_encontrada=True
   
      
    if(not salida_encontrada):
        if posicion_inicial[0]>0:
            if labe[posicion_inicial[0]-1][posicion_inicial[1]]==0:
                nuevaposicion=[posicion_inicial[0]-1, posicion_inicial[1]]
                
                salida_encontrada= encuentrasalida(labe,nuevaposicion, salida, salida_encontrada)
                    
                
        if posicion_inicial[0]<3 and not salida_encontrada:
            if labe[posicion_inicial[0]+1] [posicion_inicial[1]]==0:
                nuevaposicion=[posicion_inicial[0]+1, posicion_inicial[1]]
                salida_encontrada= encuentrasalida(labe,nuevaposicion, salida, salida_encontrada)
                 
        if posicion_inicial[1]>0 and not salida_encontrada:
            if labe[posicion_inicial[0]] [posicion_inicial[1]-1]==0:
                nuevaposicion=[posicion_inicial[0], posicion_inicial[1]-1]
                
                salida_encontrada= encuentrasalida(labe,nuevaposicion, salida, salida_encontrada)
        
                     
        if posicion_inicial[1]<=2 and not salida_encontrada:
            if labe[posicion_inicial[0]][posicion_inicial[1]+1]==0:
                
                nuevaposicion=[posicion_inicial[0], posicion_inicial[1]+1]
                salida_encontrada= encuentrasalida(labe,nuevaposicion, salida, salida_encontrada)
    if salida_encontrada:
          labe[posicion_inicial[0]][posicion_inicial[1]]=5          
    return salida_encontrada




if encuentrasalida(laberinto,entrada,salida,encontrado):
    print("se ha encontrado la salida \n")
else:
    print("no se encontró salida \n")
for fila in laberinto:
    print(fila)        
            
