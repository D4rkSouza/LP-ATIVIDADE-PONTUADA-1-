# QUESTÃO 4
import os
os.system('cls')

print('''
        |    ATÉ 5KG     |   ACIMA DE 5KG  |
MORANGO | R$2,50 por KG  | R$2,20 por KG   |
MAÇÃ    | R$1,80 por KG  | R$1,50 por KG   |
''')

morango = float(input('Morangos em Kg: '))
maca = float(input('Maçãs em Kg: '))

# valor morango
if morango <= 5:
        mo_valor = morango * 2.5
elif morango > 5:
        mo_valor = morango * 2.2

# valor maçã        
if maca <= 5:
        ma_valor=(maca * 1.8)
elif maca > 5:
        ma_valor=(maca * 1.5)

# valor total
valor_total = mo_valor + ma_valor
peso_total = maca + morango

# desconto
if peso_total > 10 or valor_total > 15:
        desconto = (valor_total * 0.1)
else:
        desconto = 0
        
total_a_pagar=(valor_total - desconto)

print(f'Valor Maçãs {ma_valor} \nValor Morangos {mo_valor} \nDesconto {desconto} \nValor a pagar {total_a_pagar}')