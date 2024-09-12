#067
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
jogador = 0
while jogador != 3:
    print("Suas opções:")
    print('''
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA
        [3] FIM DO JOGO
    ''')

    print("="*30)
    jogador = int(input("Qual é a sua jogada?: "))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    print("="*30)

    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print("="*30)

    if computador == 0:
        if jogador == 0:
            print("Empate")
            print("="*30)

        elif jogador == 1 :
            print("Jogador ganhou")
            print("="*30)


        elif jogador == 2:
            print("Computador ganhou")
            print("="*30)


        else:
            print("Jogada Inválida")

    elif computador == 1:
        if jogador == 0:
            print("Computador ganhou")
            print("="*30)

        elif jogador == 1:
            print("Empate")
            print("="*30)


        elif jogador == 2:
            print("Jogador ganhou")
            print("="*30)


        else:
            print("Jogada Inválida")

    elif computador == 2:
        if jogador == 0:
            print("Jogador ganhou")
            print("="*30)


        elif jogador == 1:
            print("computador ganhou")
            print("="*30)



        elif jogador == 2:
            print("Empate") 
            print("="*30)


        else:
            print("Jogada Inválida!")

    if jogador == 4:
        print("Fim do jogo")

print("FIm do programa!")        

        


