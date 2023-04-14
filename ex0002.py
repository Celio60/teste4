nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
alt1 = float(input('Digite a altura um: '))
alt2 = float(input('Dgite a altura dois: '))
peso1 = int(input('Informe o peso um: '))
peso2 = int(input('Informe o peso dois: '))
if(alt1 > alt2):
    print(f'A pessoa {nome1} é mais alta')
else:
    print(f'A pessoa {nome2} é mais alta')
if(peso1 > peso2):
    print(f'A pessoa {nome1} é mais pesado ')
else:
    print(f'A pessoa {nome2} é mais pesado')