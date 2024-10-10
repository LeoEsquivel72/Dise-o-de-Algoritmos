import random
arreglo = [-9,3,5,-2,9,-7,4,8,6]
numero1= 0
numero2=0
mult=0
mayor=0
for elemento in range(len(arreglo)-2):
    aux = elemento +1
    while aux < (len(arreglo)-1):
        mult= arreglo[elemento]* arreglo[aux]
        if elemento ==0 :
           mayor = mult
           numero1= elemento
           numero2 = aux
        elif mult > mayor:
            mayor = mult
            numero1=elemento
            numero2 = aux
        aux+=1
            

print(f"El número más grande que se pude hacer es {mayor} producto de {arreglo[numero1]} , {arreglo[numero2]}")



generavalor = int(input("que valor quieres formar: "))

monedas = [1,2,5,10]

contador = [0 for i in range (5)]

suma=0
while suma != generavalor :
    if suma+10<=generavalor:
        suma +=10
        contador[3] += 1
    elif suma +5 <=generavalor:
        suma +=5
        contador[2]+=1
    elif suma +2 <= generavalor:
        suma += 2
        contador[1]+=1
    elif suma +1 <= generavalor:
        suma+=1
        contador[0] += 1
    
print(f"la forma más sencilla de generar el {generavalor} es: ")
aux=0
for i in monedas :
    print(f"{contador[aux]} monedas de ${monedas[aux]}")
    aux+=1

class Reina:
    posiciony=0
    posicionx=0
    def cambiavalores(self):
        self.posicionx = random.randint(1,8)
        self.posiciony = random.randint(1,8)
    def imprime (self):
        print(f"{self.posicionx} , {self.posiciony}")
    def __init__(self) -> None:
        posiciony =  random.randint(1,8)
        posicionx = random.randint(1,8)   
    def ataque (self, reina):
        if reina.posiciony == self.posiciony or reina.posicionx == self.posicionx :
                return True
        elif (reina.posiciony - self.posiciony) == (reina.posicionx - self.posicionx):
            return True
        else :
            return False 
                        
reinas = [Reina(), Reina(), Reina(), Reina(), Reina(), Reina(), Reina(), Reina()]

convinacioninvalida = True
while convinacioninvalida :
    i=0
    while i< len(reinas):
        reinas[i].cambiavalores()
        i+=1
    
    i=0
    convinacioninvalida= False
    while i<len(reinas)-1 and not(convinacioninvalida):
        
        aux = i+1 
        while aux< len(reinas) and not(convinacioninvalida):
            convinacioninvalida = reinas[i].ataque(reinas[aux])
            aux += 1
        i+=1
    
    i=0
while i< len(reinas):
    reinas[i].imprime ()
    i+=1  

            
                
    
    