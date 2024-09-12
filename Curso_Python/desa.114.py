#114
ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = int(input("Nota 1 : "))
    nota2 = int(input("Nota 2 : "))
    media = (nota1 + nota2) / 2
    ficha.append([nome ,nota1 ,nota2 ,media])
    res = str(input("Quer continuar [S/N]?: "))
    if res in "Nn":
        break

print("-=-"*20)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-=-"*20)

for i , a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
