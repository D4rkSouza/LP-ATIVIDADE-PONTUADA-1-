# QUESTÃO 4
import os
os.system('cls')

print('''
        |    ATÉ 5KG     |   ACIMA DE 5KG  |
MORANGO | R$2,50 por KG  | R$2,20 por KG   |
MAÇÃ    | R$1,80 por KG  | R$1,50 por KG   |
''')

morango=float(input('Morangos em Kg: '))
maca=float(input('Maçãs em Kg: '))

if morango <= 5:
        mo_valor=(morango * 2.5)
elif morango > 5:
        mo_valor=(morango * 2.2)
        
if maca <= 5:
        ma_valor=(maca * 1.8)
elif maca > 5:
        ma_valor=(maca * 1.5)

if maca or morango >10:
        desconto=(ma_valor * 0.1)
        desconto=(mo_valor * 0.1)
        
valor_maca=(ma_valor - desconto)
valor_morango=(mo_valor - desconto)
total_a_pagar=(valor_maca + valor_morango)
        
print(f'Valor Maçãs {valor_maca} \nValor Morangos {valor_morango} \nValor a pagar {total_a_pagar}')