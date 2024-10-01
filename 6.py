def calcular_preco(sessao, idade, estudante):
    # Definindo os preços das sessões
    if sessao == "1":
        preco = 20
    elif sessao == "2":
        preco = 25
    elif sessao == "3":
        preco = 30
    else:
        print("Sessão inválida.")
        return None

    # Aplicando desconto de 50% se for criança, idoso ou estudante
    if idade <= 12 or idade >= 65 or estudante == "sim":
        preco = preco * 0.5

    return preco

# Exemplo de uso
print("Escolha o tipo de sessão (Matinê = 1, Vespertina = 2 ou Noturna = 3):")
sessao = input().capitalize()

idade = int(input("Digite a idade: "))

if 12 < idade < 65:
    estudante = input("Você é estudante? (sim/não): ").lower()
else:
    estudante = "não"  # Não precisa perguntar se a pessoa já tem desconto por idade

preco_final = calcular_preco(sessao, idade, estudante)

if preco_final is not None:
    print(f"O valor total da compra é: R$ {preco_final:.2f}")
