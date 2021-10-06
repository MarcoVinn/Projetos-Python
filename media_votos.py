a = int(input("Votos para Segunda-Feira:"))
b = int(input("Votos para Terça-Feira: "))
c = int(input("Votos para Quarta-Feira:"))
d = int(input("Votos para Quinta-Feira: "))
e = int(input("Votos para Sexta-Feira: "))
if a > b and a > c and a > d and a > e:
    print("A data escolhida foi Segunda-Feira")
elif b > a and b > c and b > d and b  > e:
    print("A data escolhida foi Terça-Feira")
elif c > a and c > b and c > d and c > e:
    print("A data escolhida foi Quarta-Feira")
elif d > a and d > b and d > c and d > e:
    print("A data escolhida foi Quinta-Feira")
else:
    print("A data escolhida foi Sexta-Feira")