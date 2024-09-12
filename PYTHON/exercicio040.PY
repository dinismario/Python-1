compras = ["Calças", "Tênis", "Perfume", "Creme", "Cama", "Chinelo","Cadeira" ,"Mesa" ,"Telefone"]
recebe = str(input("O que , que pretendes comprar.? "))



for produto in compras:
   
    if produto == recebe:
          print("Esta na lista!")
          break

    else:
        print("Infelizmente não temos este produto ca na nossa loja!")    
        break

