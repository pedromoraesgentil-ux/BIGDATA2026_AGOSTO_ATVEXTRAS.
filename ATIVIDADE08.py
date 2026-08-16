#Uma loja permite o parcelamento de compras a partir de R$ 100. Crie um algoritmo que solicite o valor total da compra e informe as condições de pagamento de acordo com o valor. 

#Considere que: 
#compras a partir de R$ 100 podem ser parceladas; 
#compras acima de R$ 500 podem ser parceladas em até 5 vezes sem juros; 
#para as demais compras elegíveis podem ser parceladas em até 3 vezes sem juros; 
#compras abaixo de R$ 100 devem ser pagas à vista. 



valor_total = float(input('Digite o valor total da compra: '))

if valor_total >= 500:
    print('O valor pode ser parcelado em até 5x sem juros')
elif valor_total >= 100:
    print('O valor pode ser parcelado em 3x sem juros')
else:
    print('O valor deve ser pago à vista!!')

