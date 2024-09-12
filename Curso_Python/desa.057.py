#067
salario = float(input("Qual é o valor do seu salário?: "))
if salario <= 1250:
    s = salario + (salario + 15 / 100)
    

else:
    s = salario + (salario + 10 / 100)

print(f'O seu salário agora é: R${s:.2f}')  

