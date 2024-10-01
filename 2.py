cargo = input("Digite a primeira letra do seu cargo (S, T, P, C, D): ").upper()
salario = float(input("Qual seu salário: "))
aumento_s = salario * 1.45
aumento_t = salario * 1.35
aumento_p = salario * 1.25
aumento_c = salario * 1.15

if cargo == "S":
    print(f"Seu salario e: {aumento_s:.2f}")

elif cargo == "T":
    print(f"Seu salario e: {aumento_t:.2f}")

elif cargo == "P":
    print(f"Seu salario e: {aumento_p:.2f}")

elif cargo == "C":
    print(f"Seu salario e: {aumento_c:.2f}")
else:
    print(f"Seu salario não muda")