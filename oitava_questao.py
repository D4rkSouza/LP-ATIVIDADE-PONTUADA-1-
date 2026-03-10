# QUESTÃO 8
import os
os.system('cls')

cor=str(input('Digite a Cor Escolhida: ')).lower()

match cor:
    case 'verde':
        valor=print('O CD custa R$10,00')
    case 'azul':
        valor=print('O CD custa R$20,00')
    case 'amarelo':
        valor=print('O CD custa R$30,00')
    case 'vermelho':
        valor=print('O CD custa R$40,00')