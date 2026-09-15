# Exercicio 04 - if / elif / else
# regra: menor de 14 nao entra, 14+ com matricula ativa entra, 14+ sem matricula precisa se cadastrar

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade nao pode ser negativa.")
            continue
        break
    except ValueError:
        print("Digite um numero valido.")

while True:
    resposta = input("Sua matricula esta ativa? (sim/nao): ").strip().lower()
    if resposta in ("sim", "s"):
        matricula_ativa = True
        break
    elif resposta in ("nao", "n"):
        matricula_ativa = False
        break
    else:
        print("Responda com 'sim' ou 'nao'.")

if idade < 14:
    mensagem = "Acesso nao permitido"
elif matricula_ativa:
    mensagem = "Entrada liberada"
else:
    mensagem = "Va ate a recepcao se cadastrar"

print("\n" + "=" * 40)
print(f"Idade: {idade} | Matricula ativa: {'Sim' if matricula_ativa else 'Nao'}")
print(f"Status: {mensagem}")
print("=" * 40)
