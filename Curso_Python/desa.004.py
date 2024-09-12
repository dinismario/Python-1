#Desafio 004
nota = int(input("Digita a sua nota: "))
nota2 = int(input("Digita a sua nota2: "))
media = (nota+nota2)/ 2

if media <= 10:
    print("Aprovado!")

elif media ==5 or media==6:
    print("Recuperação!")

elif media < 4:
    print("Reprovado!")

print(media)
