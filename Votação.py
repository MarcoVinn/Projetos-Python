cont = 0
p = 0
x = 0
n = 0
while cont < 5:
    f = int(input("Para escolher Playstation digite [1]\n"
                  "Para escolher XBOX digite [2]\n"
                  "Para escolher Nintendo digite [3]: "))
    cont += 1
    if f == 1:
        p = p + 1
    elif f == 2:
        x = x + 1
    elif f == 3:
        n = n + 1
    else:
        print("Voto Invalido")


if p > x and p > n:
    print("O ganhador foi o Playstation com {} votos!!!".format(p))
elif x > p and x > n:
    print("O ganhador foi o XBOX com {} votos!!!".format(x))
elif n > p and n > x:
    print("O ganhador foi o Nintendo com {} votos!!!".format(n))
elif n == p or n == x or p == n or p == x or x == p or x == n:
    print("Empate")

