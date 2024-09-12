#082
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
p = 0
while p != 5:
 print('''
       [1] Somar 
       [2] Multiplicar
       [3] Maior
       [4] Novos números
       [5] Sair do programa
''')
 p = int(input("Qual é a sua Opção?: "))
 if p == 1:
  soma = n1 + n2 
  print(f"A soma entre {n1} + {n2} = {soma}")

 elif p == 2:
  mult = n1 * n2 
  print(f"A multiplicação entre {n1} x {n2} = {mult}")

 elif p == 3:
  if n1 > n2 :
   print(f"{n1} é maior que {n2}")
  else:
   print(f"{n2} é maior que {n1}")
   
   
 elif p == 4:
  print("Informe os números novamente.!")
  n1 = int(input("Primeiro valor: "))
  n2 = int(input("Segundo valor: "))

 elif p == 5:
  print("FIMMM!")
 else:
  print("Opção Inválida.!")

print("FIM do Programa!")

