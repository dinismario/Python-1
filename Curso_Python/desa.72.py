#072
num = int(input("Digita um valor para ver sua tabuada: "))
for x in range(1,11):
   # print(str(num) + " x " + str(x ) + " = " + str(num * x))
   print("{} x {} = {}".format(num,x, num*x))