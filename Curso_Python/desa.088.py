#088
num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input("Digita um valor (999 para parar ): "))
    soma = soma + num 
    cont = cont + 1

soma -= 999    
print("A soma dos {} valores foi {} ".format(soma, cont))

