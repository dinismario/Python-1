#058
print("="*30)
s1 = float(input("Digita o primeiro valor:"))
s2 = float(input("Digita o segundo valor:"))
s3 = float(input("Digita o terceiro valor:"))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
   print("Os Seguimetos acima podem formar um triângulo.!")

else:
   print("Não podem formar um triângulo")
