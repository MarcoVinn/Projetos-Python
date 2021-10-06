equipamentos = []
serial = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamentos.append(str(input("Digite o equipamento: ")))
    serial.append(int(input("Digite o numero de serial: ")))
    departamento.append(str(input("Digite o departamento:")))
    resposta = input("Digite \"S\" para continuar").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento...: ", equipamentos[indice])
    print("Serial...: ", serial[indice])
    print("Departamento...: ", departamento[indice])
