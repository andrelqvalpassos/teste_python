infracoes = int(input("Quantas infrações você tem: "))

if infracoes == 0:
    print(f"Motorista exemplar")

elif infracoes <=3 :
    print(f"Motorista atento")

elif 4 <= infracoes <= 6: #Entre um numero e outro (exemplo entre 4 a 6)
    print(f"Motorista desatento")

elif infracoes > 6:
    print(f"Motorista Perigoso")
else:
    print(f"Invalido")