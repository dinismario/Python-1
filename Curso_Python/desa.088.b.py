#b
soma = 0
cont = 0
while True:
    num = int(input("Digita um valor (999 para parar): "))
    if num == 999:
        print("FIM")
        break
    soma = soma + num 
    cont = cont + 1 

print("A soma dos valores {} foi {}".format(cont , soma))    
