f = float(input("Digite seu faturamento anual: "))
p = input("Digite seu plano.\nBasic\n"
          "Silver\n"
          "Gold\n"
          "Platinum: ").lower()
if p == "basic":
    b = 30 * f / 100
    print("O bônus a ser pago é de {}".format(b))
elif p == "silver":
    b = 20 * f / 100
    print("O bônus a ser pago é de {}".format(b))
elif p == "gold":
    b = 10 * f / 100
    print("O bônus a ser pago é de {}".format(b))
elif p == "platinum":
    b = 5 * f / 100
    print("O bônus a ser pago é de {}".format(b))
