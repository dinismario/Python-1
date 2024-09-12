#Estrutura de Repetição ou LOOP ...
#while , for 

#While(Enquanto) : ele só para quando a condição for falsa, ele só pode nos retornar números verdadeiros ele só recebe valores (True e false)..
#x = 1
#while x <= 10 :
#   print(x)
#   x = x + 1
# x += 1

#saindo = False
#while not saindo:
 #   nome = input("Digita um nome: ")
  #  print("Nome é : " + nome)

   # if nome == "":
    #    saindo = True

#////////////////////////////////////////

e_par = True
while e_par:
    numero = int(input("Digita um numero par: "))
    e_par = numero % 2 == 0 
    print(e_par)
