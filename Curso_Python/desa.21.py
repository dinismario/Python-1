#21
num = 0
while True: 
   num = int(input("Digita qualquer valor para gerar uma tabuada (1-12): "))
   
   if num < 0:
      print("Não é permitido números negativos!")
      num = int(input("Digita qualquer valor para gerar uma tabuada (1-12): "))
      
  # for x in range(1,13):
  #    print(str(num) + " x " + str(x) + " = " + str(num*x))
   #   break
   
   for x in range(1,13):
      print(str(num) + " x " + str(x) + " = " + str(num*x))
      

      