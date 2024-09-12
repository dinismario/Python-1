#013

ano_actual = 2024
for x in range(7):
    ano = int(input("Digita o ano de nascimento:".format(x)))
    idade = ano_actual-ano
    if idade >=18:
       print("Já é maior de idade! a sua idade é: {}".format(ano_actual-ano))   

    elif idade <= 17:
       print("Ainda é menor de idade.! a sua idade é: {}".format(ano_actual-ano))
