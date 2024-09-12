#079

sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, por favor ,Informe o seu sexo [M/F]"))
    
print(f"Sexo {sexo} registrado com socesso.!")
   

