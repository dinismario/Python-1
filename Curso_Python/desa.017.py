#017
n1 = int(input("Digita um valor: "))
n2 = int(input("Digita um valor: "))
n = 0
while n != 5:
    print('''
          [1] Soma
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] sair do programa''')
    
    n = int(input("Digita a sua opção: "))
    if  n == 1:
        soma = n1 + n2
        print(" A Soma entre {} + {} = {}".format(n1,n2,soma))
    elif n == 2:
        mult = n1 * n2
        print(" A Multiplicação entre {} * {} = {}".format(n1,n2,mult))

    elif n == 3:
        if n1 > n2:
           maior = n1
        elif n1 < n2:
           maior = n2
           print(" Entre {} e {} o maior é {} ".format(n1,n2,maior)) 

    elif n == 4:  
         print("Informe os valores novamente")
         n1 = int(input("Digita um valor: "))
         n2 = int(input("Digita um valor: "))
         
    elif n == 5:
        print("FIM")
    else:
       
        print("Opção Inválida! " *3 )



    
print("Fim do Programa!")





