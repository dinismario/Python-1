#028
lista = list()
valores = list()
valor1 = valor2 = 0
for i in range(0,7):
    valores.append(int(input("Digita um valor(1-7): ")))
    lista.append(valores[:])
    valores.clear()
for p in lista:
    if p[0] % 2 == 0:
      print(f'Este número {p[0]}  é par ') 
      valor1 += 1
      lista.sort()
    else:
      print(f'Este número {p[0]}  é ímpar ') 
      valor2 += 1
      lista.sort()
     
      
         
