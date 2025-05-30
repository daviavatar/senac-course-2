print('BEM VINDO AO SENAC\n')

curso = int(input('Qual curso você deseja fazer conosco:\n1- Analise de Dados\n2 -Power BI\n3 - Desenvolvimento de Banco de Dados\n4- Outros\n Qual a sua opção?: '))

match curso:
    case 1:
        print('Parabéns por escoler Analise de Dados')
    case 2:
        print('Parabéns por escolher Power BI')
    case 3:
        print('Parabéns por escolher Banco de dados')
    case 4:
        print('Acesse o nosso site e veja as outras opções')
    case _:
        print('Opção Inválida')