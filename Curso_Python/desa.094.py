#094
cont = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","desazeis","dezasete","dezoito","dezanove","vinte")

while True:
    num = int(input("Digita um numero entre 0 e 20: "))
    if 0 <= num <= 20: 
        break
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]?: ")).strip().upper()[0]

    if resp == "N":
        break    


print(f"Você digitou {cont[num]}")