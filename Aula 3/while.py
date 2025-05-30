'''contador = 0

while contador <= 5:
    print(f'N° {contador}')
    contador += 1'''

'''while True:
    senha = input('Digite a senha: \n')
    
    if senha == '123':
        print('Acesso liberado')
        break
    else:
        print('Acesso negado')'''

lista = []

while True:
    try:
        nome = input('Digite um nome: ')

        if not nome.isalpha():
            raise ValueError("Digite um nome valido")

        lista.append(nome)
        sair = input('Deseja adicionar mais um nome?').lower()
        if sair != 'sim':
            break

    except ValueError as e:
        print(e)

print(lista)

    


    


    


