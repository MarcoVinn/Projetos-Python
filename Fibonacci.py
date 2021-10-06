num = int(input("Digite um número: "))
n1 = 0
n2 = 0

while n1 < num:
    n1 = n1 + n2
    n2 = n1 - n2
    if n1 == 0:
        n1 = n1 + 1

if n1 == num:
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")