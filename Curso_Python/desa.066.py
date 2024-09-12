#066
peso = float(input("Qaul é o seu peso? (kg) "))
altura = float(input("Qaul é a sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Voçê esta a baixo do peso normal")

elif 18.5 <= imc < 25:
    print("Voçê esta na faixa de peso normal")

elif 25 <= imc < 30:
    print("Voçê esta em Sobrepeso!")

elif 30 <= imc < 40:
    print("Voçê esta em Obesidade!")

elif imc > 40:
    print("Você esta em obesidade mórbida!")
