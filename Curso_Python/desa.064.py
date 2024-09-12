#064
nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2} , a média do aluno é {media}")    

if media >= 7:   
    print("O aluno esta aprovado.!")

elif media == 5:
    print("O aluno esta em Recuperação!")

elif media < 5:
    print("O aluno esta Reprovado!")



 
