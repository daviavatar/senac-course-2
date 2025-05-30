try:
    num1 = int(input('Digite um n°:\n'))
    num2 = int(input('Digite um n°:\n'))

    divisao = (num1) / (num2)
    resultado = round(divisao, 2)

    print(f'O resultado da divisão é {resultado}')

except ZeroDivisionError:
    print('Divisão por zero não é permitido')

except ValueError:
    print('Digite um N° Válido')
    
except:
    print('Erro inesperado')