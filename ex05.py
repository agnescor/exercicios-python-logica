# Exercicio 05 - formas de tomar decisao em Python
# if aninhado, if/elif encadeado, match/case e match/case com guarda

def verificar_credito():
    print("\n-- Verificar credito (if aninhado) --")
    renda = float(input("Renda mensal (R$): "))
    score = float(input("Score de credito (0 a 1000): "))

    if renda >= 2000:
        if score >= 600:
            print("Credito aprovado")
        else:
            print("Credito negado por score baixo")
    else:
        print("Credito negado por renda insuficiente")


def classificar_vendedor():
    print("\n-- Classificar vendedor (if/elif) --")
    vendas = float(input("Total vendido no mes (R$): "))

    if vendas >= 20000:
        print("Vendedor destaque")
    elif vendas >= 10000:
        print("Vendedor bom")
    elif vendas >= 5000:
        print("Vendedor regular")
    else:
        print("Vendedor abaixo da meta")


def processar_menu():
    print("\n-- Menu de atendimento (match/case) --")
    print("1 - Consultar estoque | 2 - Registrar venda | 3 - Sair")
    opcao = input("Opcao: ")

    match opcao:
        case "1":
            print("Consultando estoque...")
        case "2":
            print("Registrando venda...")
        case "3":
            print("Saindo...")
        case _:
            print("Opcao invalida")


def avaliar_cliente():
    print("\n-- Avaliar cliente (match/case com guarda) --")
    nome = input("Nome: ")
    total_compras = float(input("Total de compras (R$): "))
    atrasos = int(input("Numero de pagamentos atrasados: "))

    match (total_compras, atrasos):
        case (t, _) if t >= 10000:
            print(f"{nome}: cliente VIP")
        case (t, a) if t >= 3000 and a <= 1:
            print(f"{nome}: cliente fiel")
        case (t, a) if t >= 1000 and a <= 2:
            print(f"{nome}: cliente regular")
        case _:
            print(f"{nome}: cliente em risco")


def main():
    opcoes = {
        "1": verificar_credito,
        "2": classificar_vendedor,
        "3": processar_menu,
        "4": avaliar_cliente,
    }

    while True:
        print("\n1-Credito  2-Classificar  3-Menu  4-Avaliar  5-Sair")
        opcao = input("Escolha: ")

        if opcao == "5":
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    main()
