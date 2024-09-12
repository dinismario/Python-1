# 
def ele_primo(num):
     
     for n in range(2, num):
       if num % n == 0:
           return True
     return False       
print(ele_primo(3))



