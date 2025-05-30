Lista = []

print('Bem vindo ao senac: \n')

while True: 
    try:
        nome = input('Digite seu nome: \n')
        if not nome.isalpha():
            raise ValueError('Digite um nome válido')
        break
    except ValueError as e:
        print(e)

while True:
    try:
        cpf = int(input('Digite o seu CPF: \n'))
        break
    except:
        print('Digite o seu CPF:')

print('ESCOLHA O SEU CURSO QUE VOCÊ DESEJA:\n 1- ANÁLISE DE DADOS\n 2 - POWER BI ')

while True:
    try:
        opção = int(input(' Digite a opção de curso desejada:'))
        if opção in [1,2]:
            break
    except ValueError:
        print('Digite uma opção válida')

match opção:
    case 1:
        print('Bem vindo ao curso de análise de dados ')
    case 2:
        print('Bem vindo ao curso de PowerBI')

 

