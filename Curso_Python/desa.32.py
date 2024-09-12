#032
import time

def contar():
   print("Contagem de 1 até 10 de 1 em 1") 
   for x in range(1,11):
      time.sleep(1)
      print(x)
   print("FIM")   

   print("Contagem de 10 de 0 de 2 em 2")
   for d in range(0,10,2):
      time.sleep(1)
      print(d)
   print("FIM")
   
  
   
contar()




