viajantes = int(input("Qual a quantidade de viajantes?: "))
categoria = int(input("Qual a categoria do assento?\n"
                      "Para Econômica digite 1\n"
                      "Para Executiva digite 2\n"
                      "Para Primeira Classe digite 3: "))
valor = float(input("Qual o valor do pacote?: "))
per = 0
if categoria == 1:
    if viajantes == 2:
        per = 3
    elif viajantes == 3:
        per = 4
    elif viajantes >= 4:
        per = 5
elif categoria == 2:
    if viajantes == 2:
        per = 5
    elif viajantes == 3:
        per = 7
    elif viajantes >= 4:
        per = 8
elif categoria == 3:
    if viajantes == 2:
        per = 10
    elif viajantes == 3:
        per = 15
    elif viajantes >= 4:
        per = 20

if viajantes < 2:
    print("Apenas passagens com 2 viajantes ou mais são elegíveis à desconto")
else:
    des = per * valor / 100
    print("O valor do desconto é de R${}".format(des))
