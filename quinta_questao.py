# QUESTÃO 5
import os
os.system('cls')

print('Insira 2 Valores Inteiros')
v1=float(input('Primeiro Valor: '))
operador=(input('Insira o Operador Matemático: '))
v2=float(input('Segundo Valor: '))

soma=(v1 + v2)
subt=(v1 - v2)
mult=(v1 * v2)
divi=(v1 / v2)

match operador:
    case '+':
        resultado=(soma)
    case '-':
        resultado=(subt)
    case '*':
        resultado=(mult)
    case '/':
        resultado=(divi)
        
print(f'Tipo de Operação: {operador}')
print(f'Resultado: {resultado}')