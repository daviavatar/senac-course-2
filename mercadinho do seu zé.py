print('Bem vindo ao mercadinho do seu zé')

valor = float(input('Valor total da compra:'))
pagamento = float(input('Qual a forma de pagamento?\n1 - cartão\n2 - dinheiro\n3 - pix\n'))

match pagamento:
    case 1:
        print(f'O valor da sua compra é: {valor + (valor * 0.0485)}')
    case 2:
        print(f'o valor da sua compra é:{valor - (valor * 0.0270)}')
    case 3:
        print(f'O valor da sua compra é:{valor - (valor * 0.0195) }')
    case _:
        print(f'Forma de pagamento invalida')



