#ATIVIDADE COD-03 

#Uma instituição financeira utiliza a renda mensal e a pontuação de crédito para analisar a aprovação de crédito. Crie um algoritmo que solicite essas informações e informe se o crédito foi aprovado ou não. 
#Considere que o crédito será aprovado quando a renda mensal for de pelo menos R$ 3.000 ou a pontuação de crédito for igual ou superior a 700. 

renda_mensal = float(input("Digite a renda mensal: R$"))
pontuacao_credito = int(input("Digite a pontuação de crédito:"))

if renda_mensal >= 3000 or pontuacao_credito >= 700: 
    print("Crédito aprovado!")
else:
    print("Crédito não aprovado.")