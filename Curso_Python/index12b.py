#desenpacotador
#def contador(* núm):
    #for x in núm:
     #   print(f'Os numeros sao:{x}')
   #  tam = len(núm)
    # print(f'Os valores {núm} e são ao todo {tam}')


#contador(2, 0, 1)
#contador(5, 6)
#contador(3, 4, 1,4,5)
#def dobra(ilst):
 #   pos = 0
  #  while pos < len(ilst):
   #     ilst[pos] +=2
    #    pos +=1

#valores = [5,6,7,8,2]
#dobra(valores)
#print(valores)


def soma ( * valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')


soma(4,5)
soma(3,4,7)
