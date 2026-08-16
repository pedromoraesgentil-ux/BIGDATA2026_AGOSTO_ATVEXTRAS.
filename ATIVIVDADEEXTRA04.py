#ATIVIDADE COD-04 

#Um banco permite que seus clientes realizem saques de até R$ 1.000, desde que haja saldo suficiente na conta. Crie um algoritmo que solicite o valor do saque, verifique se a operação pode ser realizada e atualize o saldo da conta. 
#O algoritmo deve informar o valor sacado e o saldo atual da conta. 

saldo_conta = float(input("Digite o saldo da conta: R$"))
valor_saque = float(input("Digite o valor do saque: R$"))

if valor_saque > 1000:
    print("O valor do saque excede o limite permitido de R$ 1.000.")
elif valor_saque > saldo_conta:
    print("Saldo insuficiente para realizar o saque.")
else:
    saldo_atual = saldo_conta - valor_saque 
    print(f'O valor sacado foi: R${valor_saque:.2f}')
    print(f"O saldo atual da conta é: R${saldo_atual:.2f}")