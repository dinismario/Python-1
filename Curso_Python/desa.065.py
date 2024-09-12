#065
num1 = int(input("Primeiro segmento:"))
num2 = int(input("Segundo segmento:"))
num3 = int(input("Terceiro segmento:"))
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("Os seguimentos acima podem formar um Triângulo",end = " ")
    if num1 == num2 == num3:
        print("EQUILÁTERO")

    elif num1 != num2 != num3 != num1:
            print("ESCALENO")

    else:
         print("ISÔSCELES")        


else:
    print("Não podem formar um triângulo.! ")



