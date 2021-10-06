qt = int(input("Quantos alimentos foram consumidos hoje?: "))
cont = 1
soma = 0
while qt >= cont:
    al = str(input("Informe o {}° alimento ingerido: ".format(cont)))
    cal = int(input("Informe a quantidade de calorias: "))
    cont = cont + 1
    soma = soma + cal
print("Você consumiu {}kcal hoje".format(soma))
