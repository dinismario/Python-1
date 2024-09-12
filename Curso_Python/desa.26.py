#026
valor = []
m = 0
me = 0
for c in range(0,5):
    valor.append(int(input("Digita um valor: ")))
    if m == me:
        m = me = valor
    else:
         if valor[c] > m:
              m = valor[c]
         if valor[c] > me:
              me = valor[c]   
for c , x in enumerate(valor):
      print(f"A posição é {c} e o número é {x}") 
print(f"O maior é {m}"  ) 
print(f"O menor é {me}")  


 