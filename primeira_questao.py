# QUESTÃO 1
import os
os.system('cls')

valor_1=float(input('Insira o Primeiro Valor: '))
valor_2=float(input('Insira o Segundo Valor: '))
valor_3=float(input('Insira o Terceiro Valor: '))

soma=(valor_1 + valor_2)
mmc=(valor_3)

if soma > mmc:
    print(soma, 'É maior que', mmc)
    print('A soma dos 2 primeiros valores é maior que o 3 valor')
elif soma == mmc:
    print(soma, 'É igual a', mmc)
    print('A soma dos 2 primeiros valores é igual ao 3 valor')
elif soma < mmc:
    print(soma, 'É menor que', mmc)
    print('A soma dos 2 primeiros valores é menor que o 3 valor')
