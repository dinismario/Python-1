#034
print("="*30)

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual-ano
     
    if idade < 17:
       print(f'Com {idade} anos :Não vota.')
       return ""
      
    elif 17 <= idade < 18 or idade > 65:
       print(f'Com {idade} anos : O voto é Opcional')
       return ""
    else:
        print(f'Com {idade} anos : O voto é Obrigátorio')
        return ""


num = int(input("Digita o seu ano de nascimento: "))
print(voto(num)) 
