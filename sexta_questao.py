# QUESTÃO 6
import os
os.system('cls')

print('Portal do Aluno')
nota1=float(input('Informe sua Primeira Nota: '))
nota2=float(input('Informe sua Segunda Nota: '))

media=((nota1 + nota2) / 2)
situacao=('')

if media >= 6:
    situacao=('Parabéns, Aprovado')
elif 6 > media > 4:
    situacao=('Recuperação')
elif media < 4:
    situacao=('Reprovado')
    
print(f'Sua Média é de {media} pontos')
print(situacao)