# QUESTÃO 2
import os
os.system('cls')

nome=input('Digite seu Nome Completo: ')
sexo=input('Informe o seu Sexo: ').lower()
est_civil=input('Informe seu estado civil: ').lower()

if sexo == 'feminino' and est_civil == 'casada':
    tempo_casada=input('Informe a quanto tempo você é casada(EM ANOS): ')
    print(f'Nome: {nome} \nSexo: {sexo} \nEstado civil: {est_civil} \nTempo de Casada: {tempo_casada} anos')
else:
    print(f'Nome: {nome} \nSexo: {sexo} \nEstado civil: {est_civil}')