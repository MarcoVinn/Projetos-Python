bpm = int(input("Digite o seu BPM: "))
age = int(input("Digite sua idade: "))
if age <= 2 and bpm in range(120, 140):
    print("BPM Ideal")
elif age in range(3, 4) and bpm in range(80, 120):
    print("BPM Ideal")
elif age in range(5, 6) and bpm in range(75, 115):
    print("BPM Ideal")
elif age in range(7, 12) and bpm in range(70, 110):
    print("BPM Ideal")
elif age in range(13, 17) and bpm in range(60, 110):
    print("BPM Ideal")
elif age in range(8, 17) and bpm in range(80, 100):
    print("BPM Ideal")
elif age in range(18, 65) and bpm in range(70, 80):
    print("BPM Ideal")
elif age > 65 and bpm in range(50, 60):
    print("BPM Ideal")
elif age <= 2 and bpm < 120:
    print("BPM Abaixo do Ideal")
elif age in range(3, 4) and bpm < 80:
    print("BPM Abaixo do Ideal")
elif age in range(5, 6) and bpm < 75:
    print("BPM Abaixo do Ideal")
elif age in range(7, 12) and bpm < 70:
    print("BPM Abaixo do Ideal")
elif age in range(13, 17) and bpm < 60:
    print("BPM Abaixo do Ideal")
elif age in range(8, 17) and bpm < 80:
    print("BPM Abaixo do Ideal")
elif age in range(18, 65) and bpm < 70:
    print("BPM Abaixo do Ideal")
elif age > 65 and bpm < 50:
    print("BPM Abaixo do Ideal")
else:
    print("BPM Acima do ideal")
