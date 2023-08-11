menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3



while True:
    opcao = input(menu)
    if opcao == "d" :
        vlr_dep = float(input("Valor a depositar: "))

        if vlr_dep > 0:
            saldo  += vlr_dep
            extrato += f"Depósito: R$ {vlr_dep:.2f}\n"
        else:
            print("Valor inválido, tente novamente.")

    elif opcao == "s":
        vlr_saque = float(input("Valor a sacar: "))
        saque_excedido = qtd_saques >= LIMITE_SAQUES
        saldo_excedido = vlr_saque > saldo
        limite_excedido = vlr_saque > limite

        if saldo_excedido:
            print("Operação não efetuada, saldo insuficiente.")
        elif limite_excedido:
            print("Operação não efetuada, valor de saque não permitido.")
        elif saque_excedido:
            print("Operação não efetuada, limite de saques excedido.")
        elif vlr_saque > 0:
            saldo -= vlr_saque
            extrato += f"Saque: R$ {vlr_saque:.2f}\n"
            qtd_saques += 1
        else:
            print("Valor inválido, tente novamente.")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas mov imentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamento.")