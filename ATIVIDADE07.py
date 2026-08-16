#ATIVIDADE COD-07 

#Um motorista deseja verificar, se o seu carro apresenta um consumo econômico de combustível. Crie um algoritmo que solicite a distância percorrida e a quantidade de combustível utilizada, calcule o consumo do veículo e informe se o carro é econômico ou não. 
#Considere que um carro é considerado econômico quando percorre pelo menos 12 km com um litro de combustível. 

distancia_percorrida = float(input("Digite a distância percorrida em km: "))
quantidade_combustivel = float(input("Digite a quantidade de combustível utilizada em litros: "))

consumo = distancia_percorrida / quantidade_combustivel

if consumo >= 12:
    print("O carro é econômico.")
else:
    print("O carro não é econômico.")