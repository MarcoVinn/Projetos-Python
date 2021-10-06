tran = int(input("Informe a quantidade de transações realizadas: "))
cont = 1
soma = 0
while tran >= cont:
    valor = float(input("Informe o valor da {}° transação: ".format(cont)))
    cont = cont + 1
    soma = soma + valor
print("O valor total das suas transações foram de R${}".format(soma))
print("O valor médio de suas transações foram de {:.2f}".format(soma / tran))
