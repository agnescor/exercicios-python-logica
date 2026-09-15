# Exercicio 03 - pedindo dados pro usuario e montando um comprovante de aluguel

def formatar_real(valor):
    # troca o ponto e a virgula pra ficar no formato brasileiro (1.234,56)
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


print("=" * 50)
print(" ALUGUEL DE BICICLETAS")
print("=" * 50)

nome_cliente = input("Nome do cliente: ")
bicicleta = input("Modelo da bicicleta: ")
preco_hora = float(input("Preco por hora (R$): "))
horas = int(input("Quantidade de horas: "))
desconto_pct = float(input("Percentual de desconto (%): "))

subtotal = preco_hora * horas
valor_desconto = subtotal * (desconto_pct / 100)
total = subtotal - valor_desconto
valor_medio = total / horas

print("\n" + "=" * 50)
print(" COMPROVANTE DO ALUGUEL")
print("=" * 50)
print(f"Cliente: {nome_cliente}")
print(f"Bicicleta: {bicicleta}")
print(f"Horas alugadas: {horas} hora(s)")
print(f"Preco por hora: R$ {formatar_real(preco_hora)}")
print("-" * 50)
print(f"Subtotal: R$ {formatar_real(subtotal)}")
print(f"Desconto: {desconto_pct:.0f}% (R$ {formatar_real(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR: R$ {formatar_real(total)}")
print(f"Valor medio por hora: R$ {formatar_real(valor_medio)}")
print("=" * 50)
