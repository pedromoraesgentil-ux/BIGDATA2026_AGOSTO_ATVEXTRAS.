#ATIVIDADE COD-01 

#Uma loja oferece 16% de desconto nas compras com valor superior a R$ 250.  
#Crie um algoritmo, que solicite o valor da compra e informe o valor a ser pago, após a aplicação do desconto, quando houver. 

valor_compra = float(input("Digite o valor da compra: R$"))
if valor_compra >= 250:
    desconto = valor_compra * 0.16 
    valor_final = valor_compra-desconto
    print("O valor da compra com desconto é: R$", valor_final)
else:
    print("O valor da compra é: R$", valor_compra)
