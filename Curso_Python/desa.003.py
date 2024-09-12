#Desafio 003
ano = int(input("Digita o seu ano de nascimento: "))
ano1 = 2024
ano_atual = str(ano1-ano)

if  ano==2006 or ano==2005 or ano==2004:
    print("Ele vai para ao serviço militar,  A sua idade é: {}".format(ano1-ano))

elif ano == 2007:
    print("Se prepara para o exercicito , A sua idade é: {}".format(ano1-ano))

else:
   print("A sua idade ja passou, A sua idade é: {}".format(ano1-ano)+", A idade maxima é : 20")
