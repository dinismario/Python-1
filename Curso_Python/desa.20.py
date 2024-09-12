#20
n = s = 0
while True:
 num = int(input("Digita um valor: "))
 if num == 999:
  break
 s += 1
 n += num
print(f"os valores digitados são {s} e a soma entre eles é: {n}") 