while True:
    try:
        num1 = float(input('Digite o primeiro número: \n'))
        break
    except ValueError:
       print('Digite um número: \n')
while True:
    try:
        opção = input('operação (+,-,*,/): ')
        if opção in ['+','-','*','/']:
            break
    except ValueError:
        print(f'Erro:')
        
while True:
    try:
        num2 = int(input('Digite outro numero: '))
        if opção == '/' and num2 == 0:
            raise ValueError('Não é possível dividir por zero.')
        break
    except ValueError as e:
        print(f'Erro: {e}')

if opção == '+':
    resultado = num1 + num2
    print(f' O resultado da soma é: {resultado}')
elif opção == '-': 
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif opção == '*':
    resultado = num1 * num2
    print(f' O resultado da multiplicação é: {resultado} ')
elif opção == '/':
    resultado = num1 / num2
    print(f' O resultado da divisão é: {resultado}')

      

     


































'''opções = float(input('1 - soma\n2 - divisão\n3 - subtração\n 4 - multiplicação'))
        num2 = float(input('Digite o segundo número: \n'))'''