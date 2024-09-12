#Pedra, papel e tesoura: Crie uma versão do clássico jogo com Python.
from random import randint
intes = ("Pedra","Papel", "Tesoura")
computador = randint (0,2)
print("-="*30)

print('''Suas opções: 
     [ 0 ] PEDRA 
     [ 1 ] PAPEL 
     [ 2 ] TESOURA
     ''')

print("-="*30)
while True:
    jogador =int(input("Qual é a sua jogada?: "))
    print("-="*30)

    print("Computador jogou {}".format(intes[computador]))
    print("-="*30)
    print("Jogador jogou {}".format(intes[jogador]))
    print("-="*30)

    if computador == 0: #Pedra
        if jogador==0:
            print("Empate")
        elif jogador==1:
            print("Jogador Vence")
        elif jogador==2:
            print("Computador Vence")  
        else:
            print("Jogada Inválida")     
                

    elif computador ==1: #Papel
        if jogador==0:
            print("Computador Vence")

        elif jogador==1:
            print("Empate")
        
        elif jogador==2:
            print("Jogador Vence")

        else:
            print("Jogada Inválida")    


    elif computador ==2: #Tesoura
        if jogador==0:
            print("Jogador Vence")

        elif jogador==1:
            print("Computador Vence")

        elif jogador==2:
            print("Empate")

        else:
            print("Jogada Inválida")  
            
    print("-="*30)

   

    



