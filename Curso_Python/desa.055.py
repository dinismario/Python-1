#055
long = int(input("Qual é a distância da sua viagem?: "))
v = long * 0.50

print("Voce está prestes a começar uma viagem de {}km/h".format(long))
if long <= 200:
   print("É o preço da sua passagem longa será de R${}".format(v))

elif long >= 0.45:
    print("E o preço da sua passagem longa será de R${}".format(v))
  
  

