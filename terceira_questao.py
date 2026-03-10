# QUESTÃO 3
import os
os.system('cls')

print('Digite Apenas Números Inteiros')
print('''Valores iguais irão somar
Valores diferentes irão multiplicar''')
valor_1=int(input('Insira o Primeiro Valor: '))
valor_2=int(input('Insira o Segundo Valor: '))

if valor_1 == valor_2:
    resultado=(valor_1 + valor_2)
else:
    resultado=(valor_1 * valor_2)
    
print('O resultado é: ', resultado)