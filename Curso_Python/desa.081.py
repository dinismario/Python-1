#074
num = int(input("Digita um número: "))
tot = 0
for x in range(1 , num + 1):
    if num % x == 0:
        print('\033[33m',end="")
        tot += 1

    else:
        print('\033[31m',end="")
    print("{}".format(x),end="")    

    print("Número digitado: {} foi divisivel {} vezes ".format(num, tot))    

if tot == 2:
    print("È um número primo.!")
else:
    print("Não é um número primo.!")
