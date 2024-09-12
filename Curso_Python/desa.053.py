#053
carro = int(input("Digita a velocidade do seu carro: "))
if carro > 80:
    print("voce ultrapassou a velocidade miníma de 80km/h")
    multa = (carro-80) * 7
    print("Voce vai pagar a multa no valor de R${}".format(multa))

else:
    print("Boa viagem a sua velocidade é menor que 80km/h")    
