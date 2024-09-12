#60
print("="*30)
num = int(input("Digita um valor inteiro: "))
print("Escolha uma das bases para conversão:")
print('''
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL
''')
p =  int(input("Qual é a sua opção: ")) 
if p == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))

elif p == 2:
    print("{} convertido paraOCTAL é igual a {}".format(num, oct(num)[2:]))

elif p == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))

else:
    print("Opção Inválida!")
   
