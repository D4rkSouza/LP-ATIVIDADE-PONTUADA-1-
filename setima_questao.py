# QUESTÃO 7
import os
os.system('cls')

nome=(input('Insira o Nome do Produto: '))
quant=int(input('Insira a quantidade: '))
preco=float(input('Insira o Preço Unitário: '))

total=(preco * quant)

if quant <= 5:
    desconto=(total * 0.02)
elif 10 >= quant > 5:
    desconto=(total * 0.03)
elif quant > 10:
    desconto=(total * 0.05)

total_pagar=(total - desconto)
    
print(f'Produto {nome} \nValor Total R${total} \nDesconto R${desconto} \nTotal a Pagar R${total_pagar}')