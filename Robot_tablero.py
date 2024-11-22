

laberinto= [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]


def Llega_salida(matriz):
    if len(matriz)%2==0 and len(matriz[1])%3==0:
        return True
    else:
        return False 

def Encuentra_salida(Matriz):
    if Llega_salida(Matriz):
        i=0
        while i<len(Matriz):
            
            Matriz[i][0]=1
            
            i+=1
        i=0
        while i<len(Matriz[1]):
            
            Matriz[-1][i]=1
            
            i+=1

def Cuenta_caminos(Matriz, x,y):
    num_caminos=0
    if x<len(Matriz[1]):
        num_caminos+=Cuenta_caminos(Matriz,x+3,y)
    if y<len(Matriz):
        num_caminos+=Cuenta_caminos(Matriz,x,y+2)
    if y==len(Matriz)and x==len(Matriz[1]):
        num_caminos=1
    return num_caminos
    
        


if Llega_salida(laberinto):
    Encuentra_salida(laberinto)
    for fila in laberinto:
        print(fila) 
    print("la cantidad de caminos es")  
    print(Cuenta_caminos(laberinto,0,0))
else:
    print("no hay salida")
    







