#043
import random 
n1 =str(input("Primeiro aluno: "))
n2 =str(input("Segundo aluno: "))
n3 =str(input("Terceiro aluno: "))
n4 =str(input("Qaurto aluno: "))

listas = [n1, n2, n3, n4]
escolhido = random.choice(listas)
print(f'O aluno escolhido é {escolhido}')
