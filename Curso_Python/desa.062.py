#062
from datetime import date
atual = date.today().year
nasc = int(input("Digita o seu ano de nascimento: "))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print("Voce deve ser alistar imediatamente.!")

elif idade < 18:
    saldo = 18 - idade
    print(f"Vove ainda não tem {idade} anos para o alistamento")
    

elif idade > 18:
    saldo = idade - 18
    print(f"Voce ja deverias ter se alistado ha {idade} anos")
