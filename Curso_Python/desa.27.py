#027
pessoas = list()
gente = list()
pesom = peson = 0

for i in range(0,5):
    gente.append(str(input("Digita o seu nome: ")))
    gente.append(float(input("Digita o seu peso: ")))
    pessoas.append(gente[:])
    gente.clear()
print("---------------------")   

for p in pessoas:
    print(f'{p[0]} tem {p[1]} peso')

print("---------------------")   

for x in pessoas:
    if x[1] >= 20:
        print(f'{x[0]} o seu peso é maior.')
        pesom +=1

    else:
        print(f'{x[0]} o seu peso é menor.')
        peson +=1