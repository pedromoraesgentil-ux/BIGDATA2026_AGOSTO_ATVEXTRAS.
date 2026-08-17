#ATIVIDADE 01 PTD - COD-10 

#Uma calculadora precisa realizar diferentes operações com dois números. Crie um algoritmo que solicite dois números ao usuário, calcule a soma, subtração, multiplicação, divisão e o resto da divisão e imprima os resultados no final. 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))    

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto_divisao = num1 % num2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da Divisão: {resto_divisao}")