#Classes e Objetos
 
#Classes ou Objetos(P.0.0)
#Objetos :Entidade=Variaveis  e comportamentos=Funções 

class carro:
    def __init__(self ,velocidade ,cor):
        self.velocidade = velocidade
        self.cor = cor

    def acelerar(self):
        self.velocidade +=1   

    def desacelerar(self):
        self.velocidade -=1   
        

c1 = carro(5,"azul")
c2 = carro(10,"preto")
c1.acelerar() 
c2.desacelerar()
print(str(c1.velocidade)+" " + (c1.cor))
print(str(c2.velocidade)+" " + (c2.cor))

