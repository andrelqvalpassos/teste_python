estado_civil = input("Digite a primeira letra do seu estado civil (S, C, V, D): ").upper()

if estado_civil == "S":
    print(f"Voce e solteiro")

elif estado_civil == "C":
    print(f"Voce e casado")

elif estado_civil == "D":
    print(f"Voce e divorciado")

elif estado_civil == "V":
    print(f"Voce e: {estado_civil}")
else:
    print(f"Invalido")