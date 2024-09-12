#006
peso = float(input("Qual é a sua peso?: "))
altura = float(input("Qual é a sua altura?: "))
divisor = str(peso/altura)
if divisor == 18.5:
    print("Abaixo do peso.! {}".format(peso/altura))

elif divisor == 18.5 or divisor == 25:
    print("Peso Ideal {}".format(peso/altura))

elif divisor == 25 or divisor == 30:
    print("Sobrepeso {}".format(peso/altura))

elif divisor == 30 or divisor == 40:
    print("Obesidade {}".format(peso/altura))   

elif divisor == 40:
    print("Obesidade mórbida! {}".format(peso/altura))       

    