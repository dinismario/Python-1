#113
aluno = dict()
while True:
    aluno ["Nome"] = str(input("Nome: "))
    aluno ["Nota1"] = int(input("Nota 1: "))
    aluno ["Nota2"] = int(input("Nota 2: "))
    aluno ["Media"] = (aluno["Nota1"] + aluno["Nota2"]) / 2
    if aluno["Media"] >= 7:
        aluno["Situação"] = "Aprovado"
    elif 5 <= aluno["Media"] <= 7:
        aluno["Situação"] = "Recuperação"

    else:
        aluno["Situação"] = "Reprovado"

    print("-=-"*20)
    for x , k in aluno.items():
        print(f"{x} é igual   {k}")

    re = " "
    if re not in "SN":
      re = str(input("Quer continuar [S/N]?: ")).strip().upper()[0]

    if re == "N":
        break
          
print("-=-"*20) 
#for x , k in enumerate(aluno):
#   print(f"{x:<4}{k[0]:<10}{k[2]:<8.1f}")        

