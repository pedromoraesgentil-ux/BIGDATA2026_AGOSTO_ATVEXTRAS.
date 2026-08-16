 #ATIVIDADE COD-06 
#Uma empresa oferece um bônus aos funcionários de acordo com o valor de suas vendas no mês. Crie um algoritmo que receba o salário e o valor das vendas e calcule o salário final considerando o bônus. 
#Quando o valor das vendas for superior a R$ 1.000, o funcionário receberá um bônus de R$ 100. Caso contrário, receberá um bônus de R$ 20. 

#Ao final, informe o salário inicial, o bônus recebido e o salário final. 


salario_inicial = float(input("Digite o salário inicial: R$"))
valor_vendas = float(input("digite o valor das vendas:R$"))

if valor_vendas >1000: 
    salario_final = salario_inicial + 100
    print(f'Salario final com bonus de R$100,00 é R${salario_final:.2f}')

else:
    salario_final = salario_inicial + 20
    print(f'Salario final com bonus de R$20,00 é R${salario_final:.2f}')
    