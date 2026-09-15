# Exercicio 01 - variaveis e f-strings

personagem = "Guerreiro"
print(personagem)

# a multiplicacao acontece antes da soma, entao da 23 e nao 33
pontos = 5 + 6 * 3
print(pontos)

mensagem = f"{personagem} entrou na batalha!"
print(mensagem)

texto = "5 + 6 * 3"
resultado = 5 + 6 * 3

print(texto)
print(resultado)

# pra juntar string com numero usando +, precisa converter com str()
expressao = texto + " = " + str(resultado)
print(expressao)

# com f-string fica mais simples, nao precisa converter nada
expressao2 = f"{texto} = {resultado}"
print(expressao2)
