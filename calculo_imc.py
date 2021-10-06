print("Vamos calcular seu IMC!!!")
p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura em metros: "))
i = p / (a**2)
print("Seu IMC é de {:.1f}".format(i))
if i <= 16:
    print("Baixo Peso Grau III")
elif 16 <= i <= 16.99:
    print("Baixo Peso Grau II")
elif 17 <= i <= 18.49:
    print("Baixo Peso Grau I")
elif 18.50 <= i <= 24.99:
    print("Parabens! Você está em seu peso ideal.")
elif 25 <= i <= 29.99:
    print("Sobrepeso")
elif 30 <= i <= 34.99:
    print("Obesidade Grau I")
elif 35 <= i <= 39.99:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
