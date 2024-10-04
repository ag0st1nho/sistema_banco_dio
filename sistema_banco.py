menu = '''
[1] depositar
[2] sacar 
[3] extrato 
[4] sair
===> '''

saldo = 0.0
limite = 500.0
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f"Depósito realizado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou, o valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação não realizada, limite para saque insuficiente.")
        elif excedeu_limite:
            print("Operação não realizada, valor solicitado superior ao limite disponível.")
        elif excedeu_saque:
            print("Operação não realizada, limite para saque diário atingido.")
        elif valor > 0:  
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou, o valor informado é inválido.")
    
    elif opcao == "3":
        def mostrar_extrato(saldo, extrato):
            extrato = (
                "\n_____________EXTRATO_____________\n"
                f"{'Não foram realizadas movimentações.' if not extrato else extrato}\n"
                f"Saldo: R$ {saldo:.2f}\n"
                "_____________________________"
            )
            print(extrato)

        mostrar_extrato(saldo, extrato)
        
    elif opcao == "4":
        print("Obrigado por usar nosso sistema. Até logo!")
        break  
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
