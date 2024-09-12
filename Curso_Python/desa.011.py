#011
soma = 0
cont = 0
for x in range(1,7):
    n = int(input("Digita um {} valor: ".format(x)))
    if n % 2 == 0:
      soma = soma + n
      cont = cont + 1
print("A soma entre os numeros é:  {} e os numeros  pares é {}".format(soma, cont))    




   
