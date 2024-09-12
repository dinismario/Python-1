#059
print("="*30)

casa = float(input("Qual é o valor da casa?: "))
salario = float(input("Qual é o seu salario?: "))
ano  = int(input("Quantos anos voce vai pagar?: "))
pres = casa / (ano * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, ano) , end="")
print("a prestação será de R${:.2f}".format(pres))

if pres <= minimo:
    print("Emprestimo pode ser Concedido")

else:
    print("Emprestimo não Concedido!")
 

