# QUESTÃO 9
import os
os.system('cls')

renda=float(input('Informe Sua Renda Mensal: '))
emprestimo=float(input('Informe o Valor Desejado para Empréstimo: '))
prestacao=int(input('Informe a Quantidade de Prestações: '))

total_emprestimo=(emprestimo / prestacao)

if emprestimo <= renda*10 and total_emprestimo <= renda*10:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Não Aprovado')