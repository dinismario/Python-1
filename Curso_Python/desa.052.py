from random import randint
computador = randint(0,5)
jogador = int(input("Digita um valor entre (0-5): "))
if jogador == computador:
    print("voce ganhou.! jogador pensou no {} e computador {}".format(jogador , computador))

else:
    print("Ganhei ! eu pensei no numero {} e não no {}".format(computador, jogador))    

