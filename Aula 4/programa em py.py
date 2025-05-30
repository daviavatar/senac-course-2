

print('BEM VINDO A ELEIÇÃO') 

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
        idade = int(input(' Digite a sua idade:\n'))
        if idade >= 14 :
            
            break
        else:
            print('Infelizmente você não tem idade para votar')
    except:
        print()

voto1 = 0
voto2 = 0
voto3 = 0

while True:
    while True:
        try:
            print('Os candidatos são:\n 1 -GOKU\n 2 - Naruto\n 3 - Luffy')
            cadidato = int(input('Qual candidato você irá votar?\n '))
            if cadidato in [1,2,3]:
                match cadidato:
                    case 1:
                        print('Você votou em Goku')
                        voto1 += 1
                    case 2:
                        print('Você votou em Naruto')
                        voto2 += 1
                    case 3:
                        print('Você votou em Luffy')
                        voto3 += 1
                    case _:
                        print('Digite um candidato inválido')
                break
            else:
                print('Candidato inválido')
        except ValueError:
            print('Digite um número valido')

    votar = input('Deseja votar novamente? S/N\n').upper()
    if votar != 'S':
        break
    else:
        print()
   

    print(f'O resultado atual da votação é:\n 1 - Goku = {voto1}\n 2 - Naruto = {voto2}\n3 - Luffy = {voto3}')

if voto1 > voto2 and voto1 > voto3:
    print('O vencedor é o Goku')
elif voto2 > voto1 and voto2 > voto3:
    print('O vencedor é o naruto')
elif voto3 > voto1 and voto3 > voto2:
    print('O vencedor é o Luffy')
else:
    print('Teve empate')
