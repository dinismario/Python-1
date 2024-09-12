#112
aluno = dict()
aluno ["Nome:"] = str(input("Nome: "))
aluno ["Media"] = float(input("Média: "))

if aluno["Media"] >= 7:
   aluno["Situação"] = "Aprovado"
    

elif 5 <= aluno["Media"] <= 7:
    aluno["Situação"] = "Recuperação"
    

else:
  aluno["Situação"] = "Reprovado"


print("-=-"*20)

for x , k in aluno.items():
   print(f"{x} é igual {k}")

