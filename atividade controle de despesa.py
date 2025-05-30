print('Bem vindo a Empresa\n')

Limite = float(input('\nQual o seu limite de cartão?:'))
Valor = float(input('\nQual o valor da compra que deseja realizar?:'))

if Limite >= Valor:
    print('A sua compra foi aprovada')
else:
    print('A sua compra foi negada')
