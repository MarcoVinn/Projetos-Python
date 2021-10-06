notas = []
op = -1
cont = 1
print("1 - Informar notas \n2 - Exibir notas \n3 - Exibir media\n4 - Sair")
while op != 4:
    op = int(input("Escolha sua opção: "))
    if op == 1:
        notas.append(float(input("Digite a {} nota: ".format(cont))))
        cont += 1
    elif op == 2:
        for x in notas:
            print(x)
    elif op == 3:
        print("A média das notas é de {}".format(sum(notas)/len(notas)))
    else:
        print("Te vejo depois!")