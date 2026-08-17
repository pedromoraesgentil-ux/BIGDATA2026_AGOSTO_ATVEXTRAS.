#Uma instituição de ensino precisa calcular a média final dos alunos a partir de quatro notas.  
#Crie um algoritmo que solicite as quatro notas, calcule a média e informe, se o aluno foi aprovado ou reprovado. 
#Considere que a média para aprovação é 7. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))  

media = (nota1 + nota2 + nota3 + nota4) / 4 
print("A média final do aluno é:", media)

if media >= 7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")