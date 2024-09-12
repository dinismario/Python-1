num = int(input("Digita um valor: "))
u = num // 1 % 10
d = num // 10 % 10
s = num // 100 % 10 
m = num // 1000 % 10 
print("O número digitado é {}".format(num))
print("Unidade é {}".format(u))
print("Dezena é  {}".format(d))
print("Sentena é {}".format(s))
print("Miliar é  {}".format(m))


