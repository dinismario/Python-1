class pessoa:
    def __init__(self ,idade ,altura):
        self.idade = idade
        self.altura = altura

    def magro(self):
       if self.idade >= 18:
           print("Treine Sempre.!")
       else:
           print("Se esforçe ainda mas!")    

    def mas(self):
       if self.altura >= 5:
           print("A sua altura está na média!")
       else:
           print("A sua altura não esta na média!")    
           



p1= pessoa(20,18)
p2= pessoa(50,altura=5)
p1.magro()
p2.mas()
print(str(p1.idade)+ " " +str(p1.altura))
print(str(p2.idade)+ " " +str(p2.altura))




