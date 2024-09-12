#Estrutura aninhadas 
nome = str(input("Qual é o seu nome? "))
if nome == "Dinis":
    print("Que nome bonito!")

elif nome =="Pedro" or nome=="Ana" or nome=="Paula":
    print("Seu nome é bem popular em Angola!")

elif nome in "Maria Mado Jessica Juliana":
    print("Belo nome {}".format(nome))    

else:
    print("Seu nome é bem normal! ")    
print("Tenha um bom dia {}!".format(nome))    