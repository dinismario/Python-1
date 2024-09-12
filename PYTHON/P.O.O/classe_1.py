#Classes e Objetos(P.0.0)
#Objetos :Entidade=Variaveis  e comportamentos=Funções 

class carro:
    def __init__(self):
        self.velocidade = 10
        self.cor = "Azul"

    def acelerar(self):
        print("Acelerando" + str(self.velocidade))    

    def desacelerar(self):
        print("Desacelerando" + str(self.velocidade))

c1 = carro()
print(c1.velocidade)
print(c1.cor)
c1.acelerar()
c1.desacelerar()