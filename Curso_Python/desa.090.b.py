from random import randint
while True:
    jogador = int(input("Digita um valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo  not in "PI":
        tipo = str(input("Par ou Ìmpar [P/I]: ")).strip().upper()[0]
        print(f"Voce digitou {jogador} e o computador {computador} e o total é {total}")
        if tipo == "P":
            if total % 2 == 0:
                print("Você venceu.!")
            else:
                print("Você perdeu!")
                break

        elif tipo == "I": 
            if total % 2 == 1:
                print("Você venceu!")   
            else:
                print("Você perdeu!")
                break

    print("Vamos jogar novamente!")           
 

         