print('Bem vindo as opções')

num1 = float(input('Opção 1:'))
num2 = float(input('Opção 2:'))
opcoes = int(input('Qual operação você quer fazer?\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- módulo\n'))

match opcoes:
    case 1:
        print(f'O valor da soma das opções é:{num1 + num2}')
    case 2:
        print(f'A subtração das opções é:{num1 - num2}')
    case 3:
        print(f'A multiplicação das opções é:{num1 * num2}')
    case 4:
        print(f'A divisão das opções é:{num1 / num2}')
    case 5: 
        print(f'O módulo das opções é:{num1 % num2}')

