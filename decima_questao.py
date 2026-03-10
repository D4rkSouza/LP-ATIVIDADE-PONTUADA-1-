# QUESTÃO 10
import os
os.system('cls')

tipo=str(input('Insira o Tipo de Combustivel Desejado: ')).lower()
quant=int(input('Insira a Quantidade em Litros: '))

if tipo == 'gasolina':
    tipo=('gasolina')
    valor=6.59
elif tipo == 'alcool':
    tipo=('alcool')
    valor=3.79
    
valor_total=(valor * quant)

# desconto alcool
if quant <= 25:
    a_desconto=(valor_total * 0.02)
    valor_pagar=(valor_total - a_desconto)
elif quant > 25:
    a_desconto=(valor_total * 0.04)
    valor_pagar=(valor_total - a_desconto)
    
# desconto gasolina
if quant <= 25:
    g_desconto=(valor_total * 0.03)
    valor_pagar=(valor_total - g_desconto)
elif quant > 25:
    g_desconto=(valor_total * 0.05)
    valor_pagar=(valor_total - g_desconto)
    
if tipo == 'gasolina':
    print(f'Valor Total {valor_pagar}')