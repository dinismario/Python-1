#Calculadora em Python:
n1 = int(input("Digita um valor: "))
n2 = int(input("Digita um valor: "))
opcao = 0

while opcao != 6:
    print('''
         [1]-Soma 
         [2]-Multiplicar
         [3]-Subtrair
         [4]-Dividir
         [5]-Repetir a opercão''')
    opcao = int(input("Escolha a sua opção: "))

    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} + {} = {}".format(n1,n2,soma))

    elif opcao == 2:
        mult = n1 * n2 
        print("A Multiplicação entre {} * {} = {}".format(n1,n2,mult))

    elif opcao == 3:
       sub = n1 - n2 
       print("A Subtração entre {} - {} = {}".format(n1,n2,sub))

    elif opcao == 4:
        div = n1 / n2 
        print("A Divisão entre {} / {} = {}".format(n1,n2,div))
 


    elif opcao == 5:
     while opcao != 5:
      print('''
         [1]-Soma 
         [2]-Multiplicar
         [3]-Subtrair
         [4]-Dividir
         [5]-Repetir a opercão''')
    opcao = int(input("Escolha a sua opção: "))

    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} + {} = {}".format(n1,n2,soma))

    elif opcao == 2:
        mult = n1 * n2 
        print("A Multiplicação entre {} * {} = {}".format(n1,n2,mult))

    elif opcao == 3:
       sub = n1 - n2 
       print("A Subtração entre {} - {} = {}".format(n1,n2,sub))

    elif opcao == 4:
        div = n1 / n2 
        print("A Divisão entre {} / {} = {}".format(n1,n2,div))
 



    elif  opcao == 6:
       print("Opção Inválida!  escolha uma opção entre 1 , 5  " *1 )


print("FIM DO PROGRAMA!")
