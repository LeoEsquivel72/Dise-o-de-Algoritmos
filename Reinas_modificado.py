import random


generavalor = int(input("que valor quieres formar: "))

monedas = [1,2,5,10]

contador = [0 for i in range (5)]

aux=generavalor
contador[3]=aux//10
aux= aux%10
contador[2]=aux//5
aux=aux%5
contador[1]=aux//2
aux=aux%2
contador[0]=aux


    
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
i=0
while i< len(reinas):
    reinas[i].cambiavalores()
    i+=1
          
i=0
contador=0
while i in range(len(reinas)-1):
    convinacioninvalida=True
    contador=0
    while convinacioninvalida:
        
        if contador>128:
            i=0                
            while i< len(reinas):
                reinas[i].cambiavalores()
                i+=1 
                contador=0 
            i=0
            
        a=i+1 
        reinas[a].cambiavalores()
        
        e=0
        contador+=1 
        convinacioninvalida=False
        while e<a :
            
            if reinas[e].ataque(reinas[a]):
                convinacioninvalida=True
                
            e+=1
    i+=1
            
i=0                
while i< len(reinas):
    reinas[i].imprime ()
    i+=1                  
                
