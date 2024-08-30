import os
os.system('cls')
import random 

print('-----------Pedra,Papel,Tesoura-----------')

movimentos = ['pedra','papel','tesoura']
pontopc = 0
ponto = 0

movimentopc1 = random.choice(movimentos)

def jogo(movimentopc1):
    pontopc = 0
    ponto = 0
    while True:
        movimento1 = input('(Quando quiser acabar, escreva "Exit")\nPedra, papel ou tesoura?: ').lower()

        if movimentopc1 == movimento1:
            os.system('cls')
            print('Empate')
            pontopc += 1
            ponto += 1
        elif movimentopc1 == 'pedra' and movimento1 == 'tesoura':
            os.system('cls')
            print('O pc ganhou.')
            pontopc += 1
        elif movimentopc1 == 'tesoura' and movimento1 == 'papel':
            os.system('cls')
            print('O pc ganhou.')
            pontopc += 1
        elif movimentopc1 == 'papel' and movimento1 == 'pedra':
            os.system('cls')
            print('O pc ganhou.')
            pontopc += 1
        elif movimento1 == 'pedra' and movimentopc1 == 'tesoura':
            os.system('cls')
            print('Você ganhou.')
            ponto += 1
        elif movimento1 == 'tesoura' and movimentopc1 == 'papel':
            os.system('cls')
            print('Você ganhou.')
            ponto += 1
        elif movimento1 == 'papel' and movimentopc1 == 'pedra':
            os.system('cls')
            print('Você ganhou.')
            ponto += 1
        elif movimento1 == 'exit':
            break
        else:
            os.system('cls')
            print('Entrada inválida.')
        print(f'A sua quantidade de pontos é {ponto}')

jogo(movimentopc1)
