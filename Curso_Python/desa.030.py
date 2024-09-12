#030
aluno = dict()

for x in range(1):
    aluno['Nome']=(str(input("Digita o seu nome: ")))
    aluno['Media']=(float(input("Digita a nota1: ")))
   
    if aluno ['Media'] >= 10:
        aluno['Situação'] = 'Aprovado!'

    elif 5 <= aluno['Media'] <=7:  
        aluno['Situação'] = 'Recuperação!'

    else:
         aluno['Situação'] = 'Reprovado!'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')


    



    
