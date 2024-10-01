# Função para calcular o valor total da fatura
def calcular_fatura(plano, minutos_utilizados, gb_utilizados):
    # Definindo os planos
    if plano == '1':
        minutos_franquia = 100
        gb_franquia = 5
        valor_plano = 50
        nome_plano = 'Básico'
    elif plano == '2':
        minutos_franquia = 300
        gb_franquia = 10
        valor_plano = 80
        nome_plano = 'Intermediário'
    elif plano == '3':
        minutos_franquia = 500
        gb_franquia = 20
        valor_plano = 120
        nome_plano = 'Avançado'
    else:
        return None  # Plano inválido

    # Calcula o valor adicional por minutos excedentes
    if minutos_utilizados > minutos_franquia:
        minutos_excedentes = minutos_utilizados - minutos_franquia
        custo_minutos_excedentes = minutos_excedentes * 1  # R$ 1 por minuto adicional
    else:
        custo_minutos_excedentes = 0

    # Calcula o valor adicional por GB excedentes
    if gb_utilizados > gb_franquia:
        gb_excedentes = gb_utilizados - gb_franquia
        custo_gb_excedentes = gb_excedentes * 10  # R$ 10 por GB adicional
    else:
        custo_gb_excedentes = 0

    # Valor total da fatura
    valor_total = valor_plano + custo_minutos_excedentes + custo_gb_excedentes

    return valor_total, nome_plano, custo_minutos_excedentes, custo_gb_excedentes

# Entrada do usuário para escolha do plano
print("Escolha o seu plano de telefonia:")
print("1. Plano Básico (100 minutos, 5GB de internet) - R$ 50")
print("2. Plano Intermediário (300 minutos, 10GB de internet) - R$ 80")
print("3. Plano Avançado (500 minutos, 20GB de internet) - R$ 120")

plano = input("Digite o número correspondente ao seu plano: ")

# Entrada do usuário para minutos e GB utilizados
minutos_utilizados = int(input("Digite a quantidade de minutos utilizados: "))
gb_utilizados = float(input("Digite a quantidade de GB utilizados: "))

# Cálculo do valor total da fatura
resultado = calcular_fatura(plano, minutos_utilizados, gb_utilizados)

# Exibe o resultado
if resultado:
    valor_total, nome_plano, custo_minutos_excedentes, custo_gb_excedentes = resultado
    print(f"\nPlano escolhido: {nome_plano}")
    print(f"Valor do plano: R$ {valor_total - custo_minutos_excedentes - custo_gb_excedentes:.2f}")
    if custo_minutos_excedentes > 0:
        print(f"Minutos excedentes: R$ {custo_minutos_excedentes:.2f}")
    if custo_gb_excedentes > 0:
        print(f"GB excedentes: R$ {custo_gb_excedentes:.2f}")
    print(f"Valor total da fatura: R$ {valor_total:.2f}")
else:
    print("Erro: Plano inválido.")
