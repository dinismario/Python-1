#073
soma = 0
cont = 0
for x in range(1,7):
    num = int(input("Digita o {} valor: ".format(x)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num   
print("A soma entre {}  valores é: {}".format(cont,soma))

    
