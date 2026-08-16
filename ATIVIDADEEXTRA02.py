#ATIVIDADE COD-02 

#Uma loja oferece desconto de 16% nas compras que atendam a pelo menos uma das condições: valor superior a R$ 250 ou pagamento realizado pelo PIX. 
#Crie um algoritmo que solicite o valor da compra e a forma de pagamento e informe o valor final a pagar. 
#Considere que, quando uma dessas condições for atendida, o desconto deverá ser aplicado. Caso contrário, o cliente deverá pagar o valor integral. 

valor_compra = float(input("Digite o valor da compra: R$"))
forma_pagamento = input("Digite a forma de pagamento (PIX ou outro): ")


if valor_compra >=250 or forma_pagamento .upper()== "PIX":
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print("O valor da compra com desconto é: R$", {valor_final})
else:
    print(f"O valor da compra é: R${valor_compra:.2f}") 
 


