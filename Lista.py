inventario = []
resposta = "S"
#o sinal de [] abre uma lista
while resposta == "S":
    inventario.append(input("Digite o nome do produto: "))
    inventario.append(float(input("Digite o valor do produto: ")))
    inventario.append(input("Numero serial: "))
    inventario.append(input("Departamento: "))
    resposta = input("Deseja continuar? Digite \"S\"").upper()
for elemento in inventario:
    print(elemento)
