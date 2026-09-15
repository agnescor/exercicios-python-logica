# Exercicio 02 - pedido na lanchonete

titulo = "Calculo do pedido na lanchonete"
produto = "hamburguer"
preco = 18.50
quantidade = 3
desconto = 5.00

subtotal = preco * quantidade
total = subtotal - desconto

# :.2f deixa o numero sempre com 2 casas decimais, tipo preco de verdade
print(f"""
{titulo}
Produto: {produto}
Pedido de {quantidade} unidades a R$ {preco:.2f} cada
Desconto: R$ {desconto:.2f}

Subtotal: R$ {subtotal:.2f}
Total a pagar: R$ {total:.2f}
""")
